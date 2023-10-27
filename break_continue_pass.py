av = 5
x= int(input("how many candies you want?:"))

i=1
while i<=x:
    if i>av:
        print('out of stock')
        break
    print ("candy", i)
    i+=1
print("bye")
