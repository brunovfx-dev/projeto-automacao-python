class Peca:
    """Representa uma peça física na linha de montagem."""
    
    def __init__(self, id_peca, peso_g, cor, comprimento_mm, largura_mm, altura_mm):
        # Aqui definimos os atributos que toda peça terá quando for criada
        self.id_peca = id_peca
        self.peso_g = peso_g
        self.cor = cor.lower() # Garante que a cor sempre fique em letras minúsculas
        self.comprimento_mm = comprimento_mm
        self.largura_mm = largura_mm
        self.altura_mm = altura_mm
        
        # Toda peça nasce com status PENDENTE até passar pelo Inspetor
        self.status = "PENDENTE"
        self.motivos_rejeicao = []

    def __str__(self):
        # Isso diz ao Python como mostrar a peça se pedirmos para "imprimir" ela
        return f"Peça {self.id_peca} | Cor: {self.cor} | Status: {self.status}"