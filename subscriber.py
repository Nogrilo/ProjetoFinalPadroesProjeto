class Subscriber:
    def update(self, episodio):
        pass


class Subscriber(Subscriber):
    def __init__(self):
        self.catalogo = []

    # receber ep da publisher
    def update(self, episodio):
        print(f"[SUBSCRIBER] Recebido: {episodio}")
        self.catalogo.append(episodio)

    # consultar episodios
    def mostrarCatalogo(self):
        if not self.episodio:
            print("\nNenhum episodio no catalogo local.")
        else:
            print("\nCatalogo local de episodios:")
            for ep in self.catalogo:
                print(f" - {ep}")
