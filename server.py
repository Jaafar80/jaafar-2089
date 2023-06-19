import socket,threading

quiz_questions = {
    'BSC performs all the softer hand-over for MSs moving between BTSs in its control.': 'f',
    'Hand over may result in call dropping.': 't',
    'Co-channel reuse ratio depends upon the raduises of the co-channel cells.': 't',
    'There is need to use any mobility managment between in progress calls inside the cell.': 'f',
    'Slow frequency hopper is a part of BSC block diagram.': 'f',
    'The frequency hopping used in GSM may be cyclic hopping.': 't',
    'Any cellular operation starts using BCCH.': 'f',
    'Frequency correction burst contains S bits.': 'f',
    'In GSM system, the access burst has the longest guard bits.': 't',
    'Burst of all users must reach the BS at the same time.': 'f',
    'Burst in GSM can have a different length.': 'f',
    'Any registered user must have a record in HLR.': 't',
    'Using TRAU does not affect the performance of the air interface.': 't',
    'SRES is an essential data of GSN SIM card.': 'f',
    'Authentication keys are not a permanent SIM data.': 'f',
    'GSM specifies four databases.': 't',
    'For GSM system, TDMA is used on the Abis interface.': 'f',
    'In cellular system radio units are housed in BTSs.': 't',
    'Both MAHO and NCHO can be used in GSM.': 'f',
    'A HO operation can be initiated even if the MS is still unmoved.': 't'
}

client_scores = {}

def handle_client(client_soc, client_address):
    try:
        client_soc.send(str(len(quiz_questions)).encode())

        for question in quiz_questions:
            client_soc.send(question.encode())

            client_ans = client_soc.recv(1024).decode().strip()

            if client_ans.lower() == quiz_questions[question].lower():
                client_scores[client_address] = client_scores.get(client_address, 0) + 1

        score = client_scores.get(client_address, 0)
        client_soc.send(f"Score: {score}/{len(quiz_questions)}\n".encode())

    except ConnectionAbortedError:
        print(f"Connection aborted by the client: {client_address}")

    client_soc.close()
    print(f"The client got disconnected.: {client_address}")

def start_server():
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 2323)
    server_soc.bind(server_address)

    server_soc.listen(5)
    print("The server has been initiated and is awaiting connections.")

    while True:
        client_socket, client_address = server_soc.accept()
        print(f"Connected to {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    start_server()


