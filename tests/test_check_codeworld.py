from lib.check_codeword import *

def test_check_codeword_correct_incorrect():
    assert check_codeword("horse") == "Correct! Come in."

def test_check_codeword_close():
    assert check_codeword("hassle") == "Close, but nope."

def test_check_codeword_incorrect():
    assert check_codeword("pineapple") == "WRONG!"