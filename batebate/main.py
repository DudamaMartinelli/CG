# Importa a classe Game do arquivo game.py
from game import Game

# Verifica se este arquivo está sendo executado como o programa principal
if __name__ == "__main__":
    # Cria uma instância da classe Game
    game_instance = Game()
    # Executa o jogo chamando o método run da instância
    game_instance.run()
