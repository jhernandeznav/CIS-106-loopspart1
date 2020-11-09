def get_value(name):
    print("Enter " + name + " value:")
    value = int(input())
    return value


def while_loop(start, stop, increment):
    print("While loop counting from " + str(start) + " to " + str(stop) + " by " + str(increment) + ":")
    count = start
    while count <= stop:
        print(count)
        count = count + increment


def main():
    start = get_value("starting")
    stop = get_value("ending")
    increment = get_value("increment")
    while_loop(start, stop, increment)


main()
