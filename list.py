a=[1,2,3,4,"megha"]
print(a)
print(type(a))

print(a[3])    # print element at index 3


a[3]="chauhan"     # change the value at index 3 with "chauhan"  
print(a)

# List Methods.
list=[1,2,3,4]
list.append(5)     # add element in the end of the list.  [1,2,3,4,5]
print(list)

list.sort(reverse=True)     # return the list in descending order.  [5,4,3,2,1]
print(list)

list.reverse()
print(list)                 # reverse the list    [1,2,3,4,5]


list.insert(5,6)       #insert the element at particular index.  list.insert(index,element)
print(list)

list.remove(1)      # remove the first occurence of element 1    [2,3,4,5,6]
print(list)

list.pop(4)           # delete the element from particular index  - list.pop(index)
print(list)



