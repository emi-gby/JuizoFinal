import json

WIN_ALTURA = 750
WIN_LARGURA = 1350

#Inicio Imagens

caminho_inicio_bg = 'imagens/backgrounds/inicio_bg2.jpeg'

caminho_play_botao = 'imagens/play_botao.png'

#Sons
caminho_soundtrack = 'sons/soundtrack.ogg'

caminho_maquina_escrever_som = 'sons/maquina_de_escrever.wav'

caminho_botao_start_som = 'sons/botao_start.wav'

caminho_botao_clique_som = 'sons/botao_clique.wav'

#Icones

caminho_botao_img = 'imagens/Botao2.png'

caminho_balao_perg = 'imagens/Balao_pergunta.png'

caminho_karma_img = 'imagens/karma3.png'

caminho_anjo_img = 'imagens/anjo_icon.png'

caminho_demonio_img = 'imagens/demonio_icon.png'

#Tela principal

caminho_main_img = 'imagens/backgrounds/main_background3.jpeg'


#Cenarios Imagens
caminho_bg_img = ''

caminho_trabalho_img = 'imagens/edificios/trabalho.png'

caminho_escola_img = 'imagens/edificios/escola.png'

caminho_familia_img = 'imagens/edificios/familia.png'

caminho_faculdade_img = 'imagens/edificios/faculdade.png'


def pegar_imagem(background):
    global caminho_bg_img
    if background == 'escola':
        caminho_bg_img = 'imagens/backgrounds/background_escola.jpg'

    elif background == 'familia':
        caminho_bg_img = 'imagens/backgrounds/background_familia2.jpeg'

    elif background == 'faculdade':
        caminho_bg_img = 'imagens/backgrounds/background_faculdade2.png'

    else:
        caminho_bg_img = 'imagens/backgrounds/background_trabalho5.jpeg'

#Final Imagens
caminho_inferno_bg = 'imagens/backgrounds/inferno.png'

caminho_paraiso_bg = 'imagens/backgrounds/paraiso4.png'

caminho_purgatorio_bg = 'imagens/backgrounds/purgatorio.png'

#Dados Perguntas

with open('dados/perg_resp.json',encoding='UTF-8') as f:   
    dados = json.load(f) 