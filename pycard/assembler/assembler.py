#!/usr/bin/env python3

def isAddress(data): return isData(data, 2)

def isData(data, datalength=3):
  return data.isnumeric() and len(data) == datalength
  
def isLabel(data): return data.isalnum()

class Assembler:
  labels = {}
  current_line = 1
  current_address = 0
  increment_address = False
  deck = []

  preprocessLines = []

  def __init__(self, lines):
    self.preprocess(lines)

    for line in self.preprocessLines:
      print(line)
  
  def cla(self, line):
    """ CLA - Clear Load Address """
    tokens = []
    for token in line.split():
      if ';' not in token:
        tokens.append(token)
      else:
        break
    
    if len(tokens) > 2:
      raise ValueError("Too many values.")
    elif not isAddress(tokens[1]) and not isLabel(tokens[1]):
      raise ValueError("Unexpected value.")

    self.preprocessLines.append(f"{self.current_address:03}: CLA {tokens[1]}")
    self.current_address += 1

  def data(self, line):
    tokens = line.split()
    
    if len(tokens) < 2:
      raise ValueError("Expected value.")
    
    for token in tokens[1:]:
      if not isData(token):
        raise ValueError("Unexpected value.")

    for token in tokens[1:]:
      self.preprocessLines.append(f"{self.current_address:03}: {token}")
      self.current_address += 1

  def label(self, line):
    tokens = line.split()

    labelname = tokens[0].split(':')[0]

    self.labels[labelname] = self.current_address
    
  def org(self, line):
    tokens = line.split()

    if len(tokens) > 2:
      raise ValueError("Too many values.")
    elif not isData(tokens[1]):
      raise ValueError("Unexpected value.")

    self.current_address = int(tokens[1])

  def preprocessLine(self, line):
    if line.isspace(): return

    self.increment_address = False

    token = line.split(maxsplit=1)[0]
    
    if token.startswith(';'): return

    elif ':' in token: self.label(line)
    
    elif token == ".data": self.data(line)
    elif token == ".org": self.org(line)

    elif token == "#define": pass # TODO: Implement define macro.
    elif token == "#include": pass # TODO: Implement include macro.

    elif token == "INP": pass
    elif token == "CLA": self.cla(line)
    elif token == "ADD": pass
    elif token == "TAC": pass
    elif token == "SFT": pass
    elif token == "OUT": pass
    elif token == "STO": pass
    elif token == "SUB": pass
    elif token == "JMP": pass
    elif token == "HRS": pass

    #self.current_address += 1
  
  def preprocess(self, lines):
    self.preprocessLines = []
    for line in lines:
      self.preprocessLine(line)
      self.current_line += 1

if __name__ == '__main__':
  import main
  main.main()
