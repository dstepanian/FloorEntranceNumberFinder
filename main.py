# Our house consist of 5 entrances and each entrance has 20 flats. 

flat_number = int(input("Write the flat's number: "))

entrance_number = (flat_number - 1) // 20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1 
print("Entrance is: ", entrance_number)
print("Floor is: ", floor_number)