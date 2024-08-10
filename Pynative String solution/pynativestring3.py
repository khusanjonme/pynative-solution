s1 = "America"
s2 = "Japan"
def new_word(a,b):
    print(f"Berilgan ifodalar: {a} va {b}")
    la=len(a)
    lb=len(b)
    c=a[0]+b[0]+a[int(la/2)]+b[int(lb/2)]+a[-1]+b[-1]
    result = f"Natija: {c}"
    return result
print(new_word(s1,s2))