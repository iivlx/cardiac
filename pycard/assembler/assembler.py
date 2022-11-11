#!/usr/bin/env python3

CARDIAC_INSTRUCTIONS = ["INP", "CLA", "ADD", "TAC", "SFT", "OUT", "STO", "SUB", "JMP", "HRS"]

def isAddress(data): return isData(data, 2)

def isData(data, datalength=3):
  return data.isnumeric() and len(data) == datalength
  
def isLabel(data): return data.isalnum()

def removeComments(line):
  tokens = []
  for token in line.split():
    if ';' not in token:
      tokens.append(token)
    else:
      break
  return tokens

class Assembler:
  labels = {}
  comments = {}
  current_line = 1
  current_address = 0
  deck = []

  preprocessLines = []

  def __init__(self, lines):
    self.preprocess(lines)

    self.generateListing()

  def data(self, line):
    tokens = removeComments(line)
    
    if len(tokens) < 2:
      raise ValueError("Expected value.")
    
    for token in tokens[1:]:
      if not isData(token):
        raise ValueError("Unexpected value.")

    for token in tokens[1:]:
      listline = ""
      listline += f"{self.current_address:02}    {token}"
      if self.current_address in self.labels:
        listline+= f"    {self.labels[self.current_address]:<6}  "
      else:
        listline+= " "*12
      listline += "DATA    "
      listline += f"{tokens[1]}"

      self.preprocessLines.append(listline)
      self.current_address += 1
      

  def generateListing(self):
    last = 0
    for line in self.preprocessLines:
      if int(line[0:2]) - last > 1:
        print()
      last = int(line[0:2])

      print(line)

  def label(self, line):
    tokens = removeComments(line)

    labelname = tokens[0].split(':')[0]

    self.labels[self.current_address] = labelname
    
  def org(self, line):
    tokens = removeComments(line)

    if len(tokens) > 2:
      raise ValueError("Too many values.")
    elif not isData(tokens[1]):
      raise ValueError("Unexpected value.")

    self.current_address = int(tokens[1])
  
  def preprocess(self, lines):
    self.preprocessLines = []
    for line in lines:
      self.preprocessLine(line)
      self.current_line += 1

  def preprocessLine(self, line):
    if line.isspace(): return

    token = line.split(maxsplit=1)[0]
    
    if token.startswith(';'): return

    elif ':' in token: self.label(line)
    
    elif token == ".data": self.data(line)
    elif token == ".org": self.org(line)

    elif token == "#define": pass # TODO: Implement define macro.
    elif token == "#include": pass # TODO: Implement include macro.

    elif token in CARDIAC_INSTRUCTIONS:
      self.preprocessInstruction(line)
  

  def preprocessInstruction(self, line):
    tokens = removeComments(line)
    
    if len(tokens) > 2:
      raise ValueError("Too many values.")
    elif not isAddress(tokens[1]) and not isLabel(tokens[1]):
      raise ValueError("Unexpected value.")

    listline = ""

    listline += f"{self.current_address:02}    "
    listline += f"{CARDIAC_INSTRUCTIONS.index(tokens[0])}"
    listline += "xx"

    if self.current_address in self.labels:
      listline+= f"    {self.labels[self.current_address]:<6}  "
    else:
      listline+= " "*12

    listline += f"{tokens[0]}    {tokens[1]} "
    self.preprocessLines.append(listline)

    self.current_address += 1

if __name__ == '__main__':
  import main
  main.main()
