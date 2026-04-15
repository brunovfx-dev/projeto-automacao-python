class Caixa:
    """Representa uma caixa de armazenamento para peças aprovadas."""
    
    def __init__(self, id_caixa, capacidade_maxima):
        self.id_caixa = id_caixa
        self.capacidade_maxima = capacidade_maxima
        self.pecas = [] # A caixa começa vazia (uma lista vazia)
        self.aberta = True # A caixa começa aberta

    def adicionar_peca(self, peca):
        # Só adiciona se a caixa estiver aberta e com espaço
        if self.aberta and len(self.pecas) < self.capacidade_maxima:
            self.pecas.append(peca) # Coloca a peça dentro da caixa
            
            # Se encheu, fecha a caixa automaticamente
            if len(self.pecas) == self.capacidade_maxima:
                self.aberta = False 
            return True # Retorna Verdadeiro indicando que deu certo
            
        return False # Retorna Falso se a caixa estiver cheia ou fechada