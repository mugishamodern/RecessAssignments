# Assignment One 2025 Solutions
# Name: ______________________
# Date: ______________________

# =============================
# Exercise 1: Lists
# =============================

# 1. Create a list with 5 items (names of people) and output the 2nd item.
people = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
print("Exercise 1.1:", people[1])  # Output the 2nd item

# 2. Change the value of the first item to a new value
people[0] = "Alex"
print("Exercise 1.2:", people)

# 3. Add a sixth item to the list
people.append("Fiona")
print("Exercise 1.3:", people)

# 4. Add "Bathel" as the 3rd item in your list
people.insert(2, "Bathel")
print("Exercise 1.4:", people)

# 5. Remove the 4th item from the list
people.pop(3)
print("Exercise 1.5:", people)

# 6. Use negative indexing to print the last item in your list
print("Exercise 1.6:", people[-1])

# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print("Exercise 1.7:", fruits[2:5])

# 8. Write a list of countries and make a copy of it.
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda"]
countries_copy = countries.copy()
print("Exercise 1.8:", countries_copy)

# 9. Loop through the list of countries
print("Exercise 1.9:")
for country in countries:
    print(country)

# 10. List of animal names and sort them in both descending and ascending order.
animals = ["zebra", "lion", "elephant", "giraffe", "antelope"]
animals_asc = sorted(animals)
animals_desc = sorted(animals, reverse=True)
print("Exercise 1.10 Ascending:", animals_asc)
print("Exercise 1.10 Descending:", animals_desc)

# 11. Output only animal names with the letter 'a' in them
animals_with_a = [animal for animal in animals if 'a' in animal]
print("Exercise 1.11:", animals_with_a)

# 12. Two lists: first names and second names. Join the two lists.
first_names = ["John", "Jane", "Jim"]
second_names = ["Doe", "Smith", "Brown"]
full_names = first_names + second_names
print("Exercise 1.12:", full_names)

# =============================
# Exercise 2: Tuples
# =============================

# 1. Output your favorite phone brand from the tuple
x = ("samsung", "iphone", "tecno", "redmi")
print("Exercise 2.1:", x[0])  # Example: samsung

# 2. Use negative indexing to print the 2nd last item
print("Exercise 2.2:", x[-2])

# 3. Update "iphone" to "itel" (tuples are immutable, so convert to list and back)
x_list = list(x)
x_list[1] = "itel"  # type: ignore
x = tuple(x_list)
print("Exercise 2.3:", x)

# 4. Add "Huawei" to your tuple
x = x + ("Huawei",)
print("Exercise 2.4:", x)

# 5. Loop through the tuple above
print("Exercise 2.5:")
for phone in x:
    print(phone)

# 6. Remove/delete the first item in your tuple
x = x[1:]
print("Exercise 2.6:", x)

# 7. Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Gulu", "Mbarara", "Jinja"])
print("Exercise 2.7:", cities)

# 8. Unpack your tuple
city1, city2, city3, city4, city5 = cities
print("Exercise 2.8:", city1, city2, city3, city4, city5)

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities
print("Exercise 2.9:", cities[1:4])

# 10. Two tuples: first names and second names. Join the two tuples.
tuple_first_names = ("John", "Jane", "Jim")
tuple_second_names = ("Doe", "Smith", "Brown")
joined_names = tuple_first_names + tuple_second_names
print("Exercise 2.10:", joined_names)

# 11. Create a tuple of colors and multiply it by 3.
colors = ("red", "green", "blue")
colors_multiplied = colors * 3
print("Exercise 2.11:", colors_multiplied)

# 12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print("Exercise 2.12:", thistuple.count(8))

# =============================
# Exercise 3: Sets
# =============================

# 1. Use the set() constructor to create a set of 3 favorite beverages.
beverages = set(["coffee", "tea", "juice"])
print("Exercise 3.1:", beverages)

# 2. Add 2 more items to the beverages set.
beverages.add("water")
beverages.add("soda")
print("Exercise 3.2:", beverages)

# 3. Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("Exercise 3.3:", "microwave" in mySet)

# 4. Remove "kettle" from the set above.
mySet.discard("kettle")
print("Exercise 3.4:", mySet)

# 5. Loop through the set above.
print("Exercise 3.5:")
for item in mySet:
    print(item)

# 6. Write a set of 4 items and a list of two items. Add elements in the list to the set.
set_items = {"pen", "pencil", "eraser", "ruler"}
list_items = ["marker", "sharpener"]
set_items.update(list_items)
print("Exercise 3.6:", set_items)

# 7. Two sets: ages and first names. Join the two sets.
ages = {20, 25, 30}
first_names_set = {"John", "Jane", "Jim"}
joined_set = ages.union(first_names_set)
print("Exercise 3.7:", joined_set)

# =============================
# Exercise 4: Strings
# =============================

# 1. Declare two variables, an integer and a string, and concatenate them.
num = 25
text = " years old"
print("Exercise 4.1:", str(num) + text)

# 2. Remove spaces at the beginning, in the middle, and at the end.
txt = "      Hello,       Uganda!       "
no_spaces = " ".join(txt.split())
print("Exercise 4.2:", no_spaces)

# 3. Convert the value of 'txt' to uppercase.
print("Exercise 4.3:", txt.upper())

# 4. Replace character 'U' with 'V' in the string above.
print("Exercise 4.4:", txt.replace('U', 'V'))

# 5. Return a range of characters in the 2nd, 3rd and 4th position.
y = "I am proudly Ugandan"
print("Exercise 4.5:", y[1:4])

# 6. Correct the string with quotes error.
x = 'All "Data Scientists" are cool!'
print("Exercise 4.6:", x)

# =============================
# Exercise 5: Dictionaries
# =============================

# 1. Print the value of the shoe size.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print("Exercise 5.1:", Shoes["size"])

# 2. Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("Exercise 5.2:", Shoes)

# 3. Add a key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"
print("Exercise 5.3:", Shoes)

# 4. Return a list of all the keys in the dictionary above.
print("Exercise 5.4:", list(Shoes.keys()))

# 5. Return a list of all the values in the dictionary above.
print("Exercise 5.5:", list(Shoes.values()))

# 6. Check if the key "size" exists in the dictionary above.
print("Exercise 5.6:", "size" in Shoes)

# 7. Loop through the dictionary above.
print("Exercise 5.7:")
for key, value in Shoes.items():
    print(key, ":", value)

# 8. Remove "color" from the dictionary.
Shoes.pop("color", None)
print("Exercise 5.8:", Shoes)

# 9. Empty the dictionary above.
Shoes.clear()
print("Exercise 5.9:", Shoes)

# 10. Write a dictionary of your choice and make a copy of it.
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
car_copy = car.copy()
print("Exercise 5.10:", car_copy)

# 11. Show nested dictionaries
family = {
    "child1": {"name": "John", "age": 10},
    "child2": {"name": "Jane", "age": 8}
}
print("Exercise 5.11:", family)

# =============================
# Assignment Two: Inventory Management
# =============================

# Initial stock items (item name and quantity)
stock = [
    {"item": "Pens", "quantity": 20},
    {"item": "Notebooks", "quantity": 15},
    {"item": "Markers", "quantity": 10},
    {"item": "Erasers", "quantity": 25}
]

# Function to display stock items
def display_stock(stock_list):
    print("\nCurrent Stock:")
    for s in stock_list:
        print(f"Item: {s['item']}, Quantity: {s['quantity']}")

display_stock(stock)

# Function to update stock quantity
def update_stock(stock_list, item_name, new_quantity):
    for s in stock_list:
        if s["item"].lower() == item_name.lower():
            s["quantity"] = new_quantity
            print(f"Updated {item_name} to quantity {new_quantity}.")
            return
    print(f"Item '{item_name}' not found in stock.")

# Example update (you can change these values to test)
update_stock(stock, "Pens", 30)

display_stock(stock) 