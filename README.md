# CRUD com Python

Nesse projeto é possível criar, visualizar, atualizar e remover clientes.

###  Testando o Projeto

1 - Clone o repositorio ou baixe o arquivo .zip.

2 - Crie sua máquina virtual usando os seguintes comandos: 
```
python3 -m venv venv_nomedamaquina 
```
Logo após criar a máquina virtual, rode o seguinte comando para ativar a mesma:
```
source venv_nomedamaquina/bin/activate
```

3 - É necessario gerar uma *Secret Key* e colar no arquivo *Settings.py* que se encontra na pasta *desafioSNet*. Copie a chave gerada e cole em SECRET_KEY na linha 23. 
Para obter essa chave, utilize o seguinte comando:
```
python -c "import secrets; print(secrets.token_urlsafe())"
```
> **Não esqueça que a chave deve estar entre aspas simples no arquivo settings.py.**

4 - Antes de rodar o servidor, é preciso criar as tabelas e as colunas, para isso, rode o seguinte comando:
```
python manage.py makemigrations && python manage.py migrate
 ```

5 - Para criar clientes pelo admin, você precisará criar um super usuário. Para isso, faça os seguintes comandos:
```
python manage.py createsuperuser OU
python manage.py createsuperuser --email admin@example.com --username admin
 ```
> **Você pode alterar o email e o username se quiser**

6 - Por fim, rode a aplicação: 
```
python manage.py runserver
 ```
