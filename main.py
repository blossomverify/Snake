# Configurações iniciais do projeto

import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game")

largura, altura = 800, 500
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

 
# cores
preta = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# parametros da tela
tamanho_quadrado = 13
velocidade_de_atualizacao = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 13.0) * 13.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 13.0) * 13.0
    return comida_x, comida_y

def rodar_jogo():
    fim_de_jogo = False

    x = largura // 2
    y = altura // 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

   comida_x, comida_y = gerar_comida()

    while not fim_de_jogo:

        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            

# criar um loop infinito para manter o programa em execução




# Desenhar os objetos na tela
# cobrinha
# pontos 
# comida

# criar a logica de terminar o jogo
# como o jogador temina o jogo:
# cobra bateu na parede
# cobra bateu na propria cauda

# pegar interações do usuário
# fechou a tela
# apertou alguma tecla


rodar_jogo()
