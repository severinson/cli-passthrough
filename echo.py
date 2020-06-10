#!/usr/bin/env python3
# Echo input on stdin to stdout

import sys

def main():
    print("echo started with arguments", " ".join(sys.argv))
    for line in sys.stdin:
        print("echo " + line.strip(), file=sys.stdout)
        sys.stdout.flush()

if __name__ == '__main__':
    main()
