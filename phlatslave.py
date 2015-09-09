#!/usr/bin/env python
import sys
import json


class PhlatSlave:
    def __init__(self, config_file_path):
        with open(config_file_path) as config_file:
            config = json.loads(config_file.read())
            config_file.close()
        self.node = config['node']
        self.jobs_url = config['jobs'] + '/api/jobs/' + self.node

    def do_work(self):
        print self.jobs_url


def main():
    if len(sys.argv) < 2:
        print "Usage: ./phlatslave.py </path/to/config>"
        exit()

    config_file_path = sys.argv[1]
    slave = PhlatSlave(config_file_path=config_file_path)
    slave.do_work()

if __name__ == "__main__":
    main()
