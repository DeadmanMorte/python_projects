def max_num(arg1,arg2,arg3):
    return max(arg1,arg2,arg3)

print(max_num(22,5,13))

def mult_list(list):
    if len(list) == 0:
        return 0
    else:
        mult = list[0]
        for i in list[1:]:
            mult = mult * i
    return mult

print(mult_list([1,3,5,2]))

def rev_string(string):
    return string[::-1]

print(rev_string('Tacocat is tacocat'))

def num_within(x,a,b):
    if x > a and x < b:
        return True
    else:
        return False

print(num_within(9,1,2)) 
print(num_within(2,1,5)) 

triangle = [[1],[1,1]]

def pascal(n):
    if n < 1:
        print('Not enough rows')
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row=[]
            row_prev = triangle[row_number - 1]
            length = len(row_prev) + 1
            for i in range(length):
                if i==0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1][i-1]+triangle[row_number - 1][i])
                else:
                    row.append(1)   
            triangle.append(row)
            row_number += 1     
        for row in triangle:
            print(row)

pascal(5)
pascal(15)