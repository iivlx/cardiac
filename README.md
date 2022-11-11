# cardiac

**CARD**board **I**llustrative **A**id to **C**omputation

See https://www.cs.drexel.edu/~bls96/museum/cardiac.html for more information.

---
## pycard assembler

The **pycard assembler** is an assembler for cardiac assembly files.

It will assemble the source file into a `.deck` file.

### syntax

**Assembler Instructions:**

| Instruction | Description                                     |
| ----------- | ----------------------------------------------- |
| #include    | Include another file                            |
| #define     | Define                                          |
| .data       | Specify the remainder of the line contains data |
| .org        | Specify memory address for next instruction     |

**Labels:**

A **label** can be created by specifying a labelname on a newline followed by a colon.

A **label** can be on its own line or can be followed by an instruction.

```
example:
  JMP 300

with_instruction: JMP 30
```

**Comments:**

**Comments** can be created with a semicolon. Anything on the remainder of the line will be ignored by the assmbler.

```
CLA 40 ; Load memory cell 40 into the accumulator.
```

**Cardiac Instructions:**

| Instruction | Opcode | Description                                  |
| ----------- | ------ | -------------------------------------------- |
|	INP         | 0      | Read a card into memory                      |
|	CLA         | 1      | Clear accumulator and add from memory (load) |
|	ADD         | 2      | Add from memory to accumulator               |
|	TAC         | 3      | Test accumulator and jump if negative        |
|	SFT         | 4      | Shift accumulator                            |
|	OUT         | 5      | Write memory location to output card         |
|	STO         | 6      | Store accumulator to memory                  | 
|	SUB         | 7      | Subtract memory from accumulator             |
|	JMP         | 8      | Jump and save PC                             |
|	HRS         | 9      | Halt and reset                               | 
