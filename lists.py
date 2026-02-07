#LIST

# Imagine you are going to a grocery store and you need to buy some items. You can create a list of items you need to buy.
grocery_list = ["milk", "eggs", "bread", "butter"]

# We can access items in the list using their index. Remember that indexing starts at 0.
print(grocery_list[0])  # Output: milk

# We can also add items to the list using the append() method.
grocery_list.append("cheese")

# We can remove items from the list using the remove() method.
grocery_list.remove("eggs")

# We can change items in the list by assigning a new value to a specific index.
grocery_list[1] = "orange juice"
# Remember! We cannot do this with a string because strings are immutable, meaning they cannot be changed after they are created.


# we can inset items at a specific index using the insert() method.
grocery_list.insert(1, "yogurt")

# We can also find the length of the list using the len() function.
print(len(grocery_list))  # Output: 5

# We can concatenate two lists using the + operator.
fruits = ["apple", "banana", "orange"]
combined_list = grocery_list + fruits

# There are many other methods and operations we can perform on lists, such as sorting, slicing, and more. Lists are a fundamental data structure in Python and are very versatile for storing and manipulating collections of items.l



"""Exercise: Lists
1.Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,
    A. In Feb, how many dollars you spent extra compare to January?
    B. Find out your total expense in first quarter (first three months) of the year.
    C. Find out if you spent exactly 2000 dollars in any month
    D. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    E. You returned an item that you bought in a month of April and
       got a refund of 200$. Make a correction to your monthly expense list
       based on this
2. You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

    A. Length of the list
    B. Add 'black panther' at the end of this list
    C. You realize that you need to add 'black panther' after 'hulk',
      so remove it from the list first and then add it after 'hulk'
    D. Now you don't like thor and hulk because they get angry easily :)
      So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
      Do that with one line of code.
    E. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)"""
    
    
# Solution:
# 1.
expenses = [2200, 2350, 2600, 2130, 2190]
# A
feb_extrea = expenses[1] - expenses[0]
# B
q1 = expenses[0] + expenses[1] + expenses[3]
# C
for i in expenses:
    if i == 2000:
        print("Excatly 2000")
# D
expenses.append(1980)
# E
expenses[3] = expenses[3] - 200

# 2.
heros=['spider man','thor','hulk','iron man','captain america']
#A
print(len(heros))
#B
heros.append("black panther")
#C
heros.remove('black panther')
heros.insert(2, 'black panther')
#D
heros[1:3] = ['doctor strange']
#E
heros.sort()


