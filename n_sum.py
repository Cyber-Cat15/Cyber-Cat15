def sum():
    a,b=0,0
    while True:
        b=(input("enter a number/enter 'done':"))
        if b=='done' or b=='Done' or b=='DONE':
            break
        else:
            a+=int(b)
    return(a)
print(sum())
