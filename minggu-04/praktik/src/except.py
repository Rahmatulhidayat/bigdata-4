while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

raise NameError('HiThere')

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


KeyboardInterrupt