def calculator():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /, %, **")
    print("Type 'exit' to quit")

    while True:
        try:
            expression = input("Enter your calculation: ")
            if expression.lower() == 'exit':
                print("Goodbye!")
                break

            # Evaluate the mathematical expression
            result = eval(expression)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()