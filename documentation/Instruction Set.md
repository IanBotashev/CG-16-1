# Instruction Set
## Design
Each instruction opcode is a byte.


## Key
`$` - Address

| Instruction | Opcode | Description                                                                                | Added   |
| ----------- | ------ | ------------------------------------------------------------------------------------------ | ------- |
| NOP         | 0      | No operation.                                                                              | ==Yes== |
| LDA `$1`    | 1      | Load value from `$1` into Accumulator                                                      | ==Yes== |
| LDX `$1`    | 2      | Load value from `$1` into X register                                                       | ==Yes== |
| LDY `$1`    | 3      | Load value from `$1` into Y register                                                       | ==Yes== |
| LDZ `$1`    | 4      | Load value from `$1` into Z register                                                       | ==Yes== |
| LDS `$1`    | 5      | Load value from `$1` into Stack Top and Base pointers.                                     | ==Yes== |
| STA `$1`    | 6      | Load value from Accumulator into `$1`                                                      | ==Yes== |
| STX `$1`    | 7      | Load value from X register into `$1`                                                       | ==Yes== |
| STY `$1`    | 8      | Load value from Y register into `$1`                                                       | ==Yes== |
| STZ `$1`    | 9      | Load value from Z register into `$1`                                                       | ==Yes== |
| TAX         | 10     | Transfer value from Accumulator into X                                                     | ==Yes== |
| TAY         | 11     | Transfer value from Accumulator into Y                                                     | ==Yes== |
| TAZ         | 12     | Transfer value from Accumulator into Z                                                     | ==Yes== |
| TXA         | 13     | Transfer value from X into Accumulator                                                     | ==Yes== |
| TYA         | 14     | Transfer value from Y into Accumulator                                                     | ==Yes== |
| TZA         | 15     | Transfer value from Z into Accumulator                                                     | ==Yes== |
| TBA         | 16     | Transfer value from Bank Select Register into Accumulator                                  | ==Yes== |
| TTX         | 17     | Transfer Stack Top Pointer into X                                                          | ==Yes== |
| TXT         | 18     | Transfer X into Stack Top Pointer                                                          | ==Yes== |
| TTB         | 19     | Transfer Stack Base Pointer into X                                                         | ==Yes== |
| TBT         | 20     | Transfer X into Stack Base Pointer                                                         | ==Yes== |
| PHA         | 21     | Push Accumulator onto stack                                                                | ==Yes== |
| PHP         | 22     | Push Processor Flags onto stack                                                            | ==Yes== |
| PLA         | 23     | Pull Accumulator from stack                                                                | ==Yes== |
| PLP         | 24     | Pull processor flags from stack                                                            | ==Yes== |
| AND `$1`    | 25     | Logical AND on the contents of the Accumulator using `$1` result stored in the accumulator | ==Yes== |
| OR `$1`     | 26     | Logical OR on the contents of the Accumulator using `$1`, result stored in the accumulator | ==Yes== |
| XOR `$1`    | 27     | Logical OR on the contents of the Accumulator using `$1`, result stored in the accumulator | ==Yes== |
| ADC `$1`    | 28     | Adds the contents of `$1` and carry bit to the accumulator. `A + $1`                       | ==Yes== |
| SBC `$1`    | 29     | Subtracts the contents of `$1` and carry bit from the accumulator. `A - $1`                | ==Yes== |
| UMUL `$1`   | 30     | Unsigned Multiplies the contents of `$1` with the accumulator `A * $1`                     | ==Yes== |
| UDIV `$1`   | 31     | Unsigned Divides the accumulator by the contents of `$1`  `A / $1`                         | ==Yes== |
| MUL `$1`    | 32     | Signed Multiplies the contents of `$1` with the accumulator `A * $1`                       | ==Yes== |
| DIV `$1`    | 33     | Signed Divides the accumulator by the contents of `$1`  `A / $1`                           | ==Yes== |
| INC `$1`    | 34     | Increments the contents of `$1`                                                            | ==Yes== |
| INA         | 35     | Increments the contents of the accumulator                                                 | ==Yes== |
| INX         | 36     | Increments the contents of the X register                                                  | ==Yes== |
| INY         | 37     | Increments the contents of the Y register                                                  | ==Yes== |
| INZ         | 38     | Increments the contents of the Z register                                                  | ==Yes== |
| DEC `$1`    | 39     | Increments the contents of `$1`                                                            | ==Yes== |
| DEA         | 40     | Decrements the contents of the accumulator                                                 | ==Yes== |
| DEX         | 41     | Decrements the contents of the X register                                                  | ==Yes== |
| DEY         | 42     | Decrements the contents of the Y register                                                  | ==Yes== |
| DEZ         | 43     | Decrements the contents of the Z register                                                  | ==Yes== |
| LSL         | 44     | Logical shift left of the Accumulator by 1 bit.                                            | ==Yes== |
| LSR         | 45     | Logical shift right of the Accumulator by 1 bit.                                           | ==Yes== |
| ASL         | 46     | Arithmetic shift left of the Accumulator by 1 bit.                                         | ==Yes== |
| ASR         | 47     | Arithmetic shift right of the Accumulator by 1 bit.                                        | ==Yes== |
| ROL         | 48     | Rotate left the Accumulator by 1 bit.                                                      | ==Yes== |
| ROR         | 49     | Rotate right the Accumulator by 1 bit.                                                     | ==Yes== |
| CMP `$1`    | 50     | Compare the value of the Accumulator to `$1`.                                              | ==Yes== |
| CPX `$1`    | 51     | Compare the value of the X register to `$1`                                                | ==Yes== |
| CPY `$1`    | 52     | Compare the value of the Y register to `$1`                                                | ==Yes== |
| CPZ `$1`    | 53     | Compare the value of the Z register to `$1`                                                | ==Yes== |
| JMP `$1`    | 54     | Set the program counter to `$1`                                                            | ==Yes== |
| JSR `$1`    | 55     | Jump to subroutine. Push the PBCS then PC onto stack then set the PC to `$1`               | ==Yes== |
| RTS         | 56     | Return from subroutine. Pull PC then PCBS value from top of stack.                         | ==Yes== |
| BCC `$1`    | 57     | Branch to `$1` if the carry flag is 0                                                      | ==Yes== |
| BCS `$1`    | 58     | Branch to `$1` if the carry flag is 1                                                      | ==Yes== |
| BNE `$1`    | 59     | Branch to `$1` if the equal flag is 0                                                      | ==Yes== |
| BEQ `$1`    | 60     | Branch to `$1` if the equal flag is 1                                                      | ==Yes== |
| BLT `$1`    | 61     | Branch to `$1` if the less than flag is 1                                                  | ==Yes== |
| BMT `$1`    | 62     | Branch to `$1` if the more than flag is 1                                                  | ==Yes== |
| BMI `$1`    | 63     | Branch to `$1` if the negative flag is 1                                                   | ==Yes== |
| BPL `$1`    | 64     | Branch to `$1` if the negative flag is 0                                                   | ==Yes== |
| BIZ `$1`    | 65     | Branch to `$1` if the zero flag is 1                                                       | ==Yes== |
| BNT `$1`    | 66     | Branch to `$1` if the zero flag is 0                                                       | ==Yes== |
| CLC         | 67     | Clear carry flag                                                                           | ==Yes== |
| SEC         | 68     | Set carry flag                                                                             | ==Yes== |
| CLI         | 69     | Clear interrupt disable                                                                    | ==Yes== |
| SEI         | 70     | Set interrupt disable                                                                      | ==Yes== |
| CPS         | 71     | Clear Page Select                                                                          | ==Yes== |
| SPS         | 72     | Set Page Select                                                                            | ==Yes== |
| HLT         | 73     | Halt the processor                                                                         | ==Yes== |
| SYSCALL     |        | Raises a kernel interrupt                                                                  |         |
| RTI         |        | Return from interrupt                                                                      |         |
|             |        |                                                                                            |         |
|             |        |                                                                                            |         |

