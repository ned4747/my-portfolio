from time import*
class Portfolio:
    def __init__(self):
        pass            #Тут скоро будут списки файлов

    def hello(self):
        print("="*35)
        print("Добро пожаловать в мое порфолио!")
        self.choicement()

    def menu(self):
        print("="*35)
        print("Все разделы:")
        print("\n1. О себе")
        print("2. Моя цель")
        print("3. Как я пришел в IT")
        print("4. Мой ментор")
        print("5. Мой прогресс (Точка A → Точка Б)")
        print("6. Хобби и интересы")
        print("7. Мои лучшие работы")
        print("8. Ссылка на GitHub")
        print("0. Выход")
        print("="*35)

    def choicement(self):
        while True:
            self.menu()
            choice_menu = input("\nВыберите один из разделов для просмотра (0-8)")
            
            if choice_menu == "0":
                while True:    
                    exit = input("\nВы уверены что хотите выйти?")
                    if exit == "Да" or exit == "да":
                        print("Спасибо за просмотр! До встречи!")
                        sleep(3)
                        exit() #программа закрывается спустя 3 сек.
                    elif exit == "Нет" or exit == "нет":
                        break
                    else:
                        print("\nКоманда неизвестна. Сделайте выбор между 'да' и 'нет'.")
            elif choice_menu in numbers: #Это будущий список с файлами
                print(numbers[choice])
                choice = input("\n(Чтобы выйти в меню нажмите Enter)")
                self.choicement()
            else:
                print("\nОшибка! Такого")

if __name__ == "__main__":
    app = Portfolio()
    app.hello()