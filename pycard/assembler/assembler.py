#!/usr/bin/env python3

class Assembler:
  labels = []
  current_line = 1
  current_address = 0
  deck = []

  def __init__(self, lines):
    self.processLines(lines)

  def processLine(self, line):
    if line.isspace(): return

    token = line.split(maxsplit=1)[0]
    
    if token.startswith(';'):
      print(f"Comment on line {self.current_line}")
      return
    
    elif token == ".org": pass # TODO: Implement .org directive.

    elif token == "#define": pass # TODO: Implement define macro.
    elif token == "#include": pass # TODO: Implement include macro.

    elif token == "INP": pass
    elif token == "CLA": pass
    elif token == "ADD": pass
    elif token == "TAC": pass
    elif token == "SFT": pass
    elif token == "OUT": pass
    elif token == "STO": pass
    elif token == "SUB": pass
    elif token == "JMP": pass
    elif token == "HRS": pass
    
  def processLines(self, lines):
    for line in lines:
      self.processLine(line)
      self.current_line += 1

if __name__ == '__main__':
  import main
  main.main()
  