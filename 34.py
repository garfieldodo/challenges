print ("""1) square
2) triangle""")
num = (input("enter a number: "))
if num == ("1"):
    width = int(input("enter it's width: "))
    areasquare = width**2
    print ("your square's area is ", areasquare, "cm squared.")
elif num == ("2"):
    base = int(input("enter your triangle's base: "))
    height = int(input ("now enter it's height: "))
    areatriangle = base * height / 2
    print ("your triangle's area is ", areatriangle, "cm squared")
else:
    print ("error")