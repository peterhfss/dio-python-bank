<h1 align="center">PyBank</h1>

<p align="center"> Desafio de criar um sistema bancário com o Python realizado no bootcamp de Python Developer da DIO.</p>

<br>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#instalacao">Instalação</a> • 
 <a href="#como-usar">Como usar</a> • 
 <a href="#tecnologia">Tecnologia</a>
</p>

## Sobre
<br>


Projeto desenvolvido como desafio no bootcamp de Python Developer que foi realizado pela Digital Innovation One. A proposta do desafio era de criar um sistema bancário usando o Python , ao mesmo tempo que poderiamos estar praticando o que foi apresentado durante o módulo de fundamentos do Python. <br>


## Instalação
<br>

Após clonar esse repositório , realizar esses comandos no seu terminal:

```bash
cd dio-python-bank
cd app

```

Uma vez estando dentro da pasta do projeto, para iniciar basta executar o seguinte comando:

```python
python Bank.py
```

## Como usar

No terminal irá exibir um menu com as seguintes opções:

* [Depósito](#depósito)
* [Saque](#saque)
* [Extrato](#extrato)
* [Sair do Sistema](#sair-do-sistema)

<br>

### Depósito
<br>

Essa operação irá realizar um depósito no sistema bancário com o valor informado pelo usuário. O valor precisará ser positivo, caso o valor não seja , uma mensagem é exibida no terminal. sendo maior que zero, o depósito será realizado e retornará uma mensagem sobre o novo saldo. Todo depósito irá ser armazenado no extrato.

### Saque
<br>

Essa operação realiza saques no sistema bancário, contudo somente são liberados 3 saques diários com limite até R$ 500.00, onde irá retornar uma mensagem caso o valor for maior que esse limite ou um valor negativo for digitado.Assim como o depósito, todo o saque realizado irá ser armazenado no extrato.

### Extrato
<br>

Essa operação exibi no terminal toda a movimentação ocorrida no sistema. Caso ainda não tiver acontecido, uma mensagem informando que nenhuma movimentação foi realizada irá ser exibida para o usuário.Ao final do extrato, o saldo também será exibido.

### Sair do Sistema

Essa operação finaliza o sistema e encerra o  mesmo.

<br>

> Uma mensagem irá ser exibida caso o usuário digite uma operação inválida.

## Tecnologia

Todo o projeto foi utilizado somente o Python, contudo diferente do proposto no desafio, adicionei funções e módulos para poder praticar sobre esses conceitos . 