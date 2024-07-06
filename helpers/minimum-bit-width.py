from math import log2, ceil


def main():
    while True:
        try:
            number = int(input("> "))
        except ValueError:
            print("Please enter a number")
            continue

        if number <= 0:
            print("Number must be bigger than 0")
            continue

        log_of_number = log2(number)
        print(ceil(log_of_number))


if __name__ == "__main__":
    main()
