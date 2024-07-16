import json
from helpers.microinstruction_generator import convert_microinstructions_to_binary
from py_markdown_table.markdown_table import markdown_table


def main():
    """
    Converts a .json file with microinstructions into a hex file saved in the hex folder. Used for the control rom.
    Also generates an instruction set .md table.
    :return:
    """
    json_file = "control_rom.json"
    output_bin_file = "../../hex/control_rom.hex"  # woops...

    doc_table_data = []
    output_md_doc_table = "../../documentation/Instruction Set.md"
    md_doc_table_fileheader = "# Instruction Set\n## Design\nEach instruction opcode is a byte.  \nWhich leaves 3 bytes for operands.  \n## Key\n`$` - Address  \n`#` - Literal value  \n\n"
    fetch_cycle_length = 2
    control_steps_per_instruction = 16
    file_lines = ["v2.0 raw"]

    with open(json_file, "r") as f:
        json_data = json.load(f)

        for instruction_id in json_data:
            # Generate binary
            instruction_code = json_data[instruction_id]["code"]
            control_steps_remaining = control_steps_per_instruction
            file_lines.append(f"{fetch_cycle_length}*0  # {instruction_id}, {len(instruction_code)} cycle(s)")
            control_steps_remaining -= fetch_cycle_length

            for step in instruction_code:
                control_steps_remaining -= 1
                file_lines.append(hex(int(convert_microinstructions_to_binary(step), 2)))

            file_lines.append(f"{control_steps_remaining}*0")

            # Add this instruction to doc table
            # Must be at the end as it's destructive
            doc_table_data.append(json_data[instruction_id])
            doc_table_data[-1].pop('code', None)

        print("Instruction space left:", 2**8 - len(json_data.keys()))

    # Generate hex file with all the microinstruction code
    with open(output_bin_file, "w") as f:
        for line in file_lines:
            f.write(line + "\n")

    # Generate documentation document
    with open(output_md_doc_table, "w") as f:
        # Write key and info, then the header for the table.
        f.writelines([md_doc_table_fileheader, "|opcode|" + "|".join(doc_table_data[0].keys()) + "|\n", "| --- " * (len(doc_table_data[0].keys()) + 1) + "|\n"])
        for index in range(len(doc_table_data)):
            f.write(f"|{index}|{"|".join([str(value) for value in doc_table_data[index].values()])}|\n")


if __name__ == "__main__":
    main()
