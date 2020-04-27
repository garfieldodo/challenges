people = int(input("how many people do you want at your party?: "))
if people < 10:
    for i in range (people):
        name = (input("who is going?: "))
        print (name, "has been invited")
else:
    print ("too many people")