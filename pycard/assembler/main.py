#!/usr/bin/env python3

import sys

from assembler import Assembler

def showUsage():
  print("Usage: assembler.py [INPUT] [OUTPUT]")

def main():
  if len(sys.argv) < 2: return showUsage()

  with open(sys.argv[1], 'r') as f:
    assembler = Assembler(f.readlines())

if __name__ == '__main__':
  main()
