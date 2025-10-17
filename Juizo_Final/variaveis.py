import json

WIN_ALTURA = 750
WIN_LARGURA = 1350

caminho_botao_img = 'imagens/Button_1.png'
caminho_balao_perg = 'imagens/Balao_pergunta.png'

caminho_bg_img = ''

caminho_main_img = 'imagens/backgrounds/main_background.jpg'

caminho_trabalho_img = 'imagens/edificios/trabalho.png'

caminho_escola_img = 'imagens/edificios/escola.jpeg'

caminho_familia_img = 'imagens/edificios/familia.jpeg'

caminho_faculdade_img = 'imagens/edificios/faculdade.jpg'


def pegar_imagem(background):
    global caminho_bg_img, caminho_person_img
    if background == 'escola':
        caminho_bg_img = 'imagens/backgrounds/background_escola.jpg'

    elif background == 'familia':
        caminho_bg_img = 'imagens/backgrounds/background_familia.jpg'

    elif background == 'faculdade':
        caminho_bg_img = 'imagens/backgrounds/background_faculdade.jpg'

    else:
        caminho_bg_img = 'imagens/backgrounds/background_trabalho.jpg'

    


with open('dados/perg_resp.json',encoding='UTF-8') as f:   
    dados = json.load(f) 