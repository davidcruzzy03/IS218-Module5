from app.calculator_memento import CalculatorMemento


def test_memento_to_dict_and_from_dict():
    memento = CalculatorMemento([])

    data = memento.to_dict()
    restored = CalculatorMemento.from_dict(data)

    assert isinstance(data, dict)
    assert "history" in data
    assert "timestamp" in data
    assert isinstance(restored, CalculatorMemento)
    assert restored.history == []