# Plataforma Livre de Dados Abertos Governamentais | Dados Livres

## Link do GitLab: 
[https://gitlab.com/pbaesse/dados-livres](https://gitlab.com/pbaesse/dados-livres)

## Descrição
A Plataforma Livre de Dados Abertos Governamentais trata-se de um site que nasceu no IFRN — campus Ceará-Mirim no ano de 2018, quando dois alunos tiveram interesse em criar um projeto de pesquisa onde o foco seria ajudar pessoas com informação e, ao mesmo tempo, contribuir com o Software Livre. Então, foi aí que o orientador e mestre Baesse, apresentou os Dados Abertos Governamentais e uma ferramenta que pudesse ser construída unindo tudo isso.

Dados Abertos Governamentais são informações que são disponibilizadas pelo governo obrigatoriamente pela Lei de Acesso à Informação, que permite reutiliza-los, reproduzi-los e redistribui-los livremente, sendo alguns dos temas, que podem ser trabalhados: saúde, educação, segurança, meio ambiente, cultura e lazer. Mas nem sempre essas informações estão facilmente acessíveis e visualizáveis, pois elas estão espalhadas em todas as esferas do governo municipal, federal e estadual, então visando suprir essas lacunas foi lançada a Plataforma Livre de Dados Abertos Governamentais, onde o seu principal objetivo é:

> “Mapear fontes de dados abertos governamentais e softwares relacionados para o uso de desenvolvedores e pessoas comuns, onde é o próprio usuário que vai cadastrar tais informações.”

Então o usuário poderia cadastrar, por exemplo, a frequência de médicos em hospitais públicos, ou a média escolar em tal ano por alunos de escola pública, ou quantas praças públicas existem nas pequenas cidades em determinada região e, além disso, poder relaciona-las com uma funcionalidade extra que é de cadastrar softwares de dados abertos governamentais, por exemplo, existe a Operação Serenata do Amor que tem como objetivo fiscalizar gastos públicos suspeitos de deputados e poderá ser cadastrada na plataforma.

Este software, visa ter um grande número de engajamento, participação e colaboração do público, onde pode servir tanto para pessoas comuns, como para pesquisadores e jornalistas e ainda para qualquer desenvolvedor que queira contribuir com o seu código-fonte que será distribuído em Software Livre com as suas principais tecnologias Python e a MicroFramework Flask. Assim, gerando participação popular, democracia, controle social e transparência para reivindicar mudanças e decidir novos projetos de lei.

## Problemas conhecidos e possíveis melhorias


## Como instalar

#### Iniciando o repositório: 
```sh
git clone https://github.com/pbaesse/plataforma-livre-dados-abertos
cd plataforma-livre-dados-abertos
```

#### Usando o ambiente virtual (Virtualenv)

Instalando... (no Linux já vêm instalado)
```sh
$ virtualenv venv
```
Criando...
```sh
$ python3 -m venv venv
```
Ativando...
```sh
$ source venv/bin/activate       (Linux)
$ source venv\Script\activate    (Windows)
```

#### Instalando a lista de pacotes
Os pacotes estão salvos em um arquivo requirements. Para instala-los:
```sh
$ pip install -r requirements.txt
```

#### Exportando as variáveis de ambiente
```sh
$ export FLASK_APP=plataforma.py
$ export FLASK_DEBUG=1
```

#### Rodando a plataforma web com Flask
Flask, roda com o comando:
```sh
$ flask run
```
Endereço que roda o servidor (Localhost: Porta 5000):
```sh
http://localhost:5000/
```

## Lista de autores
- Maria Carolina: [@mariacarolinass](https://github.com/MariaCarolinass)
- Luiz Felipe: [@luiz200](https://github.com/luiz200/)

## Licença
GPL
Software Livre

## Contato
- pbaesse@gmail.com | @pbaesse
