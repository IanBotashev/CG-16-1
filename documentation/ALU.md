# ALU
Comparing is done by default, ALU just needs to be allowed to set our Processor Flags
5-bit wide operation selector

## Operations
| Operation              | OP # | Description                              |     |
| ---------------------- | ---- | ---------------------------------------- | --- |
| Add                    | 0    | A + B + (0 or 1 depending on Carry flag) |     |
| Subtract               | 1    | A - B                                    |     |
| Increment              | 2    | A + 1                                    |     |
| Decrement              | 3    | A - 1                                    |     |
| Unsigned Multiply      | 4    | A * B (Unsigned)                         |     |
| Unsigned Division      | 5    | A / B (Unsigned)                         |     |
| Multiply               | 6    | A * B                                    |     |
| Division               | 7    | A / B                                    |     |
| And                    | 8    | A and B                                  |     |
| Or                     | 9    | A or B                                   |     |
| Xor                    | 10   | A xor B                                  |     |
| Logical Shift Left     | 11   | Logically shifts A's bits left by 1      |     |
| Logical Shift Right    | 12   | Logically shifts A's bits righ by 1      |     |
| Rotate Left            | 13   | Rotates A's bits left by 1               |     |
| Rotate Right           | 14   | Rotates A's bits right by 1              |     |
| Arithmetic Shift Left  | 15   | Arithmetically Shifts A's bits left by 1 |     |
| Arithmetic Shift Right | 16   | Arithmetically Shifts A's bits left by 2 |     |


