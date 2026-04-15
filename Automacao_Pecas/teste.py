from models.peca import Peca
from services.inspetor import Inspetor
from services.triagem import SistemaTriagem

# Iniciamos a nossa esteira de triagem
triagem = SistemaTriagem()

print("--- LIGANDO A ESTEIRA (12 PEÇAS) ---")

# Isso vai repetir 12 vezes (do número 1 até o 12)
for numero in range(1, 13):
    # Criamos uma peça boa (peso 100g, azul, medidas corretas)
    # O f"P-{numero:03d}" cria nomes automáticos: P-001, P-002, P-003...
    peca = Peca(f"P-{numero:03d}", 100, "Azul", 120, 50, 40)
    
    # O Inspetor avalia
    Inspetor.inspecionar_peca(peca)
    
    # O Braço robótico (Triagem) tenta guardar
    if peca.status == "APROVADA":
        triagem.alocar_peca(peca)
        print(f"Peça {peca.id_peca} -> Aprovada e embalada.")

print("\n--- RELATÓRIO DO ARMAZÉM ---")
print(f"Total de caixas utilizadas: {len(triagem.caixas)}")

# Vamos olhar dentro do armazém como ficaram as caixas
for caixa in triagem.caixas:
    status_caixa = "Aberta" if caixa.aberta else "Fechada"
    print(f"Caixa {caixa.id_caixa} | Status: {status_caixa} | Peças dentro: {len(caixa.pecas)}")