# Automação Magic Tiles 3
Este código é uma automação do jogo "Magic Tiles 3" utilizando a biblioteca MSS (Multiple Screen Shot) e OpenCV. Ele captura a tela do jogo e analisa a cor de pixels específicos para determinar qual tecla pressionar.

Para utilizar este código, é necessário ter as bibliotecas MSS e OpenCV instaladas em sua máquina. Além disso, é necessário importar a biblioteca "win32gui" para dar foco à janela do jogo e a biblioteca "keys" para pressionar as teclas.

A função "focusWindow" define qual janela deve ser focalizada, utilizando o título da janela como parâmetro. A função "teclado" analisa a cor de pixels específicos na tela do jogo e pressiona as teclas correspondentes (A, S, D e F). A função "tela" captura a tela do jogo, a converte para escala de cinza e chama a função "teclado" para analisar as cores dos pixels.

O código é executado em um loop, mostrando a tela capturada e a taxa de quadros por segundo (FPS). O usuário pode pressionar "q" para sair do loop e fechar as janelas.

Este código pode ser usado como um exemplo para automatizar outros jogos ou tarefas que envolvam análise de pixels na tela.
