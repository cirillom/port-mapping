# Trabalho 1 - Script de Mapeamento

- Gustavo Moura S. de C. Ferreira - **12547792**
- Matheus Henrique Dias Cirillo - **12547750**

## Introdução

Este trabalho tem como objetivo desenvolver um script em Python para realizar o escaneamento de portas de um host, identificando portas abertas e os serviços associados. O script foi testado em um sistema Linux (Ubuntu 22.04.4 LTS), acessando uma máquina virtual Metasploitable configurada no VirtualBox. A utilização do Metasploitable permitiu a validação eficaz do script em um ambiente controlado e seguro, simulando um sistema com diversas vulnerabilidades e serviços em execução.

## Modo de Uso

Para executar o script, siga o seguinte formato:

```bash
python scan.py <host> <portas>
```

Onde `<portas>` é uma lista de um ou mais inteiros (e.g. 80) ou intervalo (e.g. 1:1000), separados por espaços. Por exemplo, o seguinte comando irá escanear as portas 80, 81, 82, 100 e 1000 do host `192.168.0.10`:

```bash
python scan.py 192.168.0.10 80:82 100 1000
```

## Teste na Máquina Virtual

Para a execução, foi utilizada o Linux Metasploitable disponibilizado. O comando de teste foi o seguinte:

```bash
python scan.py <ip> 1:65535
```

Abaixo, segue a saída gerada pelo script`.

```
Port 22 (TCP) is open (ssh)
Port 25 (TCP) is open (smtp)
Port 23 (TCP) is open (telnet)
Port 21 (TCP) is open (ftp)
Port 53 (TCP) is open (domain)
Port 80 (TCP) is open (http)
Port 111 (TCP) is open (sunrpc)
Port 139 (TCP) is open (netbios-ssn)
Port 445 (TCP) is open (microsoft-ds)
Port 513 (TCP) is open (login)
Port 514 (TCP) is open (shell)
Port 512 (TCP) is open (exec)
Port 1099 (TCP) is open (rmiregistry)
Port 1524 (TCP) is open (ingreslock)
Port 2049 (TCP) is open (nfs)
Port 2121 (TCP) is open (iprop)
Port 3306 (TCP) is open (mysql)
Port 3632 (TCP) is open (distcc)
Port 5432 (TCP) is open (postgresql)
Port 5900 (TCP) is open (Unknown service)
Port 6000 (TCP) is open (x11)
Port 6667 (TCP) is open (ircd)
Port 6697 (TCP) is open (ircs-u)
Port 8009 (TCP) is open (Unknown service)
Port 8180 (TCP) is open (Unknown service)
Port 8787 (TCP) is open (Unknown service)
Port 37603 (TCP) is open (Unknown service)
Port 53630 (TCP) is open (Unknown service)
Port 57333 (TCP) is open (Unknown service)
Port 59318 (TCP) is open (Unknown service)
```
