#!/usr/bin/env python3

class Assembler:
  labels = []
  current_line = 1

  def __init__(self, lines):
    self.processLines(lines)

  def processLine(self, line):
    for token in line.split():
      if token.startswith(';'):
        print(f"Comment on line {self.current_line}")
        return

    
  def processLines(self, lines):
    for line in lines:
      self.processLine(line)
      self.current_line += 1

if __name__ == '__main__':
  import main
  main.main()