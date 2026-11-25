# :speech_balloon: Chat_Py

Chat em grupo por linha de comando, em Python puro (só a biblioteca padrão).
Um servidor TCP recebe as mensagens e repassa para todos os clientes
conectados.

Projeto de estudo de sockets. As quatro versões antigas (v1–v4) foram
substituídas por esta, que reúne o melhor delas: chat em grupo com threads e
enquadramento de mensagens.

## :rocket: Como usar

Precisa de Python 3.10+.

**1. Inicie o servidor** (na máquina que vai hospedar):

```sh
python server.py                 # escuta em 0.0.0.0:1500
python server.py --port 5000
```

**2. Conecte os clientes** (em qualquer máquina que alcance o servidor):

```sh
python client.py --host IP_DO_SERVIDOR
python client.py --host 192.168.0.10 --port 1500 --name Lucas
```

Digite e aperte Enter para enviar. Para sair, digite `0` e Enter (ou Ctrl+C).

Para testar na mesma máquina, rode o servidor e abra dois terminais com
`python client.py --host 127.0.0.1`.

## :package: Arquivos

| Arquivo | Função |
| --- | --- |
| `server.py` | Servidor: aceita conexões e repassa as mensagens |
| `client.py` | Cliente: uma thread recebe, a principal envia |
| `protocol.py` | Enquadramento das mensagens (prefixo de tamanho + UTF-8) |

## :mag: O que mudou em relação às versões antigas

- **Chat em grupo** com repasse do servidor para todos (as v1–v3 eram ponto a ponto)
- **Enquadramento de mensagens**: cada mensagem leva o tamanho no cabeçalho,
  então não há mais mensagens cortadas ou grudadas (problema comum em TCP)
- Entradas e saídas anunciadas para todos, com desconexão tratada sem travar
- Host e porta por argumentos de linha de comando, sem variáveis globais
