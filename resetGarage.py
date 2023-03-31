import api

list_of_garages = api.get_garages()
i = 1
for garage in list_of_garages:
    name = garage.name
    print(f"{i} - {name}")
    i += 1

select = input("Select garage: ")
range_of = range(len(list_of_garages))

while True:
    try:
        select = int(select) - 1
        if select not in range_of:
            print("Input must be one of the listed numbers")
            select = input("Select garage: ")
        else:
            break
    except ValueError:
        print("Input must be one of the listed numbers")
        select = input("Select garage: ")


garage = list_of_garages[select]
print(garage.name)
garage = api.get_garages()[int(select)]

print ("1 - full(red) \n2 - critical(yellow)\n3 - open(green)")
fullness = input("Select fullness: ")
while True:
    try:
        fullness = int(fullness) - 1
        if select not in range_of:
            print("Input must be one of the listed numbers")
            select = input("Select garage: ")
        else:
            break
    except ValueError:
        print("Input must be one of the listed numbers")
        select = input("Select garage: ")

if fullness == 0:
    garFull = garage.capacity
elif fullness == 1:
    garFull = garage.capacity * 0.80
else:
    garFull = garage.capacity * .25

garage.cars_in_lot = garFull

api.put_garage(garage)

