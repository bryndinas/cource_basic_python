raiting_list = [22,6,5]
while True:
    user_input = input("Введите новый рейтинг или 'q' для выхода \n")
    try:
        new_reting = abs(int(user_input))
    except ValueError as error:
        if user_input.lower() == "'q'":
            print('До свидания')
            break
        print('Ошибка ввода')
        continue
    new_reting_count = raiting_list.count(new_reting)
    if not new_reting_count:
        if new_reting > raiting_list[0]:
            raiting_list.insert(0,new_reting)
        elif new_reting<raiting_list[-1]:
            raiting_list.append(new_reting)
        else:
            for idx, itn in enumerate (raiting_list):
                if itn < new_reting:
                    raiting_list.insert(idx,new_reting)
                    break
    else:
        end_idx = raiting_list.index(new_reting)+new_reting_count
        raiting_list.insert(end_idx, new_reting)
    print(raiting_list)

