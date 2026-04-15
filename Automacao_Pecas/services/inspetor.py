# Importamos as regras de qualidade que você criou no config.py
from config import CRITERIOS_QUALIDADE

class Inspetor:
    """Motor de regras para validação de qualidade."""
    
    @staticmethod
    def inspecionar_peca(peca):
        falhas = [] # Lista para anotar os defeitos encontrados
        
        # 1. Teste de Peso
        if not (CRITERIOS_QUALIDADE["peso_min_g"] <= peca.peso_g <= CRITERIOS_QUALIDADE["peso_max_g"]):
            falhas.append("REJEITADA_PESO")
            
        # 2. Teste de Cor
        if peca.cor not in CRITERIOS_QUALIDADE["cores_aceitas"]:
            falhas.append("REJEITADA_COR")
            
        # 3. Teste de Dimensões (Comprimento, Largura e Altura)
        if not (CRITERIOS_QUALIDADE["comp_min_mm"] <= peca.comprimento_mm <= CRITERIOS_QUALIDADE["comp_max_mm"]) or \
           not (CRITERIOS_QUALIDADE["larg_min_mm"] <= peca.largura_mm <= CRITERIOS_QUALIDADE["larg_max_mm"]) or \
           not (CRITERIOS_QUALIDADE["alt_min_mm"] <= peca.altura_mm <= CRITERIOS_QUALIDADE["alt_max_mm"]):
            falhas.append("REJEITADA_DIMENSAO")
            
        # 4. O Veredito
        if not falhas:
            peca.status = "APROVADA"
        elif len(falhas) > 1:
            peca.status = "REJEITADA_MULTIPLA"
            peca.motivos_rejeicao = falhas
        else:
            peca.status = falhas[0] # Pega o único erro que deu
            peca.motivos_rejeicao = falhas
            
        return peca.status