def number_game(x,y):
  if x < y:
         return [r for r in range(y, x) if r % 2 == 0]
  elif y == x:
       return []
  else:
      return [r for r in range(x, y) if r % 2 != 0]

print(number_game(2,10))