import time
import random
import threading

class Publisher:
    def __init__(self):
        self.subscribers = []
        self.episodios = []
        self.running = True

    def adicionarSubscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def notificarSubscriber(self, episodios):
        for sub in self.subscribers:
            sub.update(episodios)

    def publicar(self):
        numeroEpisodio = 1
        while self.running:
            # intervalo aleatorio entre 3 e 7 segundos
            time.sleep(random.randint(3, 7))

            novoEpisodio = f"episodio{numeroEpisodio:02}"
            numeroEpisodio += 1

            self.episodios.append(novoEpisodio)
            print(f"\n[PUBLISHER] Novo episodio disponivel: {novoEpisodio}")

            self.notificarSubscriber(novoEpisodio)
