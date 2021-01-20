def gender(name, gender):
    if(gender == 'M'):
        print("Mr.", name)
    elif(gender =='F'):

        print("Ms.", name)
    else:
        print("Hello ", name)
gender(input("Enter name"), input("Enter gender"))
