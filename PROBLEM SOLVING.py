def Upper_StartEnd_char(string):

    words = string.split(" ")
    lists= []
    for i in words:
        
        wording = ""
        for a,b in enumerate(i):
            if a==0 or a == len(i)-1:
                wording+=b.upper()
            else:
                wording+=b
        lists.append(wording)

    print(" ".join(lists))

# Upper_StartEnd_char("prep")

def Frequency_of_string(string):

    dicti = {}
    for i in string:
        if i in dicti:
            dicti[i]+=1
        else:
            dicti[i]=1
    print(dicti)

# Frequency_of_string("YOLO LIFE")

def Non_repeating_chr_string(string):

    Non_repeates = []
    for i in string:
        if string.count(i) == 1:
            Non_repeates.append(i)

    print(Non_repeates)

# Non_repeating_chr_string("YOLO LIFE")

def WildCharacter_Second(str1,str2):
    
    if len(str1)!=len(str2):
        return(False)
    else:
        chance:int = 0
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                chance+=1
        return(True if chance<=1 else False)
    
# print(WildCharacter_Second("Praveen","Pr@veen"))

def Reverse_List(num:list[int])->list[int]:

    start,end = 0,len(num)-1    
    while start<end:
        num[start],num[end] = num[end], num[start]
        start+=1
        end-=1

# Reverse_List([1,2,3,4,5])

def Fasc_Sdesc(array):

    half = len(array)//2
    first = array[:half]
    first.sort()
    second = array[half:]
    second.sort()
    first.extend(second[::-1])
    print(first)
    
# Fasc_Sdesc([1,2,3,4,5])

def Longest_Palindrome(array):
    
    palindromes = []
    for i in array:
        if str(i)==str(i)[::-1]:
            palindromes.append([i,len(str(i))])
    print(max(palindromes,key=lambda x: x[1]))
    
# Longest_Palindrome([1, 202, 454, 909901, 162])

def Symmetric_Elements(array):

    symmetrics = []
    for i in array:
        if i[::-1] in array:
            symmetrics.append(i)
            array.remove(i)
    print(symmetrics)

# Symmetric_Elements([[10,20], [50,60], [20,10], [40,30], [90, 100], [1, 9],[100, 90]])

def Find_Rank(array):

    sorted_arr = sorted(array)
    result = []
    for i in array:
        result.append(sorted_arr.index(i)+1)
    print(result)

# Find_Rank([100, 2, 70, 12 , 90])

def rotate_one_pos(array):
    index = 2
    print(array[index:]+array[:index])

# rotate_one_pos([10, 20, 30, 40, 50])

def Valid_brackets(string):

    brackets = {
        '[':']',
        '{':'}',
        '(':')'
    }

    stack = []
    for i in string:

        if i in brackets.keys():
            stack.append(i)
        
        elif i in brackets.values() and len(stack)>0:
            if brackets[stack.pop()] != i :
                return False
        
        elif i in brackets.values() and len(stack)==0:
            return False
        
    return (True if len(stack)==0 else False)

# print(Valid_brackets("(()())"))

def Fibonacci_Series(num:int):
    
    a,b=0,1
    print(a)
    for i in range(num):
        a,b=b,b+a
        print(a)
    pass

# Fibonacci_Series(5)

def Combinations(string):

    if len(string)==1:
        return [string]

    elif len(string)>1:

        Comb = []
        for i in range(len(string)):
            
            firstChar = string[i]
            RemainingChars = string[:i] + string[i+1:]

            for j in Combinations(RemainingChars):

                Comb.append(firstChar + j)

        return Comb


    pass

# print(Combinations("ABC"))

def sum_of_abs_diff(arr):

    output_list = []
    for i in arr:

        inner_list = []
        for j in arr:
            inner_list.append(abs(i-j))
        output_list.append(sum(inner_list))
    return output_list

# print(sum_of_abs_diff([1,4,6,8,10]))

def Merge_two_sorted_arr(arr1,arr2):

    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    newlist = sorted(arr1 + arr2)
    return newlist[:len_arr1], newlist[len_arr1:]

# print(Merge_two_sorted_arr([1,5,9,10,15,20],[2,3,8,13]))

def Find_median(arr):
    
    if len(arr)%2 ==0:
        
        n = len(arr)//2
        result = (arr[n-1]+arr[n])//2
        return result 

    elif len(arr)%2==1:
        return arr[len(arr)//2]

# print(Find_median([ 1,2,3,4,5,6,7]))

def reverseString(string:str):

    result = ""
    for i in string:
        result = i+result
    return result

# print(reverseString("Python"))

def factorial1(num:int):
    
    value = 1
    for i in range(1, num+1):
        value*=i
    return value

# print(factorial1(5))

def factorial2(num:int):
    
    value = 1
    while num>1:
        value = value* num
        num = num-1
    return value
    

print(factorial2(0))