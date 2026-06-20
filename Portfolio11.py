from time import*

class Portfolio:
    def __init__(self):
        global files
        files = {
            "1": "about_me.txt",
            "2": "goal.txt",
            "3": "history.txt",
            "4": "mentor.txt",
            "5": "progress.txt",
            "6": "hobbies.txt",
            "7": "projects.txt",
            "8": "github.txt"
        }       #Тут скоро будут списки файлов

    def read_file(self, name_file):
        with open(name_file, "r", encoding="utf-8") as myfile:
            content = myfile.read()
            return content

    def hello(self):
        print("="*35)
        print("Добро пожаловать в мое порфтолио!")
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
            choice_menu = input("\nВыберите один из разделов для просмотра (0-8): ")
            
            if choice_menu == "0":
                while True:    
                    exit_from = input("\nВы уверены что хотите выйти?: ")
                    if exit_from == "Да" or exit_from == "да":
                        print("Спасибо за просмотр! До встречи!")
                        sleep(3)
                        exit() #программа закрывается спустя 3 сек.
                    elif exit_from == "Нет" or exit_from == "нет":
                        break
                    else:
                        print("\nКоманда неизвестна. Сделайте выбор между 'да' и 'нет'.")
            elif choice_menu in files: #Это будущий список с файлами
                filename = files[choice_menu]
                text = self.read_file(filename)
                print(f'Вы выбрали {choice_menu}.')
                print("="*40)
                print(text)
                print("="*40)
                input("\n(Чтобы выйти в меню нажмите Enter)")
                self.choicement()
            else:
                print("\nОшибка! Такого раздела не существует.")



if __name__ == "__main__":
    app = Portfolio()
    app.hello()
