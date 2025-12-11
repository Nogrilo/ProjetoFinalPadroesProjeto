class Subscriber:
    def update(self, episodio):
        pass


class PodcastSubscriber(Subscriber):
    def __init__(self):
        self.catalogo = []

    # receber ep da publisher
    def update(self, episodio):
        print(f"[SUBSCRIBER] Recebido: {episodio}")
        self.catalogo.append(episodio)

    # consultar episodios
    def show_catalog(self):
        if not self.episodio:
            print("\nNenhum episódio no catálogo local.")
        else:
            print("\nCatalogo local de episódios:")
            for ep in self.catalogo:
                print(f" - {ep}")
