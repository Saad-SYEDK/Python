# Dictionary in Python

# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Dictionaries are defined using curly braces {} and key-value pairs are separated by commas. The key and value are separated by a colon :.
# They are unordered, mutable, and indexed. You can use any immutable data type as a key (like strings, numbers, tuples) and any data type as a value (like strings, numbers, lists, other dictionaries).

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

# Adding a new key-value pair to the dictionary
my_dict["country"] = "USA"

# Updating an existing key-value pair
my_dict["age"] = 31

# Removing a key-value pair from the dictionary
del my_dict["city"]

# Iterating through a dictionary
for key in my_dict:
    print(key, ":", my_dict[key])

# You can also use the items() method to iterate through key-value pairs
for key, value in my_dict.items():
    print(key, ":", value)
    
# Deleting the entire dictionary
del my_dict 

# We can also use the clear() method to remove all items from the dictionary without deleting it entirely.
my_dict.clear()





"""
Exercisse : Dictionary 

1. We have following information on countries and their population (population is in crores),

    Country	Population
     China	  143
     India	  136
     USA	  32
    Pakistan  21
 Using above create a dictionary of countries and its population
 Write a program that asks user for three type of inputs,
 print: if user enter print then it should print all countries with their population in this format,
    china==>143
    india==>136
    usa==>32
    pakistan==>21
 add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
 remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
 query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
 """
 
 # Solution
population = {}
population["china"] = 143
population["india"] = 136
population["usa"] = 32
population["pakistan"] = 21
while True:
    ip = input("Add, Remove, Query or any other to exit: ")
    if ip == "Add":
        ip = input("Enter Country name to be added: ")
        if ip in population:
            print("Country already exist!")
        else:
            population[ip] = input("Enter population:")
    elif ip == "Remove":
        ip = input("Enter country to be removed: ")
        if ip in population:
            del population[ip]
        else:
            print("Country does not exist!")
        for i, j in population.items():
            print(i, j)
    elif ip == "Query":
        ip = input("enter the country name: ")
        if ip in population:
            print(population[ip])
        else:
            print("Country does not exists!")
    else:
        break
    
"""
Exercise 2:

2. You are given following list of stocks and their prices in last 3 days,

    Stock	Prices
     info	 [600,630,620]
     ril	 [1430,1490,1567]
     mtl	 [234,180,160]
Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list.
Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks."""

# Solution
stocks = {}
stocks["info"] = [600, 630, 620]
stocks["ril"] = [1430, 1490, 1567]
stocks["mtl"] = [234, 180, 160]

while True:
    ip = input("print, add (submit any other to exit): ")
    if ip == "print":
        for i, j in stocks.items():
            print(i, "==>", j, "==>", "avg: ", round(sum(j)/len(j),2))
    elif ip == "add":
        ip = input("Enter Stock name: ")
        if ip in stocks:
            stocks[ip].append(int(input("Enter price: ")))
        else:
            stocks[ip] = [int(input("Enter Price: "))]
    else:
        break

    