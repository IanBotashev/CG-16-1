import pytest
from helpers.assembler.tokenizer.tokenizer import Tokenizer
from helpers.assembler.assembler_types import Instruction, Argument


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


@pytest.mark.parametrize(
    "string_to_parse, expected_token",
    [
        ("mOV", Instruction("mov")),
        ("AdC", Instruction("adc")),
        ("int", Instruction("int")),
        ("MOv", Instruction("mov")),
        pytest.param("NOT_AN_INSTRUCTION", None, marks=pytest.mark.xfail),
        pytest.param("3", None, marks=pytest.mark.xfail),
    ])
def test_instruction_tokenizing(tokenizer, string_to_parse, expected_token):
    """
    Make sure that the tokenizer returns the correct token when passing in just an instruction with no arguments.
    :return:
    """
    tokens = tokenizer.parse(string_to_parse)
    assert isinstance(tokens, list)
    assert tokens[0] == expected_token


@pytest.mark.parametrize(
    "string_to_parse, expected_token",
    [
        ("MOV 1", Instruction("mov", arguments=[Argument(1, address=False)])),
        ("aDC $2", Instruction("adc", arguments=[Argument(2, address=True)])),
        ("int $3, 4,$5, $6 ,      7", Instruction("int", arguments=[Argument(3, address=True), Argument(4, address=False), Argument(5, address=True), Argument(6, address=True), Argument(7, address=False)])),
        pytest.param("MoV invalid", None, marks=pytest.mark.xfail),
        pytest.param("MoV 1 2 $3", None, marks=pytest.mark.xfail),
        pytest.param("MoV $1 $2", None, marks=pytest.mark.xfail),
        pytest.param("MoV $1 2 3", None, marks=pytest.mark.xfail),
    ])
def test_argument_tokenizing(tokenizer, string_to_parse, expected_token):
    """
    Tests if the tokenizer can properly tokenize an instruction with arguments into the right token.
    :return:
    """
    tokens = tokenizer.parse(string_to_parse)
    assert isinstance(tokens, list)
    assert tokens[0] == expected_token
