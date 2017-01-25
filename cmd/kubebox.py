#!/usr/bin/env python

import argparse
import sys
import os


WORK_DIR = os.getcwd()


class KubeBox:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Simple package tool for development in kubernetes',
            usage='''kubebox.py <command> [<args>]

Commands:
   create     Create new package for local deploy
   start      Starts package
''')
        parser.add_argument('command', help='Subcommand to run')

        args = parser.parse_args(sys.argv[1:2])

        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def create(self):
        parser = argparse.ArgumentParser(
            description='Create new package for local deploy')

        parser.add_argument('--p', action='store_true')

        args = parser.parse_args(sys.argv[2:])
        print('Running create with {}'.format(args.p))

    def start(self):
        parser = argparse.ArgumentParser(
            description='Download objects and refs from another repository')

        parser.add_argument('package')
        args = parser.parse_args(sys.argv[2:])
        print('Running start with {}'.format(args.package))


if __name__ == '__main__':
    KubeBox()
