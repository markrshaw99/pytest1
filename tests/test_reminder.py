import pytest
from lib.reminder import Reminder

def test_reminder():
    reminder1 = Reminder("Mark")
    reminder1.remind_me_to("Eat")
    assert reminder1.remind() == "Eat, Mark!"

def test_reminder_exception():
    reminder2 = Reminder("Bronwen")
    with pytest.raises(Exception) as e:
        reminder2.remind()
    assert str(e.value) == "No reminder set!"

