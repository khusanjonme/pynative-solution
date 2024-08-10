

str2 = "JaSonAy"
l2=len(str2)
mid=int(l2/2)
res1=str2[mid-1]+str2[mid]+str2[mid+1]
print(res1)

def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")