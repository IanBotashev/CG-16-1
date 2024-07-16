# Instruction Set
## Design
Each instruction opcode is a byte.  
Which leaves 3 bytes for operands.  
## Key
`$` - Address  
`#` - Literal value  

|opcode|usage|desc|tested|
| --- | --- | --- | --- |
|0|NOP|No operation|True|
|1|LDA `#1`|Load `#1` into the accumulator|False|
|2|LDA `$1`|Load value from `$1` into the accumulator|False|
|3|LDX `#1`|Load `#1` into the X register|False|
|4|LDX `$1`|Load value from `$1` into the X register|False|
|5|LDY `#1`|Load `#1` into the Y register|False|
|6|LDY `$1`|Load value from `$1` into the Y register|False|
|7|LDZ `#1`|Load `#1` into the Z register|False|
|8|LDZ `$1`|Load value from `$1` into the Z register|False|
|9|LDS `#1`|Load `#1` into the stack top and base registers|False|
|10|LDS `$1`|Load value from `$1` into the stack top and base registers|False|
|11|STA `$1`|Load value from Accumulator into `$1`|False|
|12|STA `$1`, X|Load value from an address, using `$1` as the bank select and value in X register as address into accumulator|False|
|13|STA `$1`, Y|Load value from an address, using `$1` as the bank select and value in Y register as address into accumulator|False|
|14|STA `$1`, Z|Load value from an address, using `$1` as the bank select and value in Z register as address into accumulator|False|
|15|STX `$1`|Load value from X register into `$1`|False|
|16|STX `$1`, Y|Load value from an address, using `$1` as the bank select and value in Y register as address into X register|False|
|17|STX `$1`, Z|Load value from an address, using `$1` as the bank select and value in Y register as address into X register|False|
|18|STY `$1`|Load value from Y register into `$1`|False|
|19|STY `$1`, X|Load value from an address, using `$1` as the bank select and value in X register as address into Y register|False|
|20|STY `$1`, Z|Load value from an address, using `$1` as the bank select and value in Z register as address into Y register|False|
|21|STZ `$1`|Load value from Z register into `$1`|False|
|22|STZ `$1`, X|Load value from an address, using `$1` as the bank select and value in X register as address into Z register|False|
|23|STZ `$1`, Y|Load value from an address, using `$1` as the bank select and value in Y register as address into Z register|False|
|24|STI `$1`|Load value from Interrupt Register into `$1`|False|
|25|STA `$1`, X|Load value from an address, using `$1` as the bank select and value in X register as address into interrupt register|False|
|26|STA `$1`, Y|Load value from an address, using `$1` as the bank select and value in Y register as address into interrupt register|False|
|27|STA `$1`, Z|Load value from an address, using `$1` as the bank select and value in Z register as address into interrupt register|False|
|28|TAX|Transfer value from Accumulator into X|False|
|29|TAY|Transfer value from Accumulator into Y|False|
|30|TAZ|Transfer value from Accumulator into Z|False|
|31|TXA|Transfer value from X into accumulator|False|
|32|TYA|Transfer value from Y into accumulator|False|
|33|TZA|Transfer value from Z into accumulator|False|
|34|TBA|Transfer value from Bank Select Register into Accumulator|False|
|35|TTX|Transfer Stack Top Pointer into X|False|
|36|TXT|Transfer X into Stack Top Pointer|False|
|37|TTB|Transfer Stack Base Pointer into X|False|
|38|TBT|Transfer X into Stack Base Pointer|False|
|39|PHA|Push Accumulator onto stack|False|
|40|PHP|Push Processor Flags onto stack|False|
|41|PLA|Pull Accumulator from stack|False|
|42|PLP|Pull processor flags from stack|False|
|43|AND `$1`|Logical AND on the contents of the Accumulator using `$1` result stored in the accumulator|False|
|44|OR `$1`|Logical OR on the contents of the Accumulator using `$1`, result stored in the accumulator|False|
|45|XOR `$1`|Logical OR on the contents of the Accumulator using `$1`, result stored in the accumulator|False|
|46|ADC `$1`|Adds the contents of `$1` and carry bit to the accumulator. `A + $1`|False|
|47|SBC `$1`|Subtracts the contents of `$1` and carry bit from the accumulator. `A - $1`|False|
|48|UMUL `$1`|Unsigned Multiplies the contents of `$1` with the accumulator `A * $1`|False|
|49|UDIV `$1`|Unsigned Divides the accumulator by the contents of `$1`  `A / $1`|False|
|50|MUL `$1`|Signed Multiplies the contents of `$1` with the accumulator `A * $1`|False|
|51|DIV `$1`|Signed Divides the accumulator by the contents of `$1`  `A / $1`|False|
|52|INC `$1`|Increments the contents of `$1`|False|
|53|INA|Increments the contents of the accumulator|False|
|54|INX|Increments the contents of the X register|False|
|55|INY|Increments the contents of the Y register|False|
|56|INZ|Increments the contents of the Z register|False|
|57|DEC `$1`|Increments the contents of `$1`|False|
|58|DEA|Decrements the contents of the accumulator|False|
|59|DEX|Decrements the contents of the X register|False|
|60|DEY|Decrements the contents of the Y register|False|
|61|DEZ|Decrements the contents of the Z register|False|
|62|LSL|Logical shift left of the Accumulator by 1 bit.|False|
|63|LSR|Logical shift right of the Accumulator by 1 bit.|False|
|64|ROL|Rotate left the Accumulator by 1 bit.|False|
|65|ROR|Rotate right the Accumulator by 1 bit.|False|
|66|ASL|Arithmetic shift left of the Accumulator by 1 bit.|False|
|67|ASR|Arithmetic shift right of the Accumulator by 1 bit.|False|
|68|CMP `$1`|Compare the value of the Accumulator to `$1`.|False|
|69|CPX `$1`|Compare the value of the X register to `$1`|False|
|70|CPY `$1`|Compare the value of the Y register to `$1`|False|
|71|CPZ `$1`|Compare the value of the Z register to `$1`|False|
|72|JMP|Set the program counter to `$1`|False|
|73|JSR|Jump to subroutine. Push the PCBS then PC onto stack then set the PC to `$1`|False|
|74|RTS|Return from subroutine. Pull PC then PCBS value from top of stack.|False|
|75|BCC `$1`|Branch to `$1` if the carry flag is 0|False|
|76|BCS `$1`|Branch to `$1` if the carry flag is 1|False|
|77|BNE `$1`|Branch to `$1` if the equal flag is 0|False|
|78|BEQ `$1`|Branch to `$1` if the equal flag is 1|False|
|79|BLT `$1`|Branch to `$1` if the less than flag is 1|False|
|80|BMT `$1`|Branch to `$1` if the more than flag is 1|False|
|81|BMI `$1`|Branch to `$1` if the negative flag is 1|False|
|82|BPL `$1`|Branch to `$1` if the negative flag is 0|False|
|83|CLC|Clear clarry flag|False|
|84|SEC|Set carry flag|False|
|85|CLI|Clear interrupt disable|False|
|86|SEI|Set interrupt disable|False|
|87|CPS|Clear page select|False|
|88|SPS|Set Page Select|False|
|89|HLT|Halt the processor|False|
|90|INT `#1`|Raises a kernel interrupt of value `#1`|False|
