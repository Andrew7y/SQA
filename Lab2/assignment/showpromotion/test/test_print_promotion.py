# Lab#2 - Test design - designing practical test scenarios and test cases
# Student name: Mr Kamphaengphet Singkhon
# Student ID:653380120-2

import pytest
import source.print_promotion as promo

def test_TS001_TC01(capsys):
    promo.print_promotion(total_cost=500)
    captured = capsys.readouterr()
    assert captured.out == 'Free ice cream cone = 1.0\n'

def test_TS001_TC02(capsys):
    promo.print_promotion(total_cost=699.99)
    captured = capsys.readouterr()
    assert captured.out == 'Free ice cream cone = 1.0\n'

def test_TS002_TC03(capsys):
    promo.print_promotion(total_cost=700)
    captured = capsys.readouterr()
    assert captured.out == 'Free chocolate cake = 1.0\n'

def test_TS002_TC04(capsys):
    promo.print_promotion(total_cost=1199.99)
    captured = capsys.readouterr()
    assert captured.out == 'Free chocolate cake = 1.0\n'

def test_TS003_TC05(capsys):
    promo.print_promotion(total_cost=1200)
    captured = capsys.readouterr()
    assert captured.out == 'Free ice cream cone = 1.0 and Free chocolate cake = 1.0\n'

def test_TS003_TC06(capsys):
    promo.print_promotion(total_cost=1200.00)
    captured = capsys.readouterr()
    assert captured.out == 'Free ice cream cone = 1.0 and Free chocolate cake = 1.0\n'

def test_TS004_TC07(capsys):
    promo.print_promotion(total_cost=150)
    captured = capsys.readouterr()
    assert captured.out == 'Thank you and see you next time\n'

def test_TS004_TC08(capsys):
    promo.print_promotion(total_cost=499.99)
    captured = capsys.readouterr()
    assert captured.out == 'Thank you and see you next time\n'

def test_TS005_TC09(capsys):
    promo.print_promotion(total_cost=3500)
    captured = capsys.readouterr()
    assert captured.out == 'Free ice cream cone = 2.0 and Free chocolate cake = 3.0\n'

def test_TS005_TC10(capsys):
    promo.print_promotion(total_cost=2400)
    captured = capsys.readouterr()
    assert captured.out == 'Free ice cream cone = 2.0 and Free chocolate cake = 2.0\n'

