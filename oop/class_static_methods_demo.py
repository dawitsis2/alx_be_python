# class_static_methods_demo.py

class Calculator:
    """Calculator class demonstrating static and class methods."""
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers and reference a class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
