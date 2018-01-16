# -*- coding: utf-8 -*-

from scapy.all import sniff, DHCP
import yaml
import importlib
import argparse

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


parser = argparse.ArgumentParser()
parser.add_argument('--config', default='config.yml')
parser.add_argument('runtype', choices=['detect', 'run'])
args = parser.parse_args()


def run(pkt, config):
    options = pkt[DHCP].options
    for option in options:
        if not isinstance(option, tuple):
            continue
        if 'requested_addr' in option:
            cdict = config[pkt.src]
            cdict['action'](*cdict['args'])
            break


def detect(pkt):
    if pkt.haslayer(DHCP):
        print "Button press detected: {}".format(pkt.src)


def main():
    if args.runtype == "detect":
        print "Waiting for a button press..."
        sniff(prn=detect, store=0, filter="udp")

    elif args.runtype == "run":
        module = importlib.import_module("action")
        with open(args.config, "r") as f:
            config = yaml.load(f)
            for mac, cdict in config.iteritems():
                cdict["action"] = getattr(module, cdict["action"])

            mac_id_list = list(config.keys())

        print "Waiting for the button press..."
        sniff(prn=lambda pkt: run(pkt, config), store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)


if __name__ == "__main__":
    main()
