import random

class Player:
    def __init__(self, name, health=100, attack=10):
        self.name = name
        self.vida = health
        self.attack = attack
    
    def is_alive(self):
        return self.vida > 0
    
    def take_damage(self, damage):
        self.vida -= damage
    
    def attack_enemy(self, enemy):
        damage_dealt = random.randint(0, self.attack)
        enemy.take_damage(damage_dealt)
        print(f"{self.name} attacks {enemy.name} for {damage_dealt} damage!")

class Dragon:
    def __init__(self, name, health=50, attack=20):
        self.name = name
        self.health = health
        self.attack = attack
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
    
    def attack_player(self, player):
        damage_dealt = random.randint(0, self.attack)
        player.take_damage(damage_dealt)
        print(f"{self.name} attacks {player.name} for {damage_dealt} damage!")

def fight_with_dragon(player, dragon):
    print("Você está enfrentando um dragão! O que você deseja fazer?")
    print("1. Atacar o dragão")
    print("2. Tentar esquivar do ataque do dragão")

    choice = input("Escolha seu próximo passo: ")

    if choice == "1":
        player.attack_enemy(dragon)
        dragon.attack_player(player)

        if player.is_alive() and dragon.is_alive():
            fight_with_dragon(player, dragon)
        elif player.is_alive():
            print("Parabéns! Você derrotou o dragão!")
        else:
            print("Você foi derrotado pelo dragão. Tente novamente!")
    elif choice == "2":
        lucky_roll = random.randint(1, 10)
        if lucky_roll > 7:
            print("Você conseguiu desviar do ataque de Quetzalcóatl!")
            print("Você aproveita a chance para atacar o dragão Quetzalcóatl!")
            player.attack_enemy(dragon)
            if dragon.is_alive():
                print("O dragão contra-ataca!")
                dragon.attack_player(player)
                if player.is_alive():
                    fight_with_dragon(player, dragon)
                else:
                    print("Você foi derrotado por Quetzalcóatl o Soberando dos ventos. Tente novamente!")
            else:
                print("Parabéns! Você derrotou Quetzalcóatl,  e pegou o Tesouro!")
        else:
            print("Você tenta esquivar do ataque de Quetzalcóatl, mas falha!")
            print("Você é atingido pelo ataque de Quetzalcóatl e morre.")
    else:
        print("Escolha inválida!")
        fight_with_dragon(player, dragon)

def main():
    player_name = input("Digite o nome do jogador: ")
    player = Player(player_name)
    dragon = Dragon("Dragão Quetzalcóatl")
    
    print(f"Bem-vindo ao Emberlyn, {player.name}!")
    print("Você está em uma aventura perigosa em busca de um tesouro lendário.")
    print("Você chega a uma encruzilhada. À sua esquerda, há um castelo. À sua direita, uma ponte estreita.")

    choice = input("Você deseja entrar no castelo (1) ou atravessar a ponte (2)?, escolha com Sabedoria ")

    if choice.lower() == "1":


        castelo = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠰⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡀⠈⡇⠀⠀⠀⡄⣴⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠛⠷⢸⡇⣦⣦⡖⡏⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⢸⣷⣿⣿⣧⡇⠠⣿⡇⣰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⢻⣼⣿⡿⣻⢿⣇⣴⣿⡇⡟⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⢸⢻⣿⡇⡏⢸⣿⢹⣿⣟⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠀⢸⠿⣿⡇⡇⢸⣿⠿⣿⡿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣠⣠⣠⠀⠀⠀⢺⠀⢸⠀⣿⣷⣷⣾⣿⠀⣿⡇⡗⡇⠀⠀⣤⣠⣠⢠⠀⠀⠀⠀
⠀⠀⠀⠈⣿⣿⡏⠀⠀⠀⢼⣰⣸⣿⡏⠛⢻⠛⡟⣿⣿⡇⣿⡇⠀⠀⠈⣿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡏⡇⠀⠀⠀⣼⣿⣿⣿⣷⣶⣾⣶⣶⣿⣿⡇⣿⡇⠀⠀⠀⡏⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣇⡇⠀⠀⠀⢿⣿⣿⣿⡿⠟⠲⠻⢿⣿⣿⡇⣿⡇⠀⠀⠀⣅⣿⡇⠀⠀⠀⠀
⠀⠀⠀⢹⣿⣿⣷⢰⡆⢰⣿⡿⢿⠀⠀⠀⠀⠀⠀⠀⠀⡿⢿⣷⡀⣰⣆⣿⡇⣿⡟⠁⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡟⠛⣿⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⣿⣿⠛⢻⣿⣿⣿⡏⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡇⠀⣿⣿⣿⣏⠀⢀⠀⠀⢀⠀⠀⠀⣿⣿⣿⣯⠀⢸⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣷⣷⣿⣿⣿⣧⢼⣈⠃⠀⢸⢋⣠⠄⣿⣿⣿⣿⣾⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢥⢇⡃⠀⢸⡺⡪⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⣟⠂⠀⢸⢲⢏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠺⣌⡇⠀⢸⣧⡝⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣃⣀⣸⣾⣶⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀
⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
"""
        print(castelo)

        
        Dragão = """"
                   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠄⠀⠀⠀⢠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⠀⠀⠀⢠⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢹⡄⠀⠀⠀⢸⢣⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠀⢻⡻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡜⢿⣇⠀⠀⡏⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⢸⡇⠀⠈⣷⡹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⡀⠉⠓⢶⡇⢠⣧⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⣶⣶⣤⣄⣀⠀⠀⠀⠀⢸⡇⢸⣇⠀⠀⠸⡇⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣷⣄⢸⡇⠈⣿⡟⠳⢦⣄⡀⠀⠀⠀⠀⠉⠻⢯⡉⠙⠶⣄⠉⠳⣤⠀⠀⠸⣇⠀⢻⡀⠀⠀⢱⠀⠸⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⠀⢯⢷⠀⠀⠀⠉⠛⠶⣦⣄⡀⠀⠀⢳⡀⠀⠀⠳⡄⠀⠳⡄⠀⠻⣆⠀⠻⣆⠀⢸⡆⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡇⠀⢸⡌⣧⡀⠒⢦⣀⠀⠀⠀⠙⠻⢦⣀⢷⡀⠀⠀⢹⡄⠀⠹⣦⡠⢿⣿⡷⣮⣻⣾⡇⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠘⣷⠙⣿⣶⣄⡉⠳⣄⡀⠀⠀⠀⠈⠻⢷⣄⠀⠀⣿⠀⠀⠙⣶⣏⣡⣶⠿⠿⠏⢻⣄⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⢿⠀⠀⠸⣆⠘⢷⡙⠿⣦⡈⠳⣦⣀⠀⠀⠀⠀⠙⢧⣀⣿⠆⠀⢸⠟⢻⣿⠻⣆⠀⠀⠀⠙⢧⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠛⢳⣾⡆⠀⠀⠻⡄⠈⠳⣄⠙⢿⣦⡈⠻⣧⡄⠀⠀⠀⠀⠙⢿⡆⠀⠃⠀⠉⣿⣆⢹⡄⠀⠀⠀⠈⣧⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣞⣉⣷⠀⠀⠀⠹⣄⠀⠙⢧⡀⠙⢷⣄⠘⢿⣤⡀⠀⠀⠀⠀⠻⣦⣄⠀⢸⠋⠙⣦⣿⡀⠀⠀⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⡛⠛⠛⠻⢿⣧⡀⠀⠀⠙⢧⡀⠈⠻⣦⢤⣹⣦⠀⢻⣿⠀⠀⠀⠀⣀⣹⣏⣴⣇⠀⠀⠈⣿⡇⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠈⢹⣷⠀⠀⠈⢷⠳⡀⠀⠀⠈⠻⣄⠀⠉⢷⣭⡙⣧⠀⣹⣷⣶⢖⣫⣭⣽⣿⣅⠀⠀⣰⠟⠙⡿⣦⣤⣤⣄⣸⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠘⣧⠙⢦⣀⡀⠀⠙⢦⡀⠀⠙⢿⣿⣿⣏⣽⣿⣿⠟⠛⢋⣻⣿⣷⣶⡋⠀⠀⣠⠾⢿⣗⠿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⡿⠿⠶⠶⢶⣶⣶⣶⣿⣧⡀⠻⣿⣶⡀⠈⢳⣄⠠⣄⠀⠙⠿⣿⡟⠁⠀⡴⠋⠉⠉⠙⣧⡉⠀⠊⠀⠀⠀⢙⣷⣌⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠿⢦⡀⠀⠀⠀⠀⠀⠀⠈⠉⠙⢿⣿⣦⡀⠻⣿⣶⣤⠹⣦⠈⢷⡀⢠⡟⢿⣄⠀⠀⠀⡴⠒⠂⠉⠻⢦⡀⠀⢀⠞⠉⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠞⠉⠀⠀⠀⢠⡟⠀⣀⣀⣀⣀⣀⣀⣠⡶⠛⠛⣿⣿⣷⡀⠉⠻⣿⣌⣧⠀⣿⡟⠀⠀⠙⢷⣄⣸⠁⠀⠀⠀⠠⠤⢽⣏⠛⠀⠀⣀⣼⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⠿⠿⠛⠻⢿⣿⡿⠋⠀⠀⠈⠉⢿⣿⣿⣄⠀⠹⣿⣿⣿⣿⠁⠀⠀⠀⠀⠙⣿⣦⡀⣸⠀⠀⠀⠀⡬⢷⣤⣴⠁⠀⠻⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠟⠉⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⢀⣀⣠⠾⣿⣿⣿⣿⣄⠀⠉⠉⢻⣿⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣷⣄⣰⡄⠀⠀⠀⠹⠀⠀⠀⠛⢿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⠥⢤⡀⠀⠀⠀⠀⣀⣠⡾⠃⠀⠀⠈⠉⠁⠀⠀⠀⠈⠻⣿⣿⣧⣀⣀⣘⣿⡄⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠰⡄⠀⡀⠀⢸⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⠟⠁⠀⢀⣇⣀⣴⣶⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠿⢿⣿⡿⠉⠻⣦⡀⠀⠀⠀⠀⠀⠻⣇⠉⠛⢿⣿⣆⠀⠀⠀⠀⣳⣠⡇⣰⣼⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠁⠀⣠⣴⠿⠛⠉⠁⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣾⣿⡟⢿⠃⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠙⢷⣤⣤⣿⣿⢿⡶⠤⠶⠛⣿⠛⠛⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡿⠋⠁⠀⠀⠀⠀⣰⠇⠀⠀⠀⠀⠀⢀⡤⠖⠛⣫⣴⣾⣿⠛⠋⠀⠸⣧⣸⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠉⠻⣿⣿⠀⢷⡀⠀⠀⢻⡆⠘⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⣠⣾⠋⠀⠀⠀⠀⣠⠾⠋⢀⣤⣾⣿⠛⠉⠻⣆⠀⠀⠀⠙⢿⡄⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⠘⠇⠀⠀⠘⡇⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⣴⡏⣠⡀⠀⣠⣴⣾⣿⠇⠀⠀⠀⠀⠞⠋⠀⣴⣿⣿⣿⠁⠀⠀⠀⠙⢧⡀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣧⡀⠀⠀⠐⢷⡀⣷⠀⠀⠀⠀⠀
⠀⠀⢠⣿⠟⠉⣡⣾⡿⠋⠁⡟⠀⠀⠀⠀⠀⠀⢀⣾⣿⠟⠁⢿⡆⠀⠀⠀⠀⢀⡟⠻⣍⠉⠉⠻⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣬⡇⠀⠀⠀⠈⠳⢻⡆⠀⠀⠀⠀
⠀⠀⠸⠁⢀⣾⡟⠋⠀⠀⣼⠀⠀⠀⠀⠀⠀⣠⣿⣿⠁⠀⠀⠀⠙⣦⡀⠀⠀⢸⡀⠀⢈⡷⢦⣤⣬⡿⢶⣄⡀⠀⠀⢰⣤⡀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀
⠀⠀⠀⢀⣾⠏⠀⠀⠀⣰⠇⠀⠀⠀⠀⠀⣴⣿⣿⣹⣧⠀⠀⠀⠀⠀⠉⠉⠉⠉⠻⣏⠁⠀⣠⡟⠁⠀⠀⠈⠙⠶⣄⠘⠿⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀
⠀⠀⠀⣿⠃⠀⠀⢀⣼⡟⠀⠀⠀⠀⠀⢰⣿⡿⠁⠀⠘⢧⡀⠀⠀⠀⠘⢷⣀⣀⣤⠾⢿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠈⠹⣦⡀⠉⠳⣦⡀⠀⠀⠀⠀⠀⢴⡏⠉⠙⠶⠄⠘⡗⠶⡄
⠀⠀⢸⣇⡴⢶⣠⣾⣿⡇⠀⠀⠀⠀⢰⣿⣿⠃⠀⠀⠀⠀⠉⠛⢶⠶⠶⠞⢷⠀⠀⣰⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠙⢳⣄⠀⠀⠀⠈⣿⣄⠀⠀⠀⠀⠀⠀⣿
⠀⠀⣼⠟⢀⣾⡿⠋⣸⡇⠀⠀⠀⠀⣼⣿⠹⣇⠀⠀⠀⠀⠀⠀⠈⣆⠀⣀⣨⠟⠋⣽⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⠠⡀⠙⣧⡀⠀⢰⣿⣿⣆⠀⠀⠀⠀⠀⢻
⠀⢀⡏⢀⣾⡟⠀⠀⣿⠃⠀⠀⠀⢸⣿⡿⠶⠛⠷⣤⣀⣀⣀⣀⣠⢿⡟⠉⠁⠀⣼⡿⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣽⡄⠸⣇⠀⠘⠞⢿⣿⠤⠶⠂⡔⢠⠟
⠀⠀⠀⣾⡟⠀⠀⢰⡿⠀⠀⠀⠀⣿⡟⠀⠀⠀⠀⠀⠉⢹⡏⠁⠀⠈⢷⡤⠤⢴⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠻⣄⡀⠀⠶⠏⠀⠀⠀⡇⣸⠀
⠀⠀⢸⣿⠁⠀⠀⢸⡇⠀⠀⠀⢰⣿⠻⣄⠀⠀⠀⠀⠀⠈⢷⣀⣤⠔⠋⠀⠀⢰⣿⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⠈⠛⠲⣤⡀⠀⣀⡼⣿⠏⠀
⠀⠀⣼⡇⠀⠀⠀⢸⡇⠀⠀⠀⣼⣿⠴⠚⠓⢤⣄⣀⣀⣤⠴⣯⡀⠀⠀⠀⠀⣼⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠦⣤⠬⢿⣦⣅⡿⠋⠀⠀
⠀⠀⣿⣴⠞⠛⢳⣼⡇⠀⠀⢠⣿⠏⠀⠀⠀⠀⠈⢹⡍⠀⠀⠈⢳⣤⣤⣴⠞⢻⡏⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⠀⠀⠀
⠀⢐⡿⠁⠀⠀⣾⣿⡇⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀⠀⠙⣆⣀⡤⠞⠁⠀⠀⠙⢿⡇⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⡇⠀⠀⣼⣿⢻⣇⠀⠀⣿⣿⠓⢤⣀⠀⠀⠀⢀⣤⠿⣯⠀⠀⠀⠀⠀⢀⣾⡇⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠁⠀⢸⣿⠃⢘⣿⠀⠀⣿⣿⠶⠋⠉⠛⠛⣿⠉⠁⠀⠙⢷⣤⣀⣠⣴⠊⣻⡇⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡟⠀⠈⣿⠀⢸⣿⡟⠀⠀⠀⠀⠀⠘⠦⣀⢀⣠⠟⠁⠀⠀⠈⠻⣿⡇⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⣿⢡⠞⢧⣿⠀⢸⣿⣧⡀⠀⠀⠀⠀⠀⠀⣰⣏⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠇⠀⣸⣿⠀⣾⣿⣍⣳⠦⢤⣀⡤⠴⠞⠁⠸⢧⡀⠀⠀⠀⠀⣠⣾⣿⡀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡿⠀⢠⣿⣿⠀⣿⡿⠉⠁⠀⠀⠹⣇⠀⠀⠀⠀⠀⣿⠷⠶⠶⠟⠻⣅⣿⡇⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠃⣿⠀⣿⣇⠀⠀⠀⠀⠀⠈⠳⢤⣀⡴⠞⠁⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡿⢰⡟⢠⣿⣿⡄⠀⠀⠀⠀⠀⣀⣴⢿⡅⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀⠀⠀⠀⠀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⣸⡇⢸⣿⣿⡿⠓⠦⢤⣶⡛⠋⠁⠀⠙⠲⣤⣄⣀⣀⣀⣀⣴⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⢻⡇⢸⣿⠁⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀⢀⣼⠟⠉⠉⠋⠉⠀⠉⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢁⣿⠇⢸⣿⠀⠀⠀⠀⠀⠀⠈⠳⢤⣤⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⡏⠀⣸⣿⡀⠀⠀⠀⠀⠀⠀⣠⣼⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠃⠀⣿⣿⣷⣶⣶⣶⣶⣶⡿⠋⠀⠉⠈⠙⢦⣄⣀⣀⣀⣠⣤⠶⠚⠓⠛⠛⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡟⠀⢰⣿⣿⠿⢛⡏⠉⢻⡇⠀⠀⠀⠀⠀⠀⢀⡽⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠘⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠷⣤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⠃⠀⣸⣿⠉⠓⠊⠀⠀⠀⢳⡄⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⡿⠀⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠈⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⣀⣠⣤⠶⠶⠶⠛⠛⠛⠲⠿⠀⠀⠀⠀⠀⠀
⠀⢀⣴⣿⡇⠀⠀⣸⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⣠⡿⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⠿⠦⠤⠴⠾⠋⠁⠉⠙⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⠟⠁⣿⣀⣀⣾⡿⠿⠛⠿⢷⣶⣤⣠⣤⠴⠞⠋⠀⠀⠙⢦⣄⣀⠀⠀⠀⠀⠀⣀⣠⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠉⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡟⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀⢀⡴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢦⣥⠤⠞⠋⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

        print(Dragão)
        print 
        print("Você entra no castelo e se depara com um dragão enorme e amedrontador chamado Quetzalcóatl, e reparar que ele esta protegendo um Báu repleto do tesouros!")
        fight_with_dragon(player, dragon)
        
    elif choice.lower() == "2":
        print("Você decide atravessar a ponte. Ela parece instável...")

        ponte = """                                              
                             ___....___                             
   ^^                __..-:'':__:..:__:'':-..__                                   
            _ :.':  :  :  :  :  :  :  :  :  :  :  :'.: _           
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]          
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]          
  :::::::::[ ]:__:__:__:__:__:__:__:__:__:__:__:__:__:[ ]:::::::::::
 !!!!!!!!![ ]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![ ]!!!!!!!!!!!
  ^^^^^^^^^[ ]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[ ]^^^^^^^^^^^
           [ ]                                        [ ]          
           [ ]                                        [ ]          
           [ ]                                        [ ] 

    """
        print(ponte)


        perdeu = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⠊⠉⠉⠉⠒⠲⢤⣀⠀⠀⠀⠀⠀⣀⣤⠤⠶⠒⠶⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣀⣠⠤⢤⣀⣀⡀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠉⠙⠲⢤⣹⣀⣀⡤⠤⠤⠤⠤⠤⠤⢄⣀⣈⣇⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠒⣊⡭⠥⠔⠒⠲⠦⠤⢭⣉⣳⣄⣤⣴⣒⣊⡭⠭⠭⠭⠭⠭⣿⣶⣻⣦⣀⠀
⠀⠀⠀⢀⡴⠚⢹⠃⠀⠀⠀⠀⠀⠀⢀⡤⠖⢚⣡⠖⠋⠁⠀⠀⠀⠀⠀⢀⣀⣀⣀⣙⣿⡛⠉⠁⠀⢀⣀⣀⣠⣤⣤⣤⠤⣭⣝⣿⣄
⠀⠀⢠⡞⠁⠀⣾⠀⠀⠀⠀⠀⠀⣾⣛⣛⠋⠉⢀⣀⣀⡠⠤⢶⣶⢿⣿⣿⣤⡀⠀⠀⠈⡷⠒⠚⠉⠉⢠⣿⡿⢿⣿⣿⣦⡀⠀⠉⢻
⠀⢀⡏⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠯⣉⠀⠀⠀⢠⣿⣿⣶⣿⠛⢻⣿⡆⠀⣰⠁⠀⠀⠀⠀⣿⣿⠿⣿⣏⣹⣿⣧⢀⣠⡞
⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⢬⣙⠒⠤⢼⠿⢿⡿⠿⠿⠿⠛⠛⢉⡼⠛⠓⠒⠒⠶⠟⠛⠛⠛⠛⠛⠋⢩⡿⠛⠀
⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠒⠒⠒⠒⠒⠒⣲⡾⠉⠉⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠋⠁⠀⠀⠀⠀⠈⠛⠢⢤⣤⠤⠤⠴⠒⢿⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠁⡀⠀⣀⡀⠀⠉⠉⠙⠓⠒⠲⠦⠤⠤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⠤⠶⠚⠉⢉⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡅⠀⠀⠉⠉⠉⠉⠉⠓⠒⠶⠤⢤⣤⣀⣀⣀⣀⡀⠀⠀⠉⠉⠉⠉⠁⣀⣀⣀⣀⣠⣴⠟⠁⠀⠀
⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠙⠒⠒⠒⠒⠒⠲⠦⠤⠤⣀⣀⣀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⢀⣿⠀⠀⠀⠀
⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠛⠒⠒⠒⠒⠶⠶⠶⠶⢶⡦⠶⠒⠋⠁⠀⠀⠀⠀
⠟⠿⢿⡶⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠓⠦⣭⣉⠓⠒⠶⠦⠤⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡤⠖⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠲⠦⢤⣤⣤⣀⣀⣀⣉⣉⣉⣉⣉⡉⢉⣉⣉⣉⣉⣩⣭⠟⠛⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                    
"""
        print(perdeu)

        print("Você escorrega e cai em um abismo profundo e sem saida ou seja, Você Escolheu a MORTE!")


    else:
        print("Escolha inválida! Você fica parado sem fazer nada.")

if __name__ == "__main__":
    main()