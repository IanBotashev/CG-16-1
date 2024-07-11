POSSIBLE_INSTRUCTIONS = ["MOV", "ADC"]


class Instruction:
    """
    Represents an instruction, such as MOV, LDA, ADC, etc.
    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        return self.value == other.value

    def __repr__(self):
        return f"Instruction({self.value})"
