import json

microinstructions_map = {
    "mmuread": 0,
    "mmuwrite": 0,
    "xread": 0,
    "xwrite": 0,
    "yread": 0,
    "ywrite": 0,
    "zread": 0,
    "zwrite": 0,
    "aread": 0,
    "awrite": 0,
    "pcread": 0,
    "pcwrite": 0,
    "pcinc": 0,
    "pcclr": 0,
    "pcbsread": 0,
    "pcbswrite": 0,
    "pcbsclr": 0,
    "irread": 0,
    "irwrite": 0,
    "stread": 0,
    "stwrite": 0,
    "sbread": 0,
    "sbwrite": 0,
    "bsread": 0,
    "bswrite": 0,
    "aawrite": 0,
    "aluop": "00000",
    "aluwriteflags": 0,
    "carryset": 0,
    "carryclear": 0,
    "zeroset": 0,
    "zeroclear": 0,
    "negativeset": 0,
    "negativeclear": 0,
    "morethanset": 0,
    "morethanclear": 0,
    "equalset": 0,
    "equalclear": 0,
    "lessthanset": 0,
    "lessthanclear": 0,
    "disableinterrupts": 0,
    "enableinterrupts": 0,
    "ccclr": 0,
    "flagsread": 0,
    "flagswrite": 0,
    "readinstructionlow": 0,
    "readinstructionhigh": 0,
    "stinc": 0,
    "stdec": 0,
    "stclr": 0,
    "aluread": 0,
    "aluselectxhigh": 0,
    "condjump": "000",
    "condjumpdesired": 0,
    "haltclock": 0,
    "pageset": 0,
    "pageclear": 0,
}


def main():
    file = input("file: ")
    with open(file, 'r') as f:
        file = json.load(f)
        values = file["values"]
        for value in values:
            print("0b" + convert_microinstructions_to_binary(value))


def convert_microinstructions_to_binary(microinstructions):
    """
    Converts a dict of microinstructions ({"pcread": 1, "aawrite": 1}) to a string of little-endian binary.
    :param microinstructions:
    :return:
    """
    microinstructions_map_copy = microinstructions_map.copy()
    microinstructions_map_copy.update(microinstructions)
    return f"{''.join(str(e) for e in reversed(microinstructions_map_copy.values()))}"


if __name__ == "__main__":
    main()