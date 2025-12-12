from Publisher import Publisher
from Subscriber import Subscriber
import threading
import os

def limparTela():
    os.system("cls")

def subscriberMenu(Subscriber):
    while True:
        print("1 - Listar episodios recebidos")
        print("2 - Sair")
        op = input("Escolha uma opcao: ")

        if op == "1":
            subscriber.mostrarCatalogo()
        elif op == "2":
            print("Programa Finalizado")
            exit()
        else:
            print("Opção invalida!")


if __name__ == "__main__":
    limparTela()
    publisher = Publisher()
    subscriber = Subscriber()

    publisher.adicionarSubscriber(subscriber)

    # Thread do publisher para gerar episodios
    t = threading.Thread(target=publisher.publicar)
    t.daemon = True
    t.start()

    subscriberMenu(subscriber)
