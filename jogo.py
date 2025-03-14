import random

class Personagem():
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome #encapsulamento - Privado
        self.__vida = int(vida)
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    

    def exibir_dados(self):
        return f"Nome: {self.get_nome()} \nVida: {self.get_vida()} \nNivel: {self.get_nivel()}"
    
    def recebe_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() *2, self.get_nivel()* 4)
        alvo.recebe_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


#Classe FILHO
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_habilidade(self):
        return f"{super().exibir_dados()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel()* 8)
        alvo.recebe_ataque(dano)  
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} dano")

#Classe FILHO
class Vilao (Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_tipo(self):
        return f"{super().exibir_dados()}\nTipo: {self.get_tipo()}"


#Clsse Jogo Orquestradora do jogo
class Jogo():
    def __init__(self) -> None:
        self.heroi = Heroi(nome= "Heroi", vida=50, nivel=5, habilidade="Super Força")
        self.vilao = Vilao(nome= "Vilao", vida=50, nivel=5, tipo="Voador")


    #gestão em turnos
    def iniciar_batalha(self):
        print("Iniciando Batalha!")

        while self.heroi.get_vida() > 0 and self.vilao.get_vida()  > 0:
            print("\nDetalhes dos Personagens")
            print(self.heroi.exibir_habilidade())
            print(self.vilao.exibir_tipo())

            input("Precione Enter para atacar...")
            escolha = input("Escolha 1 - Ataque normal 2 - Ataque Especial ")

            if escolha == "1":
                self.heroi.atacar(self.vilao)
                if self.vilao.get_vida() > 0:
                    self.vilao.atacar(self.heroi)
            elif escolha == "2":
                self.heroi.ataque_especial(self.vilao)
                if self.vilao.get_vida()>0:
                    self.vilao.atacar(self.heroi)
            else:
                print("Escolha inválida, Por favor escolha novamente")
            



        if self.heroi.get_vida() > 0:
            print("\n Parabens, você venceu !!")
        else:
            print("\n Você foi derrotado !!")

#instancia do jogo
jogo = Jogo()
jogo.iniciar_batalha()
