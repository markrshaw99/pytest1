from lib.report_length import *

def test_report_length_standard():
    assert report_length("Alphabet") == "This string was 8 characters long."

def test_report_length_numeric():
    assert report_length("1234567890") == "This string was 10 characters long."

def test_report_length_empty():
    assert report_length("") == "This string was 0 characters long."

def test_report_length_special_chars():
    assert report_length("! @# $") == "This string was 6 characters long."
