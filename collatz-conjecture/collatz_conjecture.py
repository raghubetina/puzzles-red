def steps(x):
    while x != 1:
        if x % 2 > 0:
             x =((3 * x) + 1)
             list_.append(x)
        else:
            x = (x / 2)
            list_.append(x)
    return list_


print('Please enter a number: ', end='')

while True:
    try:
        x = int(input())
        list_ = [x]
        break
    except ValueError:
        print('Invaid selection, try again: ', end='')


l = steps(x)

print('\nList:', l, sep=' ')
print('Number of steps required:', len(l) - 1)