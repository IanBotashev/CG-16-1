# CG-16-1
#### Made in [Digital v0.30 by Hneeman](https://github.com/hneemann/Digital)

A 16-bit processor with capability for graphics.

## Running processor in [Digital v0.30](https://github.com/hneemann/Digital)

1. Clone this repository onto your machine.
2. Download Digital.zip from [here](https://github.com/hneemann/Digital/releases)
3. Unzip
4. Run Digital
   - If on linux, run Digital.sh 
   - If on windows, run Digital.exe
5. Open the processor: Top left, file > open > navigate to repo, open `CG-16-1-Processor.dig`
6. Load program hex onto processor by right clicking on `ROM` in the `MMU` section > Edit > File > Load 
   - Make sure to press only `OK` when exiting, otherwise ROM does not save.

## Running processor emulator
Work in progress...


## Todo:
- Pipe ALU output high to the X register
- Assembler
- Emulator
- Addressing modes
- Allow normal fetch to be 1 cycle, interrupt fetch to be 2
- Push PC and PCBS onto stack when interrupted