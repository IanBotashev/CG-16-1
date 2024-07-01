44

| Instruction       | Bit pos | Description                                                         |
| ----------------- | ------- | ------------------------------------------------------------------- |
| mmuread           | 0       | Output the currently selected address onto the bus.                 |
| mmuwrite          | 1       | Write onto the currently selected address                           |
| xread             | 2       | Output the contents of the X register onto the bus                  |
| xwrite            | 3       | Write data on the bus onto the X register                           |
| yread             | 4       | Output the contents of the Y register onto the bus                  |
| ywrite            | 5       | Write data on the bus onto the Y register                           |
| zread             | 6       | Output the contents of the Z register onto the bus                  |
| zwrite            | 7       | Write data on the bus onto the Z register                           |
| aread             | 8       | Output the contents of the accumulator onto the bus                 |
| awrite            | 9       | Write data on the bus onto the accumulator                          |
| pcread            | 10      | Output the contents of the program counter onto the bus             |
| pcwrite           | 11      | Write data on the bus onto the program counter                      |
| pcinc             | 12      | Increment the program counter                                       |
| pcclr             | 13      | Clear the program counter                                           |
| pcbsread          | 14      | Output the contents of the program counter bank select onto the bus |
| pcbswrite         | 15      | Write data on the bus onto the program counter bank select          |
| pcbsclr           | 16      | Clear the program counter bank select                               |
| irread            | 17      | Output the contents of the instruction register onto the bus        |
| irwrite           | 18      | Write data on the bus onto the instruction register                 |
| stread            | 19      | Output the contents of the stack top register onto the bus          |
| stwrite           | 20      | Write data on the bus onto the stack top register                   |
| sbread            | 21      | Output the contents of the stack base register onto the bus         |
| sbwrite           | 22      | Write data on the bus onto the stack base register                  |
| bsread            | 23      | Output the contents of the bank select register onto the bus        |
| bswrite           | 24      | Write data on the bus onto the bank select register                 |
| aawrite           | 25      | Write data on the bus onto the address access                       |
| aluop             | 26      | ALU operation to perform                                            |
| aluwriteflags     | 27      | ALU write to flags                                                  |
| carryset          | 28      | Sets the carry flag                                                 |
| carryclear        | 29      | Clears the carry flag                                               |
| zeroset           | 30      | Sets the zero flag                                                  |
| zeroclear         | 31      | Clears the zero flag                                                |
| negativeset       | 32      | Sets the negative flag                                              |
| negativeclear     | 33      | Clears the negative flag                                            |
| morethanset       | 34      | Sets the more than flag                                             |
| morethanclear     | 35      | Clears the more than flag                                           |
| equalset          | 36      | Sets the equal flag                                                 |
| equalclear        | 37      | Clears the equal flag                                               |
| lessthanset       | 38      | Sets the less than flag                                             |
| lessthanclear     | 39      | Clears the less than flag                                           |
| disableinterrupts | 40      | Sets the Interrupt Disable flag                                     |
| enableinterrupts  | 41      | Clears the Interrupt Disable flag                                   |
| ccinc             | 42      | Increment the control counter                                       |
| ccclr             | 43      | Clear the control counter                                           |
