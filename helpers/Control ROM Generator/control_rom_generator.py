import json
from helpers.microinstruction_generator import convert_microinstructions_to_binary


def main():
    json_file = "./control_rom.json"
    output_file = "../../hex/control_rom.hex"  # woops...
    fetch_cycle_length = 2
    control_steps_per_instruction = 16
    file_lines = ["v2.0 raw"]

    with open(json_file, "r") as f:
        json_data = json.load(f)
        for instruction in json_data:
            control_steps_remaining = control_steps_per_instruction
            file_lines.append(f"#===================START {instruction}===================")
            file_lines.append(f"{fetch_cycle_length}*0")
            control_steps_remaining -= fetch_cycle_length

            for step in json_data[instruction]:
                control_steps_remaining -= 1
                file_lines.append(hex(int(convert_microinstructions_to_binary(step), 2)))

            file_lines.append(f"{control_steps_remaining}*0")
            file_lines.append(f"#===================END {instruction}===================")

    with open(output_file, "w") as f:
        for line in file_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
