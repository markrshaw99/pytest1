from lib.password_checker import *
import pytest

def test_password_checker():
    passwordchecker1 = PasswordChecker()
    with pytest.raises(Exception) as e1:
        passwordchecker1.check("crap")
    assert str(e1.value) == "Invalid password, must be 8+ characters."
    assert passwordchecker1.check("alphabet") == True