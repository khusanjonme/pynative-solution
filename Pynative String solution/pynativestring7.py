s1 = "Yn"
s2 = "PYnative"
s3 = "Ynf"
s4 = "PYnative"
def string_balance_test(a,b):
    flag=True
    for i in a:
        if i in b:
            continue
        else:
            flag=False
    return flag
print(string_balance_test(s1,s2))
print(string_balance_test(s3,s4))