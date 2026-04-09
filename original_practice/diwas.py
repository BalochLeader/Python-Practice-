import diwas

def test_math_utils():
    assert diwas.add(5, 10) == 15
    assert diwas.mul(5, 10) == 50
    assert diwas.divide(10, 2) == 5.0
    assert diwas.square_root(16) == 4.0
    assert diwas.greatest([1, 5, 10, 2]) == 10
    assert diwas.smallest([1, 5, 10, 2]) == 1
    assert diwas.sum_list([1, 2, 3]) == 6
    print("Math utils tests passed!")

def test_converters():
    assert diwas.celsius_to_fahrenheit(0) == 32
    assert diwas.fahrenheit_to_celsius(32) == 0
    print("Converters tests passed!")

def test_calculators():
    assert diwas.simple_interest(1000, 5, 2) == 100
    assert diwas.calculator("2 + 2 * 2") == 6
    print("Calculators tests passed!")

def test_random_tools():
    r = diwas.random(1, 5)
    assert 1 <= r <= 5
    c = diwas.choice(["a", "b", "c"])
    assert c in ["a", "b", "c"]
    print("Random tools tests passed!")

def test_algebra():
    assert diwas.solve_linear(2, -4) == 2.0
    assert diwas.solve_quadratic(1, -3, 2) == (2.0, 1.0)
    print("Algebra tests passed!")

if __name__ == "__main__":
    test_math_utils()
    test_converters()
    test_calculators()
    test_random_tools()
    test_algebra()
    print("All tests passed!")