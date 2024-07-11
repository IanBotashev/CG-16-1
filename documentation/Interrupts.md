# Interrupts

Interrupts are written to the Interrupt Register. If the interrupt flag is on, the control logic will finish the current instruction then write the address `0x10000` to the PC, running the interrupt handler.
The interrupt handler has to be written, the processor does not start with a handler.

The interrupt handlers **VERY FIRST** instruction MUST be `CIN`
