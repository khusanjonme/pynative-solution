str1 = "P@#yn26at^&i5ve"
def find_number_letter_symbol(a):
    print("Berilgan ifoda:", a)
    letter_count=0
    number_count=0
    symbol_count=0
    for x in a:
        if x.isalpha():
            letter_count+=1
        elif x.isdigit():
            number_count+=1
        else:
            symbol_count+=1
    print(f"Berilgan ifodada {letter_count}ta harf. {number_count}ta raqam, {symbol_count}ta simbol bor.")
find_number_letter_symbol(str1)
