
try: 
    val = float(input("Enter your marks: "))
except ValueError as ve:
    print("You DUMB! You were supposed to enter your marks, i wont be surprised if you fail")
else:
    
    if 0< val > 100:
        print("WOW! Looks like your'e dreaming")
    else :
        if val > 90:
            print("A")
        elif 80 < val < 90 :
            print("B")
        elif 70 < val < 80 :
            print("C")
        elif 60 < val < 70 :
            print("D")
        else :
            print("F")
finally:
    print("Thanks for using the grade calculator")