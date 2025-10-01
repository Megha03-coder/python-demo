dic={
    1:"megha",
    2:"chauhan"
}
print(dic)

# Methods of Dictionary.

print(dic.keys())      # return all keys in list format.

print(dic.__len__())    # return total no. of keys

print(dic.values())      # return all values

print(dic.items())      # return pairs in the tuple form

print(dic.get(2))       # return the vlaue of specified key.

print(dic.update({3:"hello"}))     # add key/value to the dictionary.
print(dic)