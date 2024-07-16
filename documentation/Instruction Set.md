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
