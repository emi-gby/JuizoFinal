import json

WIN_ALTURA = 750
WIN_LARGURA = 1350

caminho_botao_img = 'imagens/Botao.png'

caminho_balao_perg = 'imagens/Balao_pergunta.png'

caminho_karma_img = 'imagens/karma.jpeg'
caminho_anjo_img = 'imagens/anjo2.png'
caminho_demonio_img = 'imagens/demonio2.png'

caminho_bg_img = ''

caminho_main_img = 'imagens/backgrounds/main_background3.jpeg'

caminho_trabalho_img = 'imagens/edificios/trabalho3.png'

caminho_escola_img = 'imagens/edificios/escola3.png'

caminho_familia_img = 'imagens/edificios/familia4.png'

caminho_faculdade_img = 'imagens/edificios/faculdade3.png'


def pegar_imagem(background):
    global caminho_bg_img
    if background == 'escola':
        caminho_bg_img = 'imagens/backgrounds/background_escola.jpg'

    elif background == 'familia':
        caminho_bg_img = 'imagens/backgrounds/background_familia.jpeg'

    elif background == 'faculdade':
        caminho_bg_img = 'imagens/backgrounds/background_faculdade2.png'

    else:
        caminho_bg_img = 'imagens/backgrounds/background_trabalho5.jpeg'

    


with open('dados/perg_resp.json',encoding='UTF-8') as f:   
    dados = json.load(f) 