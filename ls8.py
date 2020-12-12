#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *


if len(sys.argv) != 2:
    print("Input is incorrect. Usage: python3 ls8.py mult.ls8")
    sys.exit(1)

cpu = CPU()
cpu.load(sys.argv[1])

cpu.run()


