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

### settings.py
<p>Definições e Configurações para seu projeto Django.</p>

### urls.py
<p>Todas as URLS declarada para seu projeto Django.</p>

### wsgi.py
<p>Um ponto de entrada para servidores da web compatíveis com WSGI para atender ao seu projeto</p>

### manage.py
<p>Um utilitário de linha de comando que permite interagir com este projeto Django de várias maneiras.</p>

### models.py
<p>O arquivo models.py é um utilitário para definição de Banco de Dados. Atráves de classes escritas em python é possivel criar complexos banco de dados.</p>

### tests.py
<p>Um local convencional para os testes de um aplicativo é no arquivo tests.py do aplicativo; o sistema de teste encontrará automaticamente os testes em qualquer arquivo cujo nome comece com teste.</p>

### views.py
<p>O arquivo views.py é o local onde coloca os path de acesso a nossa aplicação.</p>

## Criando ambiente virtual
1. python -m venv dev_web_django
2. dev_web_django/Scripts/Activate

## Instalando o Django
