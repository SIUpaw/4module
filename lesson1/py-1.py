# def strcount(s):
#     for sym in set(s): #set(создает массив- в массиве есть только уникальные значения)
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)

# strcount("abacabv")

def strcount(s):
    dct = {}
    for sym in s:
        dct[sym] = dct.get(sym, 0) + 1

    for key, value in dct.items():
        print(key, value)


strcount('aaabcd')

