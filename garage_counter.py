import requests
import api


list_of_garages = []
for garage in api.get_garages():
    i = 1
    name = garage.name
    print(f"{i} - {name}")
    i += 1

select = input("Select garage:")
garage = api.get_garages()[int(select) - 1]
print(garage.name)

garage_id = garage.name
capacity = garage.capacity
spaces_filled = garage.cars_in_lot
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
