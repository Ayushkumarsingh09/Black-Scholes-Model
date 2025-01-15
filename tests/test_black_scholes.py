import pytest
from src.black_scholes import black_scholes

def test_call_option():
    price = black_scholes(100, 100, 1, 0.05, 0.2, "call")
    assert round(price, 2) == 10.45

def test_put_option():
    price = black_scholes(100, 100, 1, 0.05, 0.2, "put")
    assert round(price, 2) == 5.57
