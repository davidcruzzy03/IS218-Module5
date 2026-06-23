import pytest
from decimal import Decimal

from app.calculation import Calculation
from app.exceptions import OperationError


def test_calculation_operation_failure_branch():
    calc = Calculation.__new__(Calculation)
    calc.operation = "Addition"
    calc.operand1 = "bad"
    calc.operand2 = Decimal("2")

    with pytest.raises(OperationError):
        calc.calculate()


def test_calculation_str_method():
    calc = Calculation("Addition", Decimal("1"), Decimal("2"))

    assert str(calc) == "Addition(1, 2) = 3"


def test_calculation_repr_method():
    calc = Calculation("Addition", Decimal("1"), Decimal("2"))

    text = repr(calc)

    assert "Calculation(operation='Addition'" in text
    assert "operand1=1" in text
    assert "operand2=2" in text
    assert "result=3" in text


def test_calculation_eq_not_implemented():
    calc = Calculation("Addition", Decimal("1"), Decimal("2"))

    assert calc.__eq__("not a calculation") is NotImplemented