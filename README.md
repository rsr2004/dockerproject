# DockerProject em Ubuntu 22.04
## Descrição do Projeto:
1- Saber usar uma imagem do DockerHub.
2- Escrever uma pequena aplicação e publicar para o dockerhub.
3- Usar o docker swarm na aplicação.
4- Um colega usa a imagem feita no ponto 2.

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
4. Cria o certificado, neste passo é importante dar um nome referido á localização da máquina;
```
./easyrsa build-ca
```
5. Gera um pedido, aqui insere o nome que deste ao server;
```
./easyrsa gen-req enta nopass
```
6. Assina o certificado;
```
./easyrsa sign-req server enta
```
7. Passa o certificado para a máquina que necessita do certificado;
```
scp -i chave.pem /usr/share/easy-rsa/pki/issued/enta.crt ubuntu@10.0.9.101:/tmp
```
8. Passa a key para a máquina que necessita da key;
```
scp -i chave.pem /usr/share/easy-rsa/pki/private/enta.key ubuntu@10.0.9.101:/tmp
```
