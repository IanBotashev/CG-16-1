POSSIBLE_INSTRUCTIONS = ["MOV", "ADC", "INT"]


class Instruction:
    """
    Represents an instruction, such as MOV, LDA, ADC, etc.
    """
    def __init__(self, value, arguments=None):
        if arguments is None:
            arguments = []

        self.arguments = arguments
        self.value = value

    def check_if_valid_instruction(self):
        """
        Checks if the value of this instruction is in the POSSIBLE_INSTRUCTIONS list.
        :return:
        """
        return self.value in POSSIBLE_INSTRUCTIONS

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False

        return self.value.lower() == other.value.lower() and self.arguments == other.arguments

    def __repr__(self):
        return f"Instruction({self.value}, Arguments={self.arguments})"


class Argument:
    """
    Represents an argument that an instruction could have.
    i.e. `MOV 1` 1 is an immediate-value argument.
    """
    def __init__(self, value, address=False):
        """
        :param value: The value of this argument, in decimal.
        :param address: Set to true if this argument was preceded with a '$' character.
        """
        self.value = value
        self.address = address

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False

        return self.value == other.value and self.immediate == other.immediate

    def __repr__(self):
        return f"Argument({self.value}, immediate={self.immediate})"
