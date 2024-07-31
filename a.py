def a(k,a):
    if len([i for i in a if i >= 0]) >= k:
        return 'NO'
    else:
        return 'YES'
    
b = list(map(int,'26 94 -95 34 67 -97 -17 52 1 86'.split(' ')))
print(a(7,b))

# case 6
# a = input()
# print(list(map(int,a.split(' '))))

def angryProfessor(k, a):
    # Write your code here
    onTime=0
    for arrivalTime in a:
        if arrivalTime<=0:
            onTime += 1
    if onTime >= k:
        return "NO"
    else:
        return "YES"
b = list(map(int,'26 94 -95 34 67 -97 -17 52 0 86'.split(' ')))
print(angryProfessor(7,b))


def a(k, a):
    if len([i for i in a if i <= 0]) >= k:
        return 'NO'
    else:
        return 'YES'
    
b = list(map(int, '26 94 -95 34 67 -97 -17 52 0 86'.split(' ')))
print(a(7, b))

#cc