a = {"a": 1, "b":2, "c":3, "d":4}
b = {"z": 1, "b":2, "e":5, "x":3}
 
t = common_keys = a.keys() & b.keys()  
print(t)
