import pytest
from src.greeks import calculate_greeks

def test_greeks():
    greeks = calculate_greeks(100, 100, 1, 0.05, 0.2)
    assert round(greeks["Delta (Call)"], 2) == 0.63
    assert round(greeks["Gamma"], 4) == 0.0198
