# Создать телефонный справочник возможностью добавления записей и чтения. 
# Пользователь также может ввести фамилию, тогда программа должны вывести на экран все записи с этой фамилий. 
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.


with open ('справочник.txt', 'r', encoding='utf-8') as file:
    with open ('справочник1.txt', 'w', encoding='utf-8') as file1:
        text = file.read().splitlines()

        
        surname = text[0]
        name = text[1]
        tel = text[2]
           
      


        def export(surname, name, tel):
            surname3 = surname3.splitlines('Введите фамилию')
            name3 = name3.splitlines('Введите имя')
            tel3 = tel3.splitlines('Введите телефон')
            print(surname3, name3, tel3)


        def import(text)
            list2 = 

        mode = input('Введите режим ввода: 1 - экпорт, 2 - импорт')
            if mode == 1:
                export()
            elif mode == 2:
                import()
            else:
            print('Ввели некорректные данные')