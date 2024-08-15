import pygame
from pygame.locals import *
import random
import threading


pygame.init()

# tela

tamanhoTela = (850 , 520)

tela = pygame.display.set_mode(tamanhoTela)
relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 60)

filosofosImagens = { "Platão", "Nietzsche" , "Simone de Beauvoir" , "Confucio" , "René Descartes"
    
}

def draw_screen():
    screen.fill((255, 255, 255))  # Fundo branco
    # Desenhar filósofos e outros elementos na tela
    pygame.display.flip()

# Função para atualizar o estado dos filósofos
def atulizar():
    # Alternar entre comer e pensar a cada 7 segundos
    pass

# Função de perguntas e respostas
def perguntar():
    # Mostrar pergunta e verificar resposta
    pass

# Função para controlar o cronômetro
def cronometro():
    global time_left
    while time_left > 0:
        time_left -= 1
        pygame.time.wait(1000)
        if time_left == 0:
            game_over()

# Função de Game Over
def game_over():
    # Mostrar mensagem de Game Over
    pass

# Loop principal do jogo
running = True
time_left = 30
question_thread = threading.Thread(target=perguntar)
question_thread.start()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    atulizar()
    draw_screen()
    relogio.tick(60)  # 60 frames por segundo

pygame.quit()