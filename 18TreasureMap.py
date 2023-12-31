import random, time
list1 = [ " ", " ", " " ]
list2 = [ " ", " ", " " ]
list3 = [ " ", " ", " " ]

list = [ list1, list2, list3 ]

loc = input("Enter the location of your treasure : ")

alphb = []

for i in range( 97, 123 ) :
    alphb.append(chr(i))

ind =alphb.index(loc[0])

list[ind][int(loc[1])-1] = "X"

print(f"{list1}\n{list2}\n{list3}")


