def number_game(x,y):
    if x > y:
        return [n for n in range(y,x) if n%2==0]
    elif y==x:
        return []
    else:
        return [n for n in range(x,y) if n%2!=0]
print(number_game(12,2))
     
print(number_game(180,200))

print(number_game(20,0))