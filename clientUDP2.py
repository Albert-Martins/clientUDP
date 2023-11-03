import socket
import threading

# Endereço IP e porta do servidor
host = '192.168.3.52'  # Endereço IP do servidor
porta = 12345  # Porta do servidor

# Tamanho máximo de dados a serem recebidos de uma vez
tamanho_maximo = 1024

# Cria um objeto socket UDP para o cliente
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cliente_socket.bind((host, porta))

# Função para enviar mensagens para o servidor
def enviar_mensagens():
    while True:
        mensagem = input("Digite a mensagem a ser enviada: ")
        if mensagem == ".parar":
            print("Encerrando o cliente...")
            cliente_socket.sendto(mensagem.encode('utf-8'), (host, 1234))
            break
        elif mensagem.startswith(".destino"):
            destino_ip = input("Digite o endereço IP de destino: ")
        else:
            # Envia a mensagem para o servidor
            cliente_socket.sendto(mensagem.encode('utf-8'), (host, 1234))

# Thread para enviar mensagens para o servidor
thread_envio = threading.Thread(target=enviar_mensagens)
thread_envio.start()

while True:
    dados, endereco_servidor = cliente_socket.recvfrom(tamanho_maximo)
    mensagem = dados.decode('utf-8')
    print(f"Resposta do servidor ({endereco_servidor[0]}:{endereco_servidor[1]}): {mensagem}")

# Fecha o socket do cliente
cliente_socket.close()
print("Cliente encerrado. Adeus!")
