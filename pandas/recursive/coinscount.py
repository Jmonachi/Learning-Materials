ways = []
amount = 4
    
def count_change(change, way):
    global ways
 
    for i in range(len(change)):
        way_new = way + [change[i]]
        if sum(way_new) < amount:
            count_change(change[i:], way_new)
        elif sum(way_new) == amount:
            print(way_new)
            ways.append(way_new)
    
if __name__ == "__main__":
    count_change([2, 1], [])
    print(amount, "can be changed in ", str(len(ways)) +  " ways" )



