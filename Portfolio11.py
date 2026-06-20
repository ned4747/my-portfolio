from time import sleep
from turtle import*

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
    
    def intro(self):
        speed(0)
        hideturtle()
        screen = Screen()
        screen.bgcolor("#1a1a2e")
        color("cyan")
        fillcolor("#3f354a")
        pensize(1)
        penup()
        goto(-150,-80)
        pendown()
        begin_fill()
        for i in range(4):
            forward(200)
            left(90)
        end_fill()
        begin_fill()
        forward(200)
        left(35)
        forward(70)
        left(55)
        forward(200)
        left(90)
        forward(200)
        left(35)
        forward(69)
        end_fill()
        left(145)
        forward(200)
        left(35)
        forward(70)
        left(180)
        forward(70)
        left(55)
        forward(200)
        penup()
        goto(-125, 60)
        pendown()
        speed(5)
        color("white")
        pensize(3)
        left(65)
        forward(75)
        right(128)
        forward(75)
        penup()
        goto(25, -5)
        pendown()
        right(26.8)
        forward(76)
        penup()
        goto(-25,-145)
        pendown()
        write("MY PORTFOLIO", align="center", font=("Arial", 30, "bold"))

        sleep(1)
        
        bye()

        self.hello()

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
            else:
                print("\nОшибка! Такого раздела не существует.")



if __name__ == "__main__":
    app = Portfolio()
    app.intro()
