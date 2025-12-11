import time
import random
import threading

class PodcastPublisher:
    def __init__(self):
        self.subscribers = []
        self.episodios = []
        self.running = True

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def notify_subscribers(self, episodios):
        for sub in self.subscribers:
            sub.update(episodios)

    def start_publishing(self):
        numeroEpisodio = 1
        while self.running:
            # intervalo aleatório entre 3 e 7 segundos
            time.sleep(random.randint(3, 7))

            novoEpisodio = f"episodio{numeroEpisodio:02}"
            numeroEpisodio += 1

            self.episodios.append(novoEpisodio)
            print(f"\n[PUBLISHER] Novo episódio disponível: {novoEpisodio}")

            self.notify_subscribers(novoEpisodio)
