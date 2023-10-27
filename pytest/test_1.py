from datetime import date
import pytest


class Calculator:

    def calculate_addition(self, a: float, b: float) -> float:
        return a + b

    def calculate_multiply(self, a: float, b: float) -> float:
        return a * b

    def calculate_substraction(self, a: float, b: float) -> float:
        return a - b

    def calculate_divide(self, a: float, b: float) -> float:
        if b == 0.0:
            raise ValueError('b cannot accepts a zero value')

        return a / b

    def calculate_age(self, dob: date) -> int:
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age


# 创建 Calculator 类的实例
calculator = Calculator()

# 测试 calculate_addition 方法
def test_calculate_addition():
    result = calculator.calculate_addition(2.0, 3.0)
    assert result == 5.0

# 测试 calculate_multiply 方法
def test_calculate_multiply():
    result = calculator.calculate_multiply(2.0, 3.0)
    assert result == 6.0

# 测试 calculate_substraction 方法
def test_calculate_substraction():
    result = calculator.calculate_substraction(5.0, 2.0)
    assert result == 3.0

# 测试 calculate_divide 方法
def test_calculate_divide():
    result = calculator.calculate_divide(6.0, 2.0)
    assert result == 3.0

    with pytest.raises(ValueError):
        calculator.calculate_divide(6.0, 0.0)

# 测试 calculate_age 方法
def test_calculate_age():
    dob = date(1993, 12, 12)
    age = calculator.calculate_age(dob)
    assert age == 33

# 运行测试
if __name__ == "__main__":
    pytest.main()

# You are required to complete the following questions:

# 1. Use pytest library to complete the use cases:
# 1) Write a test case for testing function - calculate_addition()


# 2) Write a test case for testing function - calculate_multiply()


# 3) Write a test case for testing function - calculate_substraction()


# 4) Write a test case for testing function - calculate_divide()


# 2. Complete the following questions
# 1) Implement the function calculate_age(). When input a date of birth, the function can calculate the age and return its value


# 2) Use pytest library to test the function calculate_age()


