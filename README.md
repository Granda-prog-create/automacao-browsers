Este projeto fornece um código Python para automatizar a pesquisa no YouTube em sistemas Mac e Linux. O código:

Solicita ao usuário o que ele deseja pesquisar.
Realiza a pesquisa no YouTube.
Pergunta ao usuário se ele deseja realizar outra pesquisa.
Funcionalidades:

Suporte para Mac e Linux.
Interface de linha de comando simples.
Permite pesquisas com acentos.
Requisitos:

Python 3.6 ou superior
Bibliotecas pyautogui, pyperclip e platform (já instaladas na maioria dos sistemas)
Instalação:

Clone este repositório em seu computador.
Instale as bibliotecas necessárias:
pip install pyautogui pyperclip
Uso:

Abra o terminal ou prompt de comando.
Navegue até a pasta do projeto.
Execute o comando:
python main.py
Digite o que você deseja pesquisar no YouTube e pressione Enter.
O código irá realizar a pesquisa e abrir o vídeo no navegador.
Exemplo de uso:

Digite o que você deseja pesquisar no YouTube: Metallica

Realizando pesquisa...

Abrindo vídeo...
Observações:

As coordenadas para clicar na barra de pesquisa do YouTube podem variar. Ajuste os valores de x e y de acordo com seu computador.
O tempo de espera (time.sleep) pode precisar ser ajustado dependingo da velocidade do seu computador.
Sugestões:

Você pode adicionar mais opções ao código, como a capacidade de abrir o YouTube em um navegador específico.
Você pode usar imagens personalizadas para identificar elementos na tela.
Você pode usar a biblioteca webbrowser para abrir o YouTube diretamente em um navegador específico.
Contribuições:

Sinta-se à vontade para enviar pull requests com melhorias ou correções de bugs.