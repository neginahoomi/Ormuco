     
def check_overlap(x1, x2, x3, x4):
    #First, we make sure that x1<x2 and X3<x4
    if x1 > x2:
        x1, x2 = x2, x1
        
    if x3 > x4: 
        x3, x4 = x4, x3
    
    if (x3 > x1 and x3 < x2) or (x4 > x1 and x4 < x2):
        return True
    else:
        return False
    
    

if __name__ == '__main__':
    
    try:
        X1, X2 = input ("Please enter the coordinates for line one.")
        X3, X4 = input ("Please enter the coordinates for line two")
        result = check_overlap(X1,X2,X3,X4)
        print result
    
    except:
        print("An exception has occured. Strings and Characters are not accepted.")
