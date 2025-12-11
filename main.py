from Publisher import Publisher
from Subscriber import Subscriber
import threading

def subscriberMenu(Subscriber):
    while True:
        print("\n=== MENU DO SUBSCRIBER ===")
        print("1 - Listar episodios recebidos")
        print("2 - Sair")
        op = input("Escolha uma opcao: ")

        if op == "1":
            subscriber.show_catalog()
        elif op == "2":
            print("Encerrando...")
            exit()
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    publisher = Publisher()
    subscriber = Subscriber()

    publisher.adicionarSubscriber(subscriber)

    # Thread do publisher para gerar episodios
    t = threading.Thread(target=publisher.publicar)
    t.daemon = True
    t.start()

    subscriberMenu(subscriber)
