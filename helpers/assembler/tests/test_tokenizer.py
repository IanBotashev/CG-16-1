import pytest
from helpers.assembler.tokenizer.tokenizer import Tokenizer
from helpers.assembler.assembler_types import Instruction


@pytest.fixture
def tokenizer():
    return Tokenizer()


def test_tokenizer_fixture(tokenizer):
    """
    Tests if the fixture is working correctly.
    :param tokenizer:
    :return:
    """
    assert isinstance(tokenizer, Tokenizer)


@pytest.mark.parametrize("string_to_parse", ["MOV", "ADC", "INT"])
def test_instruction_tokenizing(tokenizer, string_to_parse):
    """
    Make sure that the tokenizer returns the correct token when passing in just an instruction with no arguments.
    :return:
    """
    tokens = tokenizer.parse(string_to_parse)
    assert tokens[0].value == string_to_parse
    assert isinstance(tokens[0], Instruction)
