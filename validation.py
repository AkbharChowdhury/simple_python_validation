def is_valid_name(name):
    if len(name.strip()) == 0:
        print("you must enter your name")
        return False

    if name.isdigit():
        print('you cannot have numbers in your name')
        return False

    return True
