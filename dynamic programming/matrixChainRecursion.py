##Problem 2d

def matrixChainMultiParent(n):
    mcmp = {new_list: [] for new_list in range(1,n+1)} ##initialize dict. with []
    print mcmp
    for i in range(1,n+1): # loop through I to N
        if (n==1 or i==1) and mcmp[1]==[]:
            mcmp.update({1:1})
        else:
            if mcmp[i] == []:
                resultPlus = 0
                newI=1
                newN=i
                while newI<newN:
                    resultMul = int(mcmp[newI]) * int(mcmp[newN-newI])
                    newI = newI + 1
                    resultPlus = resultPlus + resultMul
                mcmp.update({i:resultPlus})
                resultPlus=0
            
    print mcmp
    return mcmp[i]

##The equation above has a time function of T(n) = n*n + n + c which products T(n) = O(n*n) time complexity.
##The above statement is achieved by initializing the dictionary for the range 1 to n, this is done to store the values of C(n).
##next we loop though 1 to the input n, this is done to capture the value of i= (1,2, 3, …, n), we then divide the problem into subproblems refencing i as the new n
##value in order to ensure we calculate the values of each C(n) in an order C(1), C(2),C(3)...C(n-1),
##C(n) this approach has a cost of O(n*n).

if __name__ == "__main__":
    value = input("Please enter an number of matrix to parenthesize:\n")
    clientInput1 =  value
    print("Matrix Chain Parentharization, number of parenthesizesation of "+str(clientInput1) +" matrices is " + str(matrixChainMultiParent(clientInput1)))
