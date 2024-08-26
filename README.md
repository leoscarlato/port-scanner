# Port Scanner

Projeto para a matéria de Cybersegurança do curso de Ciência da Computação.

Feito por [Leonardo Scarlato](https://github.com/leoscarlato)

## Objetivo
Desenvolvimento de uma aplicação que realize o escaneamento de portas
de comunicação de um destino por meio de bibliotecas de desenvolvimento da
Linguagem de programação Python.

Além disso, a aplicação deveria possuír uma interface amigável para o usuário e de fácil utilização.

## Tecnologias utilizadas
Foi utilizada a linguagem ***Python***, junto à biblioteca ***Socket*** para realizar a verificação das portas de comunicação, além da biblioteca ***Tkinter*** para a criação da interface gráfica.

## Funcionamento
O usuário deve inserir o IP do destino e o intervalo de portas que deseja verificar. Após isso, basta clicar no botão "Começar verificação" e aguardar o resultado.

## Como executar
1. Clone o repositório
```bash
git clone https://github.com/leoscarlato/port-scanner.git
```

2. Acesse a pasta do projeto no terminal
```bash
cd port-scanner
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute o projeto
```bash
python main.py
```

Em seguida, se abrirá a interface gráfica da aplicação. Nela, basta inserir o IP do destino e o intervalo de portas que deseja verificar nos campos indicados e clicar no botão "Começar verificação".

Assim, a aplicação irá realizar a verificação das portas e exibirá o resultado na tela.

## Referências
https://www.geeksforgeeks.org/port-scanner-using-python/

https://medium.com/@wizD/a-simple-port-scanner-using-python-e541454ea570

 https://www.infosecinstitute.com/resources/penetration-testing/write-a-port-scanner-in-python/