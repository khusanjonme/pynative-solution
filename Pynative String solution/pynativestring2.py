s1 = "Ault"
s2 = "Kelly"
def middle_joylash(a,b):
    print(f"Berilgan ifodalar: {a} {b}")
    l=int(len(a))
    c=a[:int(l/2)]+b+a[int(l/2):]
    print(f"Natija: {c}")

middle_joylash(s1,s2)

