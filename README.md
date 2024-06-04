# DockerProject em Ubuntu 22.04
## Descrição do Projeto:
1- Saber usar uma imagem do DockerHub.
2- Escrever uma pequena aplicação e publicar para o dockerhub.
3- Usar o docker swarm na aplicação.
4- Um colega usa a imagem feita no tópico 2.

A imagem do tópico 1 consiste em um website em https (com ssl) em que se irá usar o Nginx com uma simples identificação pessoal.

A aplicação do tópico 2 consiste em um tradutor das 7 cores do arco-íris em que existe a opção de:
Português <--> Inglês
Português <--> Francês
Inglês <--> Francês

#Step-by-step Guide:
## 1ª Máquina [Manager] (docker1.enta.pt)
Os seguintes comandos estão em sequência para a realização do projeto: 

1. Atualizar os pacotes da máquina:
```
sudo apt update && sudo apt upgrade -y
```
2. Alterar o hostname da máquina:
```
sudo hostnamectl set-hostname docker1.enta.pt
```
3. Reiniciar a máquina para concluir a atualização dos pacotes:
```
sudo reboot
```
4. Neste passo iremos realizar o tópico 1 começando por criar e entrar na pasta do projeto:
```
mkdir nginx-ssl
cd nginx-ssl
mkdir html
mkdir ssl
```
5. Já dentro da pasta criada iremos criar os ficheiros necessários (Dentro dos ficheiros usar o código presente neste repositório):
```
nano Dockerfile
nano nginx.conf
cd html
nano index.html
cd ~/nginx-ssl/ssl
```
6. Iremos agora criar os certificados para o HTTPS (selfsigned):
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout docker1.enta.pt.key -out docker1.enta.pt.crt
```
6. Após os ficheiros estarem devidamente criados iremos criar a imagem do Docker: 
```
docker build -t rsr2004/nginxssl .
```
7. Depois de termos a imagem criada iremos executar o container do Docker:
```
docker run -d -p 5001:443 rsr2004/nginxssl
```
8. Num browser pesquisar o seguinte URL e verificar se está a funcionar:
```
https://100.28.10.242:5000/
```
