
# Instruction Set
## Design
Each instruction opcode is a byte.
Which leaves 3 bytes for operands.


## Key
`$` - Address
`#` - Literal value

| Instruction | Opcode | Description                                            | Added | Tested |
| ----------- | ------ | ------------------------------------------------------ | ----- | ------ |
| NOP         | 0      | No operation.                                          | Yes   | Yes    |
| LDA `$1`    |        | Load value from `$1` into Accumulator                  | Yes   | Yes    |
| LDA `#1`    |        | Load `#1` into the accumulator                         | Yes   | Yes    |
| LDX `$1`    |        | Load value from `$1` into X register                   | Yes   | Yes    |
| LDX `#1`    |        | Load `#1` into the X register                          | Yes   | Yes    |
| LDY `$1`    |        | Load value from `$1` into Y register                   | Yes   | Yes    |
| LDY `#1`    |        | Load `#1` into the Y register                          | Yes   | Yes    |
| LDZ `$1`    |        | Load value from `$1` into Z register                   | Yes   | Yes    |
| LDZ `#1`    |        | Load `#1` into the Z register                          | Yes   | Yes    |
| LDS `$1`    |        | Load value from `$1` into Stack Top and Base pointers. | Yes   |        |
| LDS `#1`    |        | Load `#1` into Stack Top and Base pointers.            | Yes   |        |

| Instruction | Opcode | Description                                                                                | Added | Tested | Mode      |
| ----------- | ------ | ------------------------------------------------------------------------------------------ | ----- | ------ | --------- |
| NOP         | 0      | No operation.                                                                              |       |        |           |
| LDA `$1`    |        | Load value from `$1` into Accumulator                                                      |       |        | Absolute  |
| LDA `#1`    |        | Load `#1` into the accumulator                                                             |       |        | Immediate |
| LDX `$1`    |        | Load value from `$1` into X register                                                       |       |        | Absolute  |
| LDX `#1`    |        | Load `#1` into the X register                                                              |       |        | Immediate |
| LDY `$1`    |        | Load value from `$1` into Y register                                                       |       |        |           |
| LDZ `$1`    |        | Load value from `$1` into Z register                                                       |       |        |           |
| LDS `$1`    |        | Load value from `$1` into Stack Top and Base pointers.                                     |       |        |           |
| STA `$1`    |        | Load value from Accumulator into `$1`                                                      |       |        |           |
| STX `$1`    |        | Load value from X register into `$1`                                                       |       |        |           |
| STY `$1`    |        | Load value from Y register into `$1`                                                       |       |        |           |
| STZ `$1`    |        | Load value from Z register into `$1`                                                       |       |        |           |
| STI `$1`    |        | Load value from Interrupt Register into `$1`                                               |       |        |           |
| TAX         |        | Transfer value from Accumulator into X                                                     |       |        |           |
| TAY         |        | Transfer value from Accumulator into Y                                                     |       |        |           |
| TAZ         |        | Transfer value from Accumulator into Z                                                     |       |        |           |
| TXA         |        | Transfer value from X into Accumulator                                                     |       |        |           |
| TYA         |        | Transfer value from Y into Accumulator                                                     |       |        |           |
| TZA         |        | Transfer value from Z into Accumulator                                                     |       |        |           |
| TBA         |        | Transfer value from Bank Select Register into Accumulator                                  |       |        |           |
| TTX         |        | Transfer Stack Top Pointer into X                                                          |       |        |           |
| TXT         |        | Transfer X into Stack Top Pointer                                                          |       |        |           |
| TTB         |        | Transfer Stack Base Pointer into X                                                         |       |        |           |
| TBT         |        | Transfer X into Stack Base Pointer                                                         |       |        |           |
| PHA         |        | Push Accumulator onto stack                                                                |       |        |           |
| PHP         |        | Push Processor Flags onto stack                                                            |       |        |           |
| PLA         |        | Pull Accumulator from stack                                                                |       |        |           |
| PLP         |        | Pull processor flags from stack                                                            |       |        |           |
| AND `$1`    |        | Logical AND on the contents of the Accumulator using `$1` result stored in the accumulator |       |        |           |
| OR `$1`     |        | Logical OR on the contents of the Accumulator using `$1`, result stored in the accumulator |       |        |           |
| XOR `$1`    |        | Logical OR on the contents of the Accumulator using `$1`, result stored in the accumulator |       |        |           |
| ADC `$1`    |        | Adds the contents of `$1` and carry bit to the accumulator. `A + $1`                       |       |        |           |
| SBC `$1`    |        | Subtracts the contents of `$1` and carry bit from the accumulator. `A - $1`                |       |        |           |
| UMUL `$1`   |        | Unsigned Multiplies the contents of `$1` with the accumulator `A * $1`                     |       |        |           |
| UDIV `$1`   |        | Unsigned Divides the accumulator by the contents of `$1`  `A / $1`                         |       |        |           |
| MUL `$1`    |        | Signed Multiplies the contents of `$1` with the accumulator `A * $1`                       |       |        |           |
| DIV `$1`    |        | Signed Divides the accumulator by the contents of `$1`  `A / $1`                           |       |        |           |
| INC `$1`    |        | Increments the contents of `$1`                                                            |       |        |           |
| INA         |        | Increments the contents of the accumulator                                                 |       |        |           |
| INX         |        | Increments the contents of the X register                                                  |       |        |           |
| INY         |        | Increments the contents of the Y register                                                  |       |        |           |
| INZ         |        | Increments the contents of the Z register                                                  |       |        |           |
| DEC `$1`    |        | Increments the contents of `$1`                                                            |       |        |           |
| DEA         |        | Decrements the contents of the accumulator                                                 |       |        |           |
| DEX         |        | Decrements the contents of the X register                                                  |       |        |           |
| DEY         |        | Decrements the contents of the Y register                                                  |       |        |           |
| DEZ         |        | Decrements the contents of the Z register                                                  |       |        |           |
| LSL         |        | Logical shift left of the Accumulator by 1 bit.                                            |       |        |           |
| LSR         |        | Logical shift right of the Accumulator by 1 bit.                                           |       |        |           |
| ASL         |        | Arithmetic shift left of the Accumulator by 1 bit.                                         |       |        |           |
| ASR         |        | Arithmetic shift right of the Accumulator by 1 bit.                                        |       |        |           |
| ROL         |        | Rotate left the Accumulator by 1 bit.                                                      |       |        |           |
| ROR         |        | Rotate right the Accumulator by 1 bit.                                                     |       |        |           |
| CMP `$1`    |        | Compare the value of the Accumulator to `$1`.                                              |       |        |           |
| CPX `$1`    |        | Compare the value of the X register to `$1`                                                |       |        |           |
| CPY `$1`    |        | Compare the value of the Y register to `$1`                                                |       |        |           |
| CPZ `$1`    |        | Compare the value of the Z register to `$1`                                                |       |        |           |
| JMP `$1`    |        | Set the program counter to `$1`                                                            |       |        |           |
| JSR `$1`    |        | Jump to subroutine. Push the PBCS then PC onto stack then set the PC to `$1`               |       |        |           |
| RTS         |        | Return from subroutine. Pull PC then PCBS value from top of stack.                         |       |        |           |
| BCC `$1`    |        | Branch to `$1` if the carry flag is 0                                                      |       |        |           |
| BCS `$1`    |        | Branch to `$1` if the carry flag is 1                                                      |       |        |           |
| BNE `$1`    |        | Branch to `$1` if the equal flag is 0                                                      |       |        |           |
| BEQ `$1`    |        | Branch to `$1` if the equal flag is 1                                                      |       |        |           |
| BLT `$1`    |        | Branch to `$1` if the less than flag is 1                                                  |       |        |           |
| BMT `$1`    |        | Branch to `$1` if the more than flag is 1                                                  |       |        |           |
| BMI `$1`    |        | Branch to `$1` if the negative flag is 1                                                   |       |        |           |
| BPL `$1`    |        | Branch to `$1` if the negative flag is 0                                                   |       |        |           |
| CLC         |        | Clear carry flag                                                                           |       |        |           |
| SEC         |        | Set carry flag                                                                             |       |        |           |
| CID         |        | Clear interrupt disable                                                                    |       |        |           |
| SID         |        | Set interrupt disable                                                                      |       |        |           |
| CPS         |        | Clear Page Select                                                                          |       |        |           |
| SPS         |        | Set Page Select                                                                            |       |        |           |
| CIN         |        | Clear Interrupt                                                                            |       |        |           |
| HLT         |        | Halt the processor                                                                         |       |        |           |
| INT `#1`    |        | Raises a kernel interrupt of value `#1`                                                    |       |        |           |

