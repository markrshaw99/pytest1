from lib.string_builder import StringBuilder

def test_string_builder():
    stringbuilder1 = StringBuilder()
    stringbuilder1.add("alphabet")
    assert stringbuilder1.size() == 8
    assert stringbuilder1.output() == "alphabet"