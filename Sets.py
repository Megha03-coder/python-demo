set={'a',1,3,4,"megha"} 
set2={1,2,3,4,5,6,7}      # collection of unordered items , immutable.

print(set)

# Methods of Set.

set.add(2)     # add element in the set.
print(set)

set.remove(2)  # remove the element.
print(set)

set.pop()   # delete random items from the set

set.clear()  # empty the set
print(set)

a={1,2,3,4}
b={2,7,8,9}
print(a.union(b))    # combine both set and return new set.

print(a.intersection(b))  # return comman values.