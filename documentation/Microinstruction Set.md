# Microinstruction  Set

| Instruction         | Bit pos | Description                                                                                                                                                 |
| ------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mmuread             | `0`     | Output the currently selected address onto the bus.                                                                                                         |
| mmuwrite            | `1`     | Write onto the currently selected address                                                                                                                   |
| xread               | `2`     | Output the contents of the X register onto the bus                                                                                                          |
| xwrite              | `3`     | Write data on the bus onto the X register                                                                                                                   |
| yread               | `4`     | Output the contents of the Y register onto the bus                                                                                                          |
| ywrite              | `5`     | Write data on the bus onto the Y register                                                                                                                   |
| zread               | `6`     | Output the contents of the Z register onto the bus                                                                                                          |
| zwrite              | `7`     | Write data on the bus onto the Z register                                                                                                                   |
| aread               | `8`     | Output the contents of the accumulator onto the bus                                                                                                         |
| awrite              | `9`     | Write data on the bus onto the accumulator                                                                                                                  |
| pcread              | `10`    | Output the contents of the program counter onto the bus                                                                                                     |
| pcwrite             | `11`    | Write data on the bus onto the program counter                                                                                                              |
| pcinc               | `12`    | Increment the program counter                                                                                                                               |
| pcclr               | `13`    | Clear the program counter                                                                                                                                   |
| pcbsread            | `14`    | Output the contents of the program counter bank select onto the bus                                                                                         |
| pcbswrite           | `15`    | Write data on the bus onto the program counter bank select                                                                                                  |
| pcbsclr             | `16`    | Clear the program counter bank select                                                                                                                       |
| irread              | `17`    | Output the contents of the instruction register onto the bus                                                                                                |
| irwrite             | `18`    | Write data on the bus onto the instruction register                                                                                                         |
| stread              | `19`    | Output the contents of the stack top register onto the bus                                                                                                  |
| stwrite             | `20`    | Write data on the bus onto the stack top register                                                                                                           |
| sbread              | `21`    | Output the contents of the stack base register onto the bus                                                                                                 |
| sbwrite             | `22`    | Write data on the bus onto the stack base register                                                                                                          |
| bsread              | `23`    | Output the contents of the bank select register onto the bus                                                                                                |
| bswrite             | `24`    | Write data on the bus onto the bank select register                                                                                                         |
| aawrite             | `25`    | Write data on the bus onto the address access                                                                                                               |
| aluop               | `26-30` | ALU operation to perform                                                                                                                                    |
| aluwriteflags       | `31`    | ALU write to flags                                                                                                                                          |
| carryset            | `32`    | Sets the carry flag                                                                                                                                         |
| carryclear          | `33`    | Clears the carry flag                                                                                                                                       |
| zeroset             | `34`    | Sets the zero flag                                                                                                                                          |
| zeroclear           | `35`    | Clears the zero flag                                                                                                                                        |
| negativeset         | `36`    | Sets the negative flag                                                                                                                                      |
| negativeclear       | `37`    | Clears the negative flag                                                                                                                                    |
| morethanset         | `38`    | Sets the more than flag                                                                                                                                     |
| morethanclear       | `39`    | Clears the more than flag                                                                                                                                   |
| equalset            | `40`    | Sets the equal flag                                                                                                                                         |
| equalclear          | `41`    | Clears the equal flag                                                                                                                                       |
| lessthanset         | `42`    | Sets the less than flag                                                                                                                                     |
| lessthanclear       | `43`    | Clears the less than flag                                                                                                                                   |
| disableinterrupts   | `44`    | Sets the Interrupt Disable flag                                                                                                                             |
| enableinterrupts    | `45`    | Clears the Interrupt Disable flag                                                                                                                           |
| ccclr               | `46`    | Clear the control counter                                                                                                                                   |
| flagsread           | `47`    | Output flags onto the bus                                                                                                                                   |
| flagswrite          | `48`    | Write flags from the bus.                                                                                                                                   |
| readinstructionlow  | `49`    | Puts the first byte of our current instruction onto the bus                                                                                                 |
| readinstructionhigh | `50`    | Puts the last byte of our current instruction onto the bus                                                                                                  |
| stinc               | `51`    | Increments the stack top pointer                                                                                                                            |
| stdec               | `52`    | Decrements the stack top pointer                                                                                                                            |
| stclr               | `53`    | Clears the stack top pointer                                                                                                                                |
| aluread             | `54`    | Outputs to accumulator, replacing the bus in input to accumulator                                                                                           |
| aluselectxhigh      | `55`    | Selects the 2 high bytes of the ALU output                                                                                                                  |
| condjump            | `56-58` | 3-bit selector value for jumping. Select a flag, and if it's `condjumpdesired`, sets program counter write. Value of 0 doesn't actually equate to any flag. |
| condjumpdesired     | `59`    |                                                                                                                                                             |
| haltclock           | `60`    | Halts the clock                                                                                                                                             |
| pageset             | `61`    | Sets our page to 1 in the graphical ram                                                                                                                     |
| pageclear           | `62`    | Sets our page to 0 in the graphical ram                                                                                                                     |



