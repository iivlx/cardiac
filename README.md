# cardiac

**CARD**board **I**llustrative **A**id to **C**omputation

See https://www.cs.drexel.edu/~bls96/museum/cardiac.html for more information.

---
## pycard assembler

The **pycard assembler** is an assembler for cardiac assembly files.

It will assemble the source file into a `.deck` file.

### syntax

**Assembler Instructions:**

| Instruction | Description                                  |
| ----------- | -------------------------------------------- |
| #include    | Include another file                         |
| #define     | Define                                       |
| .org        | Specify memory address for next instruction  |

**Labels:**

A **label** can be created by specifying a labelname on a newline followed by a colon.

A **label** can be on its own line or can be followed by an instruction.

```
example:
  JMP 300

with_instruction: JMP 300
```

**Comments:**

**Comments** can be created with a semicolon. Anything on the remainder of the line will be ignored by the assmbler.

```
CLA 400 ; Load card 400 into the accumulator.
```

**Cardiac Instructions:**

| Instruction | Description                                  |
| ----------- | -------------------------------------------- |
|	INP         | Read a card into memory                      |
|	CLA         | Clear accumulator and add from memory (load) |
|	ADD         | Add from memory to accumulator               |
|	TAC         | Test accumulator and jump if negative        |
|	SFT         | Shift accumulator                            |
|	OUT         | Write memory location to output card         |
|	STO         | Store accumulator to memory                  | 
|	SUB         | Subtract memory from accumulator             |
|	JMP         | Jump and save PC                             |
|	HRS         | Halt and reset                               | 
