import csv
from models.peca import Peca

class ImportadorCSV:
    """Ferramenta para ler planilhas e colocar as peças na esteira."""
    
    @staticmethod
    def carregar_lote(caminho_arquivo):
        pecas_carregadas = []
        try:
            # Abre o arquivo CSV em modo de leitura ('r' de read)
            with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
                # O DictReader é mágico: ele usa a primeira linha (cabeçalho) como nome para as colunas
                leitor = csv.DictReader(arquivo)
                
                # Para cada linha da planilha, construímos uma peça
                for linha in leitor:
                    peca = Peca(
                        id_peca=linha['id_peca'],
                        peso_g=float(linha['peso_g']),
                        cor=linha['cor'],
                        comprimento_mm=float(linha['comprimento_mm']),
                        largura_mm=float(linha['largura_mm']),
                        altura_mm=float(linha['altura_mm'])
                    )
                    pecas_carregadas.append(peca) # Adiciona a peça pronta na lista
                    
            return pecas_carregadas
            
        except FileNotFoundError:
            print(f"\n⚠️ ERRO: O arquivo '{caminho_arquivo}' não foi encontrado.")
            return []
        except Exception as e:
            print(f"\n⚠️ ERRO inesperado ao ler a planilha: {e}")
            return []