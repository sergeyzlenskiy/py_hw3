boys_input = input("Введите имена мальчиков через запятую: ")
girls_input = input("Введите имена девочек через запятую: ")

boys = [boy.strip() for boy in boys_input.split(',')]
girls = [girl.strip() for girl in girls_input.split(',')]

if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары!")
else:
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)
    
    print("Идеальные пары:")
    for boy, girl in zip(boys_sorted, girls_sorted):
        print(f"{boy} и {girl}")
