# File: "tests/test_greet.py"
from lib.greet import greet

def test_greet():
  
  assert greet("Mark") == "Hello, Mark!"

