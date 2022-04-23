# PORTIFOLIO-BLOG-POSTS

É um pequeno exemplo de como criar uma simples aplicação Web como exemplo Portifolio com Blog para fins didaticos usando Makefile com Flask, Sqlite3, Html, Css, Js, Bootstrap

### COMO RODAR ESSE PROJETO

1. Pré condiçaõ Git, Python3 instalados
2. Clone esse repositório.
3. Rode o ambiente com os comandos.

### NO TERMINAL

```
git clone https://github.com/vladetec/protifolio-blog-posts.git
cd protifolio-blog-posts
python3 -m venv venv && source venv/bin/activate
make init
make serve
```

## Links

[Portifolio - Blog - Local](http://localhost:5000/)

### COMO FAZER DEPLOY NO HEROKU

1. Pré condiçaõ ter uma conta no Heroku e Heroku-CLI, instalado
2. Rode o ambiente com os comandos.

### NO TERMINAL

```
heroku login
heroku create <nome_do_projeto> --buildpack heroku/python
git push heroku main
```

#### OBS: adicione dentro do arquivo Procfile

```
web: gunicorn app:app
```
