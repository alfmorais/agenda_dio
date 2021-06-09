# Desenvolvimento Web com Django
# Digital Innovation One

## Requisitos Básicos
- Linus, Windows, OSX
- Lógica de Programação
- Possuir fundamentos em Python
- Noções Básicas de HTML, CSS e JavaScript

## Agenda

### Objetivo do Curso
1. Aprender mais sobre sistemas web
2. Aprender a utilizar Python para desenvolvimento Web
3. Aprender o framework Django
4. Aprender a manipular informações em Banco de Dados da aplicação web.

### Sistema Web
1. São softwares/aplicações hospedadas na internet/intranet onde o usuário pode acessar atráves de requisições _http_ por um navegador.
2. Sistema web permitem ser acessados sem a necessidade de download e instalação da aplicação. 
3. Outra definição de aplicação web é onde tudo é processado em algum servidor. 

### Vantagens de um sistema Web
1. É seguro, a aplicação e banco são hospedadas em servidores em locais especializados, além de poder contar com certificados de segurança. 
2. Sistema web são mais acessíveis já que não necessitam realizar downloads e nem baixar dependencias para sua utilização. 
3. Mais rapido e menos trabalhoso para disponibilizações de novas atualizações. 

### Python para Web
1. Python é uma linguagem que é utilizada em muitos seguimentos, como ciência de dados, administrações de sistemas, desenvolvimentos de softwares desktops (GUI), jogos, aplicativos e é claro para sistemas Web.
2. Python tem crescido cada vez mais no desenvolvimento de aplicações web muito por conta de  seus ótimos frameworks, onde o mais usado é o Django.
3. Além do Django, existem outros frameworks que auxiliam no desenvolvimento Web com Python que também são muito populares, como: Flask, Pyramid, Tornado, Web2py e Bottle.

### Framework Django
1. Django é framework web Python de alto nível que incentiva o rápido desenvolvimento e um design limpo. 
2. O Django abstrai muito do trabalho do desenvolvedor, devido a grande funcionalidade na parte de desenvolvimento web, possibilitando o desenvolvedor focar apenas no código de sua aplicação. 
3. Django é gratuito e Open Source.
4. Django é framework mais popular no mercado
5. [Documentação Django](https://docs.djangoproject.com/en/3.2/)

## Diretório de um projeto Django

_IMAGEM_

### admin.py
* Interface administrativa gerada automaticamente pelo Django
* Ele lê os metadados que estão nos models e fornece uma interface poderosa e pronta para manipulação de dados.

### settings.py
* É responsável pelas configurações do Django
* Nele é possivél configurar por exemplo apps, conexão com o banco de dados, templates, time zone, cache, segurança, arquivos estáticos, etc.

### urls.py
* É um SCHEMA de URL
* Responsável por gerenciar as rotas de URL, onde é possivel configurar pra onde cada rota será executada.
* É uma forma limpa e elegante de gerenciar URLs.

### wsgi.py
* Web Server Gateway Interface - Interface de porta de entrada do servidor web
* Plataforma padrão para aplicações web em Python 
* Serve de interface do servidor web e a aplicações web
* O Django com o comando _startproject_ inicia uma configuração WSGI padrão para que se possa executar sua aplicação web. 
* Quando inicia a aplicação Django com o comando runserver é iniciado um servidor de aplicação web leve. Esse servidor é especializada pela configuração WSGI_APPLICATION 

### manage.py
* É um wrapper em volta do django-admin.py
* Ele delega tarefas para o django-admin.py
* Responsável por colocar o pacote do projeto no sys.path
* Ele define a váriavel de ambiente DJANGO_SETTINGS_MODULE que então aponta para o arquivo settings.py
* Por isso, o manage.py é gerado automaticamente junto ao projeto, para facilitar o uso de comandos do django-admin.py (comandos administativos)

_lista de comandos_

### models.py
* Define o modelo de dados inteiramente em Python
* Faz a abstração dos objetos de banco de dados para o Python, transformando todas as tabelas em classes e os acessos são feito utilizando linguagem Python, onde o Django realiza a transformação para SQL.

### tests.py
<p>Um local convencional para os testes de um aplicativo é no arquivo tests.py do aplicativo; o sistema de teste encontrará automaticamente os testes em qualquer arquivo cujo nome comece com teste.</p>

### views.py
* Responsável por processar e retornar uma resposta para o cliente que fez a requisição. 

### STATIC
* Responsável por armazenar os arquivos estáticos
* CSS, JavaScript, Imagens

### TEMPLATES
* Responsável por armazenar os arquivos HTML
* O Diretório templates é diretório padrão para armazenamos todo o conteúdo HTML da nossa aplicação.

## Criando ambiente virtual
1. python -m venv dev_web_django
2. dev_web_django/Scripts/Activate

## Instalando o Django
1. pip intall django
_imagem_

## Alfredo de Morais | Desenvolvedor de Aplicações Python
