def add(n1, n2):
    return n1 + n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def sub(n1, n2):
    return n1 - n2

while True:
    print("\nPlease select operation -\n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n"
          "5. Exit\n")

    try:
        sel = int(input("Please select operation (1-5): "))
    except ValueError:
        print("❌ Invalid choice! Please enter a number between 1 and 5.")
        continue

    if sel == 5:
        print("Exiting Calculator. Goodbye!")
        break

    if sel not in [1, 2, 3, 4]:
        print("❌ Invalid option! Please select 1–5.")
        continue

    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        continue

    if sel == 1:
        print(f"{n1} + {n2} = {add(n1, n2)}")
    elif sel == 2:
        print(f"{n1} - {n2} = {sub(n1, n2)}")
    elif sel == 3:
        print(f"{n1} * {n2} = {mul(n1, n2)}")
    elif sel == 4:
        if n2 == 0:
            print("❌ Error! Division by zero is not allowed.")
        else:
            print(f"{n1} / {n2} = {div(n1, n2)}")
