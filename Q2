def version_check(x1,x2):
    #convert versions to numbers
    x1 = int("".join(x1.split(".")))
    x2 = int("".join(x2.split(".")))
    
    if x1<0 or x2<0:
        raise Exception("An exception occured.Please enter non-negative integers.") 
        
    if x1 == x2:
        print("Equal")
    elif x1 > x2:
        print("Greater")
    else:
        print("Less")
        


if __name__ == '__main__':
    try:
        x1 = raw_input("Please enter the first version.")
        x2 = raw_input("Please enter the second version")
        version_check(x1,x2)
    except:
        print("An exception occured.Please enter non-negative integers.")
    
