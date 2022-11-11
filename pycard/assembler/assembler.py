#!/usr/bin/env python3

CARDIAC_INSTRUCTIONS = ["INP", "CLA", "ADD", "TAC", "SFT", "OUT", "STO", "SUB", "JMP", "HRS"]

def isAddress(data): return isData(data, 2)

def isData(data, datalength=3):
  return data.isnumeric() and len(data) == datalength
  
def isLabel(data): return data.isalnum()

def createIVD(dd):
  return {v: k for k, v in dd.items()}

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

  def encodeInstruction(self, opcode, address):
      op = str(CARDIAC_INSTRUCTIONS.index(opcode)) if opcode is not "DATA" else ""
      add = f"{self.labels[address]:02}" if address in self.labels else address
      return op, add

  def generateDeck(self):
    for line in self.preprocessLines:
      pass

  def generateListing(self):
    last = -1
    for line in self.preprocessLines:
      # separate discontiguous memory blocks with a blank line
      if line[0] - last > 1 and last > 0: print()
      last = line[0]

      self.generateListLine(line[0], line[1], line[2])

  def generateListLine(self, memory, mnemonic, target):
      opcode, address = self.encodeInstruction(mnemonic, target)
      print(
        f"""{memory:2}    """
        f"""{opcode + address if opcode is not "" else target}    """
        f"""{self.getLabel(memory):<8}  """
        f"""{mnemonic + " " if mnemonic is not "DATA" else mnemonic}   """
        f"""{target:<10}""",
        end=''
      )

      # display comments
      if memory in self.comments and len(self.comments[memory]) > 0:
        commentlist = self.comments[memory]
        print(commentlist[0], end='')
        for comment in commentlist[1:]:
          print(" "*40+comment, end='')
      else:
        print()
    
  def getLabel(self, memory):
      labels_ivd = createIVD(self.labels)
      return "" if memory not in labels_ivd else labels_ivd[memory]

  def label(self, line):
    tokens = self.removeComments(line)

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
    tokens = self.removeComments(line)
    
    if len(tokens) > 2:
      raise ValueError("Too many values.")
    elif not isAddress(tokens[1]) and not isLabel(tokens[1]):
      raise ValueError("Unexpected value.")

    self.preprocessLines.append([ self.current_address, tokens[0], tokens[1] ])
    self.current_address += 1
  
  def removeComments(self, line):
    if self.current_address not in self.comments: self.comments[self.current_address] = list()

    if ';' in line:
      self.comments[self.current_address].append(';'+line.split(';',maxsplit=1)[1])

    return removeComments(line)

if __name__ == '__main__':
  import main
  main.main()
