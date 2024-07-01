MMU takes in a 24-bit wide address and selects the appropriate RAM for reading and writing.

There's 2 RAM units, General Purpose and Graphical.

Technically, the General Purpose RAM is just 24 bits but the address is split so that it can be managed on a 16-bit bus.

The first 2 bytes of the address are seen as an actual address by the rest of the CPU.
The last byte is seen as a bank select, with each address being mapped onto each bank.

There's 255 banks in total. All banks are general use except banks 0 and 255. 0 is ROM program memory, 255 is Gr-RAM.