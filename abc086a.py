# atcoder begginer's selection ABC086A

'''
s = input()
x = s.split()
a = int(x[0])
b = int(x[1])
'''
a,b = map(int, input().split())
if a*b%2 == 0:
    print('Even')
else:
    print('Odd')