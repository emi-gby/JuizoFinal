import json
from customtkinter import FontManager
from pathlib import Path

#constantes
WIN_ALTURA = 750
WIN_LARGURA = 1350

KARMA_BOM = 20
KARMA_RUIM = -20


#Inicio Imagens
BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / 'imagens'
SONS_DIR = BASE_DIR / 'sons'
FONTES_DIR = BASE_DIR / 'fontes'
DADOS_DIR = BASE_DIR / 'dados'

#Importar fontes
FontManager().load_font(FONTES_DIR /'goth.otf')
FontManager().load_font(FONTES_DIR /'pixel_fonte.otf')
FontManager().load_font(FONTES_DIR /'KnightWarrior.otf') 


caminho_inicio_bg = IMAGES_DIR /'backgrounds'/'inicio_bg.png'

caminho_play_botao = IMAGES_DIR /'play_botao.png'

#Sons
caminho_soundtrack = SONS_DIR /'soundtrack.ogg'

caminho_maquina_escrever_som = SONS_DIR /'maquina_de_escrever.wav'

caminho_botao_start_som = SONS_DIR /'botao_start.wav'

caminho_botao_clique_som = SONS_DIR /'botao_clique.wav'

#Icones

caminho_botao_img = IMAGES_DIR /'Botao.png'

caminho_balao_perg = IMAGES_DIR /'Balao_pergunta.png'

caminho_karma_img = IMAGES_DIR /'karma.png'

caminho_anjo_img = IMAGES_DIR /'anjo_icon.png'

caminho_demonio_img = IMAGES_DIR /'demonio_icon.png'

#Tela principal

caminho_main_img = IMAGES_DIR /'backgrounds'/'main_background3.jpeg'


#Cenarios Imagens

caminho_trabalho_img = IMAGES_DIR /'edificios'/'trabalho.png'

caminho_escola_img = IMAGES_DIR /'edificios'/'escola.png'

caminho_familia_img = IMAGES_DIR /'edificios'/'familia.png'

caminho_faculdade_img = IMAGES_DIR /'edificios'/'faculdade.png'


def pegar_imagem(background):
    '''retorna o caminho da imagem do background para a respectiva fase'''
    if background == 'escola':
        return str(IMAGES_DIR /'backgrounds'/'background_escola.jpg')

    elif background == 'familia':
        return str(IMAGES_DIR /'backgrounds'/'background_familia.jpeg')

    elif background == 'faculdade':
        return str(IMAGES_DIR /'backgrounds'/'background_faculdade.png')

    else:
        return str(IMAGES_DIR /'backgrounds'/'background_trabalho.jpeg')

#Final Imagens
caminho_inferno_bg = IMAGES_DIR /'backgrounds'/'inferno.png'

caminho_paraiso_bg = IMAGES_DIR /'backgrounds'/'paraiso.png'

caminho_purgatorio_bg = IMAGES_DIR /'backgrounds'/'purgatorio.png'

#Dados Perguntas
with open(DADOS_DIR/'perg_resp.json',encoding='UTF-8') as f:   
    dados = json.load(f) 