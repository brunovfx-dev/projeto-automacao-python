# Importamos a nossa planta da Caixa e o limite de peças do config
from models.caixa import Caixa
from config import CAPACIDADE_CAIXA

class SistemaTriagem:
    """Responsável por alocar as peças aprovadas nas caixas corretas."""
    
    def __init__(self):
        self.caixas = [] # Lista que guarda todas as caixas criadas
        self.caixa_atual = None # A caixa que está aberta no momento
        self.contador_caixas = 0 # Para dar nome às caixas (CX-001, CX-002...)

    def alocar_peca(self, peca):
        # Regra de ouro: só entra peça aprovada!
        if peca.status != "APROVADA":
            return False 

        # Se não tem caixa nenhuma, ou se a caixa atual já encheu e fechou...
        if self.caixa_atual is None or not self.caixa_atual.aberta:
            self.contador_caixas += 1
            # Cria uma nova caixa (ex: CX-001)
            nova_caixa = Caixa(f"CX-{self.contador_caixas:03d}", CAPACIDADE_CAIXA)
            self.caixas.append(nova_caixa) # Guarda ela no armazém
            self.caixa_atual = nova_caixa # Define ela como a caixa da vez

        # Coloca a peça na caixa atual
        self.caixa_atual.adicionar_peca(peca)
        return True