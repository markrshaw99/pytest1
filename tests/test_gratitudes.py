from lib.gratitudes import *

def test_gratitudes():
    gratitude1 = Gratitudes()
    gratitude1.add("Health")
    assert gratitude1.format() == "Be grateful for: Health"

def test_gratitudes_multi():
    gratitude2 = Gratitudes()
    gratitude2.add("Family")
    gratitude2.add("John Cena")
    gratitude2.add("Chicken and chorizzo orzo")
    assert gratitude2.format() == "Be grateful for: Family, John Cena, Chicken and chorizzo orzo"
