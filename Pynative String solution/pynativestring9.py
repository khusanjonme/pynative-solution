str1 = "PYnative29@#8496"
def sum_number_average(word):
    sum=0
    count=0
    for i in word:
        if i.isdigit():
            sum=sum+int(i)
            count=count+int(1)
    average=sum/count
    print(f"Berilgan ifoda: {word}")
    print(f"Berilgan ifodadagi raqamlar yig'indisi: {sum}"
          f" Sonlar o'rtachasi: {average}")
sum_number_average(str1)