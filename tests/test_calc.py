import pytest

from Calculator import LayMe

def test_positive_odds():
    result = LayMe(100, [150, 200])
    assert result['odds'] == round((2.5) * (3.0), 3)  # 2.5 * 3 = 7.5
    assert result['earnings'] == round(100 * 7.5 - 100, 2)

def test_negative_odds():
    result = LayMe(100, [-110, -200])
    expected_odds = round(((100/110)+1) * ((100/200)+1), 3)
    expected_earnings = round(100 * expected_odds - 100, 2)
    assert result['odds'] == expected_odds
    assert result['earnings'] == expected_earnings
