from validation import is_valid_name


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def main():
    while True:

        name = input("What's your name?: ")

        if is_valid_name(name):
            print_hi(name)
            break


if __name__ == '__main__':
    main()
