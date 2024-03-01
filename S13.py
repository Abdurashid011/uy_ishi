def get_summa(lst):

    new_lst = sorted(lst, key=lambda x : sum([int(digit) for digit in str(x)]))

    return new_lst

lst = input("Sonlarni kiriting: ").split()
lst = [int(num) for num in lst]

print(get_summa(lst))