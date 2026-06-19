import tkinter as tk
import json

password = "krutoi parol"
my_stats = {
    "brawl_val": "21200",
    "so2_val": "Elite"
}


try:
    with open("databasekrutoii.txt", "r", encoding="utf-8") as f:
        full_data = json.load(f)
        my_stats = full_data["stats"]
except:
    print("Файл не найден, используем стандартные статы")

def save_data():
    data_to_save = {"stats": my_stats}
    with open("databasekrutoii.txt", "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)

#бравл старс
def change_stats1():
    def close_changement_internal():
        global my_stats
        my_stats["brawl_val"] = entry1.get()
        brawl = my_stats.get('brawl_val', '0')
        so2 = my_stats.get('so2_val', 'Elite')
        games_list.config(text=f"Brawl Stars: {brawl}\nStandoff 2: {so2}")
        label2.config(text="Значение успешно изменено")
        changement.after(500, changement.destroy)
        
    changement = tk.Toplevel()
    changement.title("Изменение данных")
    changement.geometry("300x300")

    label2 = tk.Label(changement, text="Введите новое значение:", font=("Arial", 12))
    label2.pack()

    igra = tk.Label(changement, text="Brawl Stars:", font=("Arial", 10))
    igra.place(x=5, y=100)

    entry1 = tk.Entry(changement)
    entry1.place(x=120, y=100)

    butt3 = tk.Button(changement, text="Подтвердить", font=("Arial", 10), command=close_changement_internal)
    butt3.place(x=150, y=150)

#стандофф
def change_stats2():
    def close_changement_internal():
        global my_stats
        my_stats["so2_val"] = entry2.get()
    
        brawl = my_stats.get('brawl_val', '0')
        so2 = my_stats.get('so2_val', 'Elite')
        games_list.config(text=f"Brawl Stars: {brawl}\nStandoff 2: {so2}")
        label2.config(text="Значение успешно изменено")
        changement.after(500, changement.destroy)
        
    changement = tk.Toplevel()
    changement.title("Изменение данных")
    changement.geometry("300x300")

    label2 = tk.Label(changement, text="Введите новое значение:", font=("Arial", 12))
    label2.pack()

    igra = tk.Label(changement, text="Standoff 2:", font=("Arial", 10))
    igra.place(x=5, y=100)

    entry2 = tk.Entry(changement)
    entry2.place(x=120, y=100)

    butt3 = tk.Button(changement, text="Подтвердить", font=("Arial", 10), command=close_changement_internal)
    butt3.place(x=150, y=150)

def open_main_menu():
    global my_stats, games_list 
    
    menu = tk.Tk()
    menu.title("Главное меню")
    menu.geometry("500x500")
    
    label1 = tk.Label(menu, text="ТВОИ ИГРЫ:", font=("Arial", 18, "bold"))
    label1.pack(pady=20)
    
    stats_text = f"Brawl Stars: {my_stats.get('brawl_val', '0')}\nStandoff 2: {my_stats.get('so2_val', '0')}"
    
    games_list = tk.Label(menu, text=stats_text, font=("Arial", 14))
    games_list.place(x=10, y=80)

    butt = tk.Button(menu, text="Изменить", font=("Arial", 8), command=change_stats1)
    butt.place(x=250, y=80)
    
    butt1 = tk.Button(menu, text="Изменить", font=("Arial", 8), command=change_stats2)
    butt1.place(x=250, y=102)
    
    butt4 = tk.Button(menu, text="Сохранить и выйти", font=("Arial", 8), command=lambda: [save_data(), menu.destroy()])
    butt4.place(x=300, y=102)
    
    menu.mainloop()

def check_password():
    parol = entry.get()
    if parol == password:
        label.config(text="Верный код! Майонез реально!", fg="green")
        root.after(1000, lambda: [root.destroy(), open_main_menu()])
    else:
        label.config(text="Код невeрный", fg="red")

root = tk.Tk()
root.title("Проверка окно :D")
root.geometry("300x200")

label = tk.Label(root, text="Введи секретный ключ", font=("Arial", 15))
label.pack(pady=25)

entry = tk.Entry(root, show="*")
entry.pack()

button = tk.Button(root, text="Проверить", font=("Arial", 12), command=check_password)
button.pack()

root.mainloop()