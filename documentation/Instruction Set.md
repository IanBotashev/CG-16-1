
# Instruction Set
## Design
Each instruction opcode is a byte.


## Key
`$` - Address
`#` - Literal value

| Instruction | Opcode | Description                                                                                | Added   | Tested  |
| ----------- | ------ | ------------------------------------------------------------------------------------------ | ------- | ------- |
| NOP         |        | No operation.                                                                              | ==Yes== | ==Yes== |
| LDA `$1`    |        | Load value from `$1` into Accumulator                                                      | ==Yes== | ==Yes== |
| LDA `#1`    |        | Load `#1` into the accumulator                                                             |         |         |
| LDX `$1`    |        | Load value from `$1` into X register                                                       | ==Yes== |         |
| LDY `$1`    |        | Load value from `$1` into Y register                                                       | ==Yes== |         |
| LDZ `$1`    |        | Load value from `$1` into Z register                                                       | ==Yes== |         |
| LDS `$1`    |        | Load value from `$1` into Stack Top and Base pointers.                                     | ==Yes== |         |
| STA `$1`    |        | Load value from Accumulator into `$1`                                                      | ==Yes== |         |
| STX `$1`    |        | Load value from X register into `$1`                                                       | ==Yes== |         |
| STY `$1`    |        | Load value from Y register into `$1`                                                       | ==Yes== |         |
| STZ `$1`    |        | Load value from Z register into `$1`                                                       | ==Yes== |         |
| STI `$1`    |        | Load value from Interrupt Register into `$1`                                               | ==Yes== |         |
| TAX         |        | Transfer value from Accumulator into X                                                     | ==Yes== |         |
| TAY         |        | Transfer value from Accumulator into Y                                                     | ==Yes== |         |
| TAZ         |        | Transfer value from Accumulator into Z                                                     | ==Yes== |         |
| TXA         |        | Transfer value from X into Accumulator                                                     | ==Yes== |         |
| TYA         |        | Transfer value from Y into Accumulator                                                     | ==Yes== |         |
| TZA         |        | Transfer value from Z into Accumulator                                                     | ==Yes== |         |
| TBA         |        | Transfer value from Bank Select Register into Accumulator                                  | ==Yes== |         |
| TTX         |        | Transfer Stack Top Pointer into X                                                          | ==Yes== |         |
| TXT         |        | Transfer X into Stack Top Pointer                                                          | ==Yes== |         |
| TTB         |        | Transfer Stack Base Pointer into X                                                         | ==Yes== |         |
| TBT         |        | Transfer X into Stack Base Pointer                                                         | ==Yes== |         |
| PHA         |        | Push Accumulator onto stack                                                                | ==Yes== |         |
| PHP         |        | Push Processor Flags onto stack                                                            | ==Yes== |         |
| PLA         |        | Pull Accumulator from stack                                                                | ==Yes== |         |
| PLP         |        | Pull processor flags from stack                                                            | ==Yes== |         |
| AND `$1`    |        | Logical AND on the contents of the Accumulator using `$1` result stored in the accumulator | ==Yes== |         |
| OR `$1`     |        | Logical OR on the contents of the Accumulator using `$1`, result stored in the accumulator | ==Yes== |         |
| XOR `$1`    |        | Logical OR on the contents of the Accumulator using `$1`, result stored in the accumulator | ==Yes== |         |
| ADC `$1`    |        | Adds the contents of `$1` and carry bit to the accumulator. `A + $1`                       | ==Yes== |         |
| SBC `$1`    |        | Subtracts the contents of `$1` and carry bit from the accumulator. `A - $1`                | ==Yes== |         |
| UMUL `$1`   |        | Unsigned Multiplies the contents of `$1` with the accumulator `A * $1`                     | ==Yes== |         |
| UDIV `$1`   |        | Unsigned Divides the accumulator by the contents of `$1`  `A / $1`                         | ==Yes== |         |
| MUL `$1`    |        | Signed Multiplies the contents of `$1` with the accumulator `A * $1`                       | ==Yes== |         |
| DIV `$1`    |        | Signed Divides the accumulator by the contents of `$1`  `A / $1`                           | ==Yes== |         |
| INC `$1`    |        | Increments the contents of `$1`                                                            | ==Yes== |         |
| INA         |        | Increments the contents of the accumulator                                                 | ==Yes== |         |
| INX         |        | Increments the contents of the X register                                                  | ==Yes== |         |
| INY         |        | Increments the contents of the Y register                                                  | ==Yes== |         |
| INZ         |        | Increments the contents of the Z register                                                  | ==Yes== |         |
| DEC `$1`    |        | Increments the contents of `$1`                                                            | ==Yes== |         |
| DEA         |        | Decrements the contents of the accumulator                                                 | ==Yes== |         |
| DEX         |        | Decrements the contents of the X register                                                  | ==Yes== |         |
| DEY         |        | Decrements the contents of the Y register                                                  | ==Yes== |         |
| DEZ         |        | Decrements the contents of the Z register                                                  | ==Yes== |         |
| LSL         |        | Logical shift left of the Accumulator by 1 bit.                                            | ==Yes== |         |
| LSR         |        | Logical shift right of the Accumulator by 1 bit.                                           | ==Yes== |         |
| ASL         |        | Arithmetic shift left of the Accumulator by 1 bit.                                         | ==Yes== |         |
| ASR         |        | Arithmetic shift right of the Accumulator by 1 bit.                                        | ==Yes== |         |
| ROL         |        | Rotate left the Accumulator by 1 bit.                                                      | ==Yes== |         |
| ROR         |        | Rotate right the Accumulator by 1 bit.                                                     | ==Yes== |         |
| CMP `$1`    |        | Compare the value of the Accumulator to `$1`.                                              | ==Yes== |         |
| CPX `$1`    |        | Compare the value of the X register to `$1`                                                | ==Yes== |         |
| CPY `$1`    |        | Compare the value of the Y register to `$1`                                                | ==Yes== |         |
| CPZ `$1`    |        | Compare the value of the Z register to `$1`                                                | ==Yes== |         |
| JMP `$1`    |        | Set the program counter to `$1`                                                            | ==Yes== |         |
| JSR `$1`    |        | Jump to subroutine. Push the PBCS then PC onto stack then set the PC to `$1`               | ==Yes== |         |
| RTS         |        | Return from subroutine. Pull PC then PCBS value from top of stack.                         | ==Yes== |         |
| BCC `$1`    |        | Branch to `$1` if the carry flag is 0                                                      | ==Yes== |         |
| BCS `$1`    |        | Branch to `$1` if the carry flag is 1                                                      | ==Yes== |         |
| BNE `$1`    |        | Branch to `$1` if the equal flag is 0                                                      | ==Yes== |         |
| BEQ `$1`    |        | Branch to `$1` if the equal flag is 1                                                      | ==Yes== |         |
| BLT `$1`    |        | Branch to `$1` if the less than flag is 1                                                  | ==Yes== |         |
| BMT `$1`    |        | Branch to `$1` if the more than flag is 1                                                  | ==Yes== |         |
| BMI `$1`    |        | Branch to `$1` if the negative flag is 1                                                   | ==Yes== |         |
| BPL `$1`    |        | Branch to `$1` if the negative flag is 0                                                   | ==Yes== |         |
| CLC         |        | Clear carry flag                                                                           | ==Yes== |         |
| SEC         |        | Set carry flag                                                                             | ==Yes== |         |
| CID         |        | Clear interrupt disable                                                                    | ==Yes== |         |
| SID         |        | Set interrupt disable                                                                      | ==Yes== |         |
| CPS         |        | Clear Page Select                                                                          | ==Yes== |         |
| SPS         |        | Set Page Select                                                                            | ==Yes== |         |
| CIN         |        | Clear Interrupt                                                                            |         |         |
| HLT         |        | Halt the processor                                                                         | ==Yes== |         |
| INT `#1`    |        | Raises a kernel interrupt of value `#1`                                                    |         |         |
| RTI         |        | Return from interrupt                                                                      |         |         |

