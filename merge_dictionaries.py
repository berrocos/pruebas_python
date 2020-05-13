def Merge(dict1,dict2):
    res = {**dict1,**dict2}

    return res



dict1={'a':10, 'b':8}
dict2={'d':11,'e':12}
dict3=Merge(dict1,dict2)

print(dict3)

    