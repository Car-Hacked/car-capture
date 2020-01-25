import argparse
parser = argparse.ArgumentParser()
parser.add_argument("garage_id", help="The id for the garage.", type=int)
parser.add_argument("-c", "--capacity", help="The total capacity of the garage. Default of 100.", type=int)
parser.add_argument("-f", "--fill", help="Fill spaces in the garage.", type=int)

args = parser.parse_args()

# Fills Garage information with given info. Garage id is required and capacity will default to 100.
garage_id = args.garage_id
capacity = 100
if args.capacity:
    capacity = args.capacity

if args.fill:
    spaces_filled = args.fill
    available_spaces = capacity - spaces_filled
else:
    spaces_filled = 0
    available_spaces = capacity - spaces_filled


def print_info():
    print("Garage id: " + str(garage_id))
    print("Spaces filled: " + str(spaces_filled))
    print("Available spaces: " + str(available_spaces))


while True:

    name = input("""
1: increment filled spaces
2: decrement filled spaces
q: quit and print analytics
        Enter input:""")

    if name == '1':
        if spaces_filled == capacity:
            print("The garage is full")
            continue
        if spaces_filled < capacity:
            spaces_filled += 1
            available_spaces -= 1
            print_info()
    elif name == '2':
        if available_spaces == capacity:
            print_info()
            continue
        if available_spaces < capacity:
            spaces_filled -= 1
            available_spaces += 1
            print_info()
    elif name == 'q':
        print_info()
        break
    else:
        print("Response invalid. Enter 1 to increment. Enter 2 to decrement. Enter q to quit.")
