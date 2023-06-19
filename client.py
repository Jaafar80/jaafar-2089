import socket

def start_cli():
    server_host = 'localhost'
    server_port = 2323

    client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_soc.connect((server_host, server_port))
        print(f"Connected to server {server_host}:{server_port}")

        num_questions = int(client_soc.recv(1024).decode())

        for i in range(num_questions):
            question = client_soc.recv(1024).decode()

            answer = input(f"{question}: ")

            client_soc.sendall(answer.encode())

        final_score = client_soc.recv(1024).decode()
        print(f"Final score: {final_score}")

    except ConnectionRefusedError:
        print("Failed to connect to the server.")
    finally:
        client_soc.close()

if __name__ == '__main__':
    start_cli()
