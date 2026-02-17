class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: does not depend on class or instance state"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: has access to class attributes"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
