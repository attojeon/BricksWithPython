'''
C언어와 Python의 list(배열) 처리에 차이가 있음. 사용에 주의해야할 필요가 있다.
'''
# python의 방식으로 배열/list를 처리하는 법 1
print('python list prcessing #1')
array = []

for i in range(3):
    line = []
    for j in range(3):
        line.append(0)
    array.append(line)

print(array)

array[1][1] = 1
print(array)

# C언어 방식으로 배열/list를 처리하는 법(아래와 같이 문제가 있음!!!)
print('')
print('C lang list prcessing #1')
array_c = [[0]*3]*3
print(array_c)
array_c[1][1] = 1
print(array_c)


# python의 방식으로 배열/list를 처리하는 법 2
print('python list prcessing #2')

array_n = [ [ 0 for j in range(3)] for i in range(3) ]
print(array_n)
array_n[1][1] = 1
print(array_n)

# python의 방식으로 배열/list를 처리하는 법 3
print('python list prcessing #3')
array_m = [ [0]*3 for i in range(3)]
print(array_m)
array_m[1][1] = 1
print(array_m)