str1 = "PyNaTive"
def new_word(a):
    print(f"Berilgan ifoda: {a} ")
    lower=[]
    upper=[]
    for x in a:
        if x.islower():
            lower.append(x)
        else:
            upper.append(x)
    sorted_str = ''.join(lower + upper)
    print(sorted_str)

print(new_word(str1))

b=list(str1)
print(b)
print(''.join(b))