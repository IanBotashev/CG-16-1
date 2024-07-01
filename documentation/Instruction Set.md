## Design
Each instruction opcode is a byte.


## Key
`$` - Address

| Instruction | Opcode | Description                                                                                                          |
| ----------- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| NOP         | 0      | No operation.                                                                                                        |
| LDA `$1`    | 1      | Load value from `$1` into Accumulator                                                                                |
| LDX `$1`    | 2      | Load value from `$1` into X register                                                                                 |
| LDY `$1`    | 3      | Load value from `$1` into Y register                                                                                 |
| LDZ `$1`    | 4      | Load value from `$1` into Z register                                                                                 |
| LDB `$1`    | 5      | Load value from `$1` into Bank Select Register                                                                       |
| STA `$1`    | 6      | Load value from Accumulator into `$1`                                                                                |
| STX `$1`    | 7      | Load value from X register into `$1`                                                                                 |
| STY `$1`    | 8      | Load value from Y register into `$1`                                                                                 |
| STZ `$1`    | 9      | Load value from Z register into `$1`                                                                                 |
| STB `$1`    | 10     | Load value from Bank Select register into `$1`                                                                       |
| TAX         | 11     | Transfer value from Accumulator into X                                                                               |
| TAY         | 12     | Transfer value from Accumulator into Y                                                                               |
| TAZ         | 13     | Transfer value from Accumulator into Z                                                                               |
| TAB         | 14     | Transfer value from Accumulator into Bank Select Register                                                            |
| TXA         | 15     | Transfer value from X into Accumulator                                                                               |
| TYA         | 16     | Transfer value from Y into Accumulator                                                                               |
| TZA         | 17     | Transfer value from Z into Accumulator                                                                               |
| TBA         | 18     | Transfer value from Bank Select Register into Accumulator                                                            |
| TSX         | 19     | Transfer Stack Pointer into X                                                                                        |
| TXS         | 20     | Transfer X into Stack Pointer                                                                                        |
| PHA         | 21     | Push Accumulator onto stack                                                                                          |
| PHP         | 22     | Push Processor Flags onto stack                                                                                      |
| PLA         | 23     | Pull Accumulator from stack                                                                                          |
| PLP         | 24     | Pull processor flags from stack                                                                                      |
| AND `$1`    | 25     | Logical AND on the contents of the Accumulator using `$1` result stored in the accumulator                           |
| OR          | 26     | Logical OR on the contents of the Accumulator using `$1`, result stored in the accumulator                           |
| XOR         | 27     | Logical OR on the contents of the Accumulator using `$1`, result stored in the accumulator                           |
| ADC `$1`    | 28     | Adds the contents of `$1` and carry bit to the accumulator. `A + $1`                                                 |
| SBC `$1`    | 29     | Subtracts the contents of `$1` and carry bit from the accumulator. `A - $1`                                          |
| UMUL `$1`   | 30     | Unsigned Multiplies the contents of `$1` with the accumulator `A * $1`                                               |
| UDIV `$1`   | 31     | Unsigned Divides the accumulator by the contents of `$1`  `A / $1`                                                   |
| MUL `$1`    | 32     | Signed Multiplies the contents of `$1` with the accumulator `A * $1`                                                 |
| DIV `$1`    | 33     | Signed Divides the accumulator by the contents of `$1`  `A / $1`                                                     |
| INC `$1`    | 34     | Increments the contents of `$1`                                                                                      |
| INA         | 35     | Increments the contents of the accumulator                                                                           |
| INX         | 36     | Increments the contents of the X register                                                                            |
| INY         | 37     | Increments the contents of the Y register                                                                            |
| INZ         | 38     | Increments the contents of the Z register                                                                            |
| DEC `$1`    | 39     | Increments the contents of `$1`                                                                                      |
| DEA         | 40     | Decrements the contents of the accumulator                                                                           |
| DEX         | 41     | Decrements the contents of the X register                                                                            |
| DEY         | 42     | Decrements the contents of the Y register                                                                            |
| DEZ         | 43     | Decrements the contents of the Z register                                                                            |
| LSL         | 44     | Logical shift left of the Accumulator by 1 bit.                                                                      |
| LSR         | 45     | Logical shift right of the Accumulator by 1 bit.                                                                     |
| ASL         | 46     | Arithmetic shift left of the Accumulator by 1 bit.                                                                   |
| ASR         | 47     | Arithmetic shift right of the Accumulator by 1 bit.                                                                  |
| ROL         | 48     | Rotate left the Accumulator by 1 bit.                                                                                |
| ROR         | 49     | Rotate right the Accumulator by 1 bit.                                                                               |
| CMP `$1`    | 50     | Compare the value of the Accumulator to `$1`. Zero flag = `A > $1`, Negative flag = `A == $1`, Carry flag = `A < $1` |
| CPX `$1`    | 51     | Compare the value of the X register to `$1`                                                                          |
| CPY `$1`    | 52     | Compare the value of the Y register to `$1`                                                                          |
| CPZ `$1`    | 53     | Compare the value of the Z register to `$1`                                                                          |
| JMP `$1`    | 54     | Set the program counter to `$1`                                                                                      |
| JSR `$1`    | 55     | Push the program counter value & processor status onto the stack, then set the PC to `$1`                            |
| RTS         | 56     | Pull a value from the stack and set it as the program counter.                                                       |
| BCC `$1`    | 57     | Branch to `$1` if the carry flag is 0                                                                                |
| BCS `$1`    | 58     | Branch to `$1` if the carry flag is 1                                                                                |
| BNE `$1`    | 59     | Branch to `$1` if the equal flag is 0                                                                                |
| BEQ `$1`    | 60     | Branch to `$1` if the equal flag is 1                                                                                |
| BLT `$1`    | 61     | Branch to `$1` if the less than flag is 1                                                                            |
| BMT `$1`    | 62     | Branch to `$1` if the more than flag is 1                                                                            |
| BMI `$1`    | 63     | Branch to `$1` if the negative flag is 1                                                                             |
| BPL `$1`    | 64     | Branch to `$1` if the negative flag is 0                                                                             |
| CLC         | 65     | Clear carry flag                                                                                                     |
| SEC         | 66     | Set carry flag                                                                                                       |
| CLI         | 67     | Clear interrupt disable                                                                                              |
| SEI         | 68     | Set interrupt disable                                                                                                |
| RTI         | 69     | Return from interrupt                                                                                                |
| CPS         | 70     | Clear Page Select                                                                                                    |
| SPS         | 71     | Set Page Select                                                                                                      |
| HLT         | 72     | Halt the processor                                                                                                   |
| SYSCALL     | 73     | Raises a kernel interrupt                                                                                            |

