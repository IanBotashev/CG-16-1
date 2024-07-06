# Flags

| Flag              | Description                                                               |
| ----------------- | ------------------------------------------------------------------------- |
| Carry             | Set to 1 if the previous ALU operation had a bit carry into the 17th bit. |
| Zero              | Set to 1 if the previous ALU operation resulted in a 0.                   |
| Negative          | Set to 1 if the previous ALU operation resulted in a negative number.     |
| More Than         | Set to 1 if Number A > Number B in the ALU after a compare instruction.   |
| Equal             | Set to 1 if Number A = Number B in the ALU after a compare instruction.   |
| Less Than         | Set to 1 if Number A < Number B in the ALU after a compare instruction.   |
| Interrupt Disable | If set to 1, disables interrupts.                                         |
| Page Select       | Selects which page to display from the Gr-RAM                             |
