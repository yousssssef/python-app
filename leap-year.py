fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape","Date"]

counter = 5

while counter > 0:
    try:
        index = int(input("Enter an index number (0-6): "))
        fruit = fruits[index]

    except ValueError:
        counter -= 1
        print(f"Warning message, you have {counter} chances left. Try again!")

    except IndexError:
        counter -= 1
        print(f"Warning message, you have {counter} chances left. Try again!")

    else:
        print("My favorite fruit is", fruit)
        print("Congrats! You've entered a valid input.")
        break

    finally:
        print("Our fruits are always fresh!")
