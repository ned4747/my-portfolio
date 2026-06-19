from random import*
vybor = ["камень", "ножницы", "бумага"]
bot_score = 0
player_score = 0
pravila = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}
print("Играем в камень, ножницы, бумага. \nПравила: Камень бьет ножницы, ножницы бьют бумагу, бумага бьет камень")
def main():
    player = input("Сделай выбор: ")
    while player not in vybor:
        print("Ошибка, выбери одно из трех.")
        player = input("Сделай выбор: ")
    return player


def determine_winner(player, computer):
    global player_score, bot_score
    if pravila[player] == computer:
        player_score += 1
        print(f"Бот выбрал {computer}. Ты выиграл!\nБот: {bot_score}\nТы: {player_score}")
    elif computer == player:
        print(f"Бот выбрал {computer}. Ничья\nБот: {bot_score}\nТы: {player_score}")
    else:
        bot_score += 1
        print(f"Бот выбрал {computer}. Ты проиграл\nБот: {bot_score}\nТы: {player_score}")
              
def get_computer_choice():
    computer = choice(vybor)
    return computer

while player_score < 3 and bot_score < 3:
    player_choice = main()
    computer_choice = get_computer_choice()
    determine_winner(player_choice, computer_choice)

if player_score == 3:
    print(f"Ты окончательно выиграл!\nБот: {bot_score}\nТы: {player_score}")
else:
    print(f"ТЫ окончательно проиграл.\nБот: {bot_score}\nТы: {player_score}")