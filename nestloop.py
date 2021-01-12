for x in range(3):
    print("Iteration" + str(x+1) + "of outer loop")
    for y in range(2):
        print(y+1)
        print("Out of inner loop")
    print("Out of outer loop")
