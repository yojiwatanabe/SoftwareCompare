#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is the main driver file that the user runs. It takes command line
# arguments and calls all of the other modules. There is one positional
# argument that this file takes and one optional should follow -i

import argparse
import dump_plugin_output
import process_dump
from sys import exit


def initiate_argparse():
    parser = argparse.ArgumentParser(description='Helper script to retrieve plugin output from Service Center scans')
    parser.add_argument('plugin_id',                    help='Plugin ID for the desired plugin output')
    parser.add_argument('-s', dest='search_list',      help='Input file for words to query output (e.g. -s queries.txt)')
    parser.add_argument('-R', dest='repo_list',        help='Input file for repositories to query (e.g. -R repos.txt)')
    parser.add_argument('-H', dest='host_list',        help='Input file for hosts to query (e.g. -H hosts.txt)')
    parser.add_argument('--ip_range', dest='ip_range', help='Range of IPs from which to gather data (e.g. --ip_range '
                                                            '127.0.0.1-192.168.0.1)')

    return parser.parse_args()


def main():
    args = initiate_argparse()

    try:
        dump_plugin_output.dump_plugin_data(args.plugin_id, args.repo_list, args.host_list, args.ip_range)
        process_dump.create_table(args.search_list)
    except Exception as e:
        print '###### ERROR'
        'Exception: [' + str(e) + ']:'
        exit(1)

    print "Created " + process_dump.OUTPUT_FILE


# # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
    main()
