pos = -1

def search(list,n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i+=1
    return False

list = [1,2,3,4,5,6]
n = 5

if search(list, n):
    print('found at: ', pos+1)
else:
    print('not found')
