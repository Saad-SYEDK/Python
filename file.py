# File Handling
# Open a file for writing
file = open('example.txt', 'w')
# Write some text to the file
file.write('Hello, World!\n')
file.write('This is a file handling example.\n')
# Close the file
file.close()

# Open the file for reading
file = open('example.txt', 'r')
# Read the contents of the file
content = file.read()
print(content)
# Close the file
file.close()

# Using 'with' statement for better file handling
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# Append to the file
with open('example.txt', 'a') as file:
    file.write('Appending a new line to the file.\n')
# Read the updated file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Handling file exceptions
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('The file does not exist.')

# self learn more about line by line reading, modes, cv flies, etc.

"""Exercise:
1. poem.txt contains famous poem "Road not taken" by poet Robert Frost.
    You have to read this file in your python program and find out words with maximum occurance.


2. stocks.csv contains stock price, earnings per share and book value.
    You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
    pe ratio = price / earnings per share
    price to book ratio = price / book value
    
    Your input format (stocks.csv) is,

Company Name	Price	Earnings Per Share	    Book Value
    Reliance	1467	            66	            653
    Tata Steel	391	                89	            572

Output.csv should look like this,

Company Name	PE Ratio	PB Ratio
    Reliance	22.23   	2.25
    Tata Steel	4.39    	0.68  
"""

# Soulution
# 1.
poem_count = {}
with open("poem.txt" , 'r') as poem:

    for line in poem:
        words = line.split(' ')
        for word in words:
            if word in poem_count:
                poem_count[word] += 1
            else:
                poem_count[word] = 1

max_count = -1
for _, j in poem_count.items():
    if j >= max_count:
        max_count = j

for i, j in poem_count.items():
    if j == max_count:
        max_word = i
        print("Most frequent word(s):", max_word, ", frequency:", max_count)

# 2.
with open("stocks.csv", "r") as cv_file , open("output.csv", 'w') as op:
    op.write("Company Name, PE Ratio, PB Ratio\n")
    next(cv_file) 
    
    for line in cv_file:
        fields = line.split(',')
        s_name = fields[0]
        s_price = float(fields[1])
        s_eps = float(fields[2])
        s_bv = float(fields[3])
        
        pe_ratio = round(s_price / s_eps, 2) 
        pb_ratio = round(s_price / s_bv, 2)
        
        op.write(f"{s_name},{pe_ratio},{pb_ratio}\n")

