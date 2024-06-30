# Lab#2 - Test design - designing practical test scenarios and test cases
# Student name: Mr Kamphaengphet Singkhon
# Student ID:653380120-2

import pytest
import source.print_promotion as promo

def test_TS001_TC01():
    result = promo.print_promotion(total_cost=500)
    assert result == 'Free ice cream cone = 1'

def test_TS001_TC02():
    result = promo.print_promotion(total_cost=699.99)
    assert result == 'Free ice cream cone = 1'

def test_TS002_TC03():
    result = promo.print_promotion(total_cost=700)
    assert result == 'Free chocolate cake = 1'

def test_TS002_TC04():
    result = promo.print_promotion(total_cost=1199.99)
    assert result == 'Free chocolate cake = 1'

def test_TS003_TC05():
    result = promo.print_promotion(total_cost=1200)
    assert result == 'Free ice cream cone = 1 and Free chocolate cake = 1'

def test_TS003_TC06():
    result = promo.print_promotion(total_cost=0)
    assert result == 'Thank you and see you next time'

def test_TS004_TC07():
    result = promo.print_promotion(total_cost=150)
    assert result == 'Thank you and see you next time'

def test_TS004_TC08():
    result = promo.print_promotion(total_cost=499.99)
    assert result == 'Thank you and see you next time'

def test_TS005_TC09():
    result = promo.print_promotion(total_cost=3500)
    assert result == 'Free ice cream cone = 2 and Free chocolate cake = 3'

def test_TS005_TC10():
    result = promo.print_promotion(total_cost=2400)
    assert result == 'Free ice cream cone = 2 and Free chocolate cake = 2'