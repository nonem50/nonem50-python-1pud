#!/usr/bin/env python3
"""nonem50-python-1pud."""
import sys,argparse
from utils import timestamp
def main():
    p=argparse.ArgumentParser(description="nonem50-python-1pud")
    p.add_argument("--version",action="version",version="1.0.0")
    p.add_argument("-v","--verbose",action="store_true")
    a=p.parse_args()
    if a.verbose:print(f"[{timestamp()}] nonem50-python-1pud v1.0.0")
    print(f"Hello from nonem50-python-1pud!")
    return 0
if __name__=="__main__":sys.exit(main())
