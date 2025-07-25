class Calculator:
    # Class attribute shared across all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: does not depend on class or instance"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: accesses class-level data"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()