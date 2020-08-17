#!/usr/bin/python

import os
import sys
import json
import argparse
import re

from tax.receipt import Receipt
from tax.item import Item

RECEIPT_REG = r'(?P<quantity>\d+) (?P<imported>(imported )*)(?P<name>[\w ]+) at (?P<price>\d+.\d+)'

def parse_items(items, exempt_dict):
    "Read input receipt and returns its corresponding object"
    prog = re.compile(RECEIPT_REG)
    item_lst = []
    for line in items:
        item = prog.match(line).groupdict()
        item_lst.append(Item.from_dict(item,
                    exempt=True if item['name'] in exempt_dict else False))
    print(item_lst)
    return item_lst

def read_receipt(f_name):
    "Read input receipt and returns its corresponding object"
    item_lst = []
    with open(f_name, 'r') as f:
        for line in f:
            item_lst.append(line)
        return item_lst


def read_exempt(exempt_f_name='exempt.json'):
    "Read Json file listing tax-exempt products, and returns its dict"
    exmp_dict = {}
    with open(exempt_f_name, 'r') as f:
        categories = json.load(f)
        for c in categories['categories']:
            for p in c['products']:
                exmp_dict[p] = c['name']
    return exmp_dict


def main():
    "This application purpose is to compute tax on a given item list"
    parser = argparse.ArgumentParser()
    parser.add_argument('receipt', help='Input Receipt Text file name')
    parser.add_argument('--exempt', help='Tax exempt goods Json file name')
    args = parser.parse_args()

    exempt_dict = read_exempt()
    items = read_receipt(args.receipt)
    recpt = Receipt(parse_items(items, exempt_dict))

    print(recpt)

if __name__ == '__main__':
    sys.exit(main())
