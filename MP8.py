print("Calculator")

for i in range(2):
    print("\nCalculation", i + 1)

    A = float(input("Enter A: "))
    B = float(input("Enter B: "))

    print("\nChoose an operation:")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        result = A + B
        print("Result:", result)

    elif operator == "-":
        result = A - B
        print("Result:", result)

    elif operator == "*":
        result = A * B
        print("Result:", result)

    elif operator == "/":
        if B != 0:
            result = A / B
            print("Result:", round(result, 2))
        else:
            print("Error: Cannot divide by zero.")

    else:
        print("Invalid operator!")

print("\nCalculator finished!")