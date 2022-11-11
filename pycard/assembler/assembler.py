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
    tokens = self.removeComments(line)
    
    if len(tokens) < 2:
      raise ValueError("Expected value.")
    
    for token in tokens[1:]:
      if not isData(token):
        raise ValueError("Unexpected value.")

    for token in tokens[1:]:
      self.preprocessLines.append([ self.current_address, "DATA", tokens[1] ])
      self.current_address += 1

  def generateListing(self):
    last = -1
    for line in self.preprocessLines:
      memory = line[0]

      address = line[2]
      if line[2] in self.labels:
        address = f"{self.labels[line[2]]:02}"

      labels_ivd = {v: k for k, v in self.labels.items()}
      label = "" if memory not in labels_ivd else labels_ivd[memory]

      if line[0] - last > 1 and last > 0: print() # separate discontiguous memory blocks with a blank line
      last = line[0]

      instruction = line[1]
      location = line[2]

      print(
        f"""{memory:2}    """
        f"""{str(CARDIAC_INSTRUCTIONS.index(line[1])) + address if line[1] is not "DATA" else location}    """
        f"""{label:<8}  """
        f"""{instruction}    """
        f"""{location}"""
      )

  def label(self, line):
    tokens = removeComments(line)

    labelname = tokens[0].split(':')[0]

    self.labels[labelname] = self.current_address
    
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
    
    if token.startswith(';'): self.removeComments(line)
    elif token.endswith(':'): self.label(line)
    
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

    self.preprocessLines.append([ self.current_address, tokens[0], tokens[1] ])
    self.current_address += 1
  
  def removeComments(self, line):
    if not self.current_address in self.comments: self.comments[self.current_address] = []

    if ';' in line:
      self.comments[self.current_address].append(line.split(';',maxsplit=1)[1])

    return removeComments(line)

if __name__ == '__main__':
  import main
  main.main()
