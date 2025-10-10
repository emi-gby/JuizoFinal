import json

WIN_ALTURA = 750
WIN_LARGURA = 1350

caminho_botao_img = 'imagens/Button_1.png'

caminho_person_img = 'imagens/professora.png'

caminho_bg_img = 'imagens/Background_escola.jpg'

caminho_balao_perg = 'imagens/Balao_pergunta.png'

with open('dados/perg_resp.json',encoding='UTF-8') as f:   
    dados = json.load(f) 