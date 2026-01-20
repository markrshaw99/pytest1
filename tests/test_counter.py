from lib.counter import Counter

def test_counter():
    counter1=Counter()
    counter1.add(10)
    assert counter1.report() == "Counted to 10 so far."