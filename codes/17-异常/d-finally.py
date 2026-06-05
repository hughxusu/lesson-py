print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break
        
    try:
        answer = int(first_number) / int(second_number)
    except Exception as e:
        print(f"This is an error: {e}")
    else:
        print(answer)
    finally:
        print(f"first_number = {first_number}, second_number = {second_number}")