#!/usr/bin/env python
import sys


class PhlatSlave:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def do_work(self):
        print self.config_file_path


def main():
    if len(sys.argv) < 2:
        print "Usage: ./phlatslave.py </path/to/config>"
        exit()

    config_file_path = sys.argv[1]
    slave = PhlatSlave(config_file_path=config_file_path)
    slave.do_work()

if __name__ == "__main__":
    main()
