A 16 bit computer with built in gpu.

Computer,  Graphical-16 bit-1st version

## Desired Features 
- 16 bits
- Ability to render onto a set resolution screen.
- Uses Digital by Hneeman
- Capability to use an assembler ide directly connected to Digital (https://github.com/hneemann/Assembler)
- Small terminal for basic commands 
- 6502 instruction set with extras added in 
- Little Endian architecture 
- Signed and unsigned integer support 
- float support
- 32 MiB of RAM. 8-bit bank select with 16 bit-wide addresses and 2 words per address. Very last bank (`11111111`) is graphic ram.
- Interrupts 
     - hardware interrupt 
     - kernel call 
- Stack
- Flags
	- Zero
	- Negative
	- Carry
	- Interrupt Disable
	- More Than
	- Equal
	- Less than
- Registers: 
     1. General Purpose X
     2. General Purpose Y
     3. General Purpose Z
     4. Accumulator - output of alu
     5. AccumulatorHigh - High output of ALU, only used
     6. Program Counter - 16 bits
     7. Program Bank Counter - 8 bits
     8. Instruction Register
     9. Stack Top Pointer 
     10. Stack Base Pointer
     11. Processor Status Register
     12. Bank Select Register
     13. Address Access Register
     14. Control Counter