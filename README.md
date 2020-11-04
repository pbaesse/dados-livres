# Dados Livres - Plataforma de Dados Abertos

**Plataforma Dados Livres permite o compartilhamento e a colaboração na
identificação de fontes de dados abertos e aplicações que fazem uso dessas
informações.**

A iniciativa de desenvolver Dados Livres surgiu inicialmente como um projeto
de pesquisa em uma instituição acadêmica do RN, no ano de 2019, quando um aluno
e uma aluna mostraram interesse de contribuir com projetos que fossem software
livre e o Prof. Mr. Pedro Baesse apresentou a ideia de desenvolver a plataforma.

Alguns diferenciais de Dados Livres é a praticidade, pois suas fontes e
aplicações podem ser facilmente cadastradas por qualquer usuário inscrito na
plataforma, sem exigir nenhum conhecimento de código, dessa forma, facilitando
encontrar vários possíveis colaboradores. Além disso, suas bases de dados podem
ser ligadas às aplicações criadas e vice-versa.

A disponibilidade dessas informações abertas direcionadas a sociedade civil gera
benefícios como: controle social, transparência pública, democracia, inovação
cívica, combate à corrupção e vários outros.

# Problemas conhecidos e possíveis melhorias

# Como instalar

Faça um fork do projeto Dados Livres e em seguida clone o repositório forkado
por você:

```sh
$ git clone https://gitlab.com/pbaesse/dados-livres.git
$ cd dados-livres       (entre na pasta clonada)
```

Use um ambiente virtual para fazer as instalações utilizadas na aplicação -

Para criar o ambiente virtual com o [venv](https://docs.python.org/pt-br/dev/library/venv.html):

```sh
$ python3 -m venv venv
```

Para ativar o ambiente virtual:

```sh
$ source venv/bin/activate       (Linux)
$ source venv\Script\activate    (Windows)
```

E finalmente, instale as dependencias da aplicação:

```sh
$ pip install -r requirements.txt
```

## Configurando o projeto

Copie o arquivo .env-example e renomei para .env.

Defina o valor para a variável `SECRET_KEY` nesse arquivo.

Se necessário, pode utilizar os comandos abaixo para gerar um valor para `SECRET_KEY`  

```sh
$ python
>>> import uuid
>>> uuid.uuid4().hex
```

Criando o banco de dados:

```sh
$ flask db stamp head
$ flask db migrate -m "criei o banco de dados"
$ flask db upgrade
```

Para rodar a aplicação utilize o comando:

```sh
$ flask run
```

Acesse no seu navegador o seguinte endereço abaixo:

```sh
http://localhost:5000/
```

# Lista de autores

- Carolina Soares ([@mariacarolinass](https://gitlab.com/mariacarolinass))

# Licença

Dados Livres é Licenciado sob Licença GPL-3.0.

# Contato

E-mail para contato: pbaesse@gmail.com

Outros meios de contato:

- Telegram: [carols0](https://t.me/carols0) ou [pbaesse](https://t.me/pbaesse)
