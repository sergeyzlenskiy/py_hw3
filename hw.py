word = input("Введите слово: ")

length = len(word)

if length % 2 != 0:
    middle_index = length // 2
    print(word[middle_index])
else:
    middle_index1 = (length // 2) - 1
    middle_index2 = length // 2
    print(word[middle_index1:middle_index2 + 1])