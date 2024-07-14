from pyparsing import Word, alphanums, nums, alphas, Combine, DelimitedList, Literal, Optional, hexnums, Suppress, ZeroOrMore
from helpers.assembler.assembler_types import Instruction, Argument
from helpers.assembler.exceptions import InvalidSyntax

class Tokenizer:
    """
    Takes a list of raw strings and converts them into Instruction objects
    """
    def __init__(self):
        pass

    def parse_string(self, string):
        """
        Parses a single string and, should, return a single Instruction object
        :param string:
        :return:
        """
        # Definitions
        mnemonic = Word(alphas).setResultsName("mnemonic").set_parse_action(lambda x: str(x[0]).lower())
        hex_value = Combine(Literal("0x") + Word(hexnums, max=4)).set_parse_action(lambda x: int(x[0], 16))
        binary_value = Combine(Literal("0b") + Word("01", max=16)).set_parse_action(lambda x: int(x[0], 2))
        decimal_value = Word(nums).set_parse_action(lambda x: int(x[0]))

        argument = Combine(Optional(Literal("$")).set_results_name("address") + (hex_value | binary_value | decimal_value).set_results_name("arg_value")).set_parse_action(self.parse_action_for_argument)

        instruction = mnemonic + Optional(DelimitedList(argument, ",")).setResultsName("arguments")
        data = instruction.parse_string(string, parse_all=True)
        if len(list(data.arguments)) > 0:
            result = Instruction(data.mnemonic, arguments=data.arguments)
        else:
            result = Instruction(data.mnemonic)

        if not result.check_if_valid_instruction():
            raise InvalidSyntax(f"Unknown mnemonic {result.mnemonic}")

        return result

    def parse_action_for_argument(self, x):
        """
        pyparsing parse action for an argument
        :return:
        """
        return Argument(x.arg_value, address=x.address == "$")
