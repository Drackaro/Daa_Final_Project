from Code import subset_equality
from Dp_Solution import subset_equality_dp
import random

def CheckSolution(original: list, array1: list, array2: list):
    if len(array1) + len(array2) != len(original):
        return False
    
    if sum(array1) != sum(array2):
        return False
    
    checkRef = []

    for i in range(len(array1)):
        checkRef.append(array1[i])
    for i in range(len(array2)):
        checkRef.append(array2[i])

    checkRef.sort()
    original.sort()

    for i in range(len(original)):
        if checkRef[i] != original[i]:
            return False
    return True

def Test(array, possible = 2):
    success, array1, array2 = subset_equality(array)

    if possible == 0 and not success:
        return True

    if possible == 1 and success:
        return CheckSolution(array, array1, array2),
    
    if possible == 2:
        if success:
            return CheckSolution(array, array1, array2)
        
        else:
            return True

def Defaultcases():
    testCases = [
        ([1,5,11,5], 1), #Test1
        ([1,2,3,5], 0), #Test2
        ([], 1),  #Test3
        ([10], 0), #Test4
        ([4,3,1,20,10,10,6,5,1], 1), #Test5
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,14], 1), #Test6
        ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 1), #Test7
        ([4,8,15,16,23,42,50,60,70,81], 0), #Test8
        ([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216], 0), #Test9
        ([3, 7, 12, 18, 25, 30, 2, 9, 14, 20, 27, 33, 4, 10, 15, 21, 28, 34, 5, 11, 16, 22, 29, 35, 6], 1) #Test10
    ]

    for test in testCases:
        if Test(test[0],test[1]):
            print("Correct")
        else:
            print("Incorrect")

def generator(size):
    arr=[]
    for _ in range(size):
        arr.append(random.randint(1,100))
    return arr

def RandomCase(size):
    arr=generator(size)

    s, c1, c2 = subset_equality(arr)

    if not s:
        print("No tiene solución")
        print(arr)
        print(f"Suma: {sum(arr)}")

    if s:
        if not CheckSolution(arr, c1, c2):
            print("Respuesta incorrecta devuelta")
        else:
            print("La solución es la siguiente:")
            print(c1)
            print(f"Suma de este conjunto: {sum(c1)}")
            print(c2)
            print(f"Suma de este conjunto: {sum(c2)}")

#Defaultcases()
#RandomCase(10)