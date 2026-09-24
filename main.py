from calc import add, subtract, multiply, divide

def main():
    print("Simple Calculator")
    a = float(input("First number: "))
    op = input("Operation (+, -, *, /): ")
    b = float(input("Second number: "))

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = subtract(a, b)
    elif op == "*":
        result = multiply(a, b)
    elif op == "/":
        result = divide(a, b)
    else:
        print("Unknown operation")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()