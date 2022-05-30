def square(x):
    """
    Square a number.
    """
    return x**2


if __name__ == "__main__":
    x = input("Enter a number: ")
    x = int(x)
    print(f"The square of {x} is {square(x)}.")
