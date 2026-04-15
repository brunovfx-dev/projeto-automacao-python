from models.peca import Peca
from services.inspetor import Inspetor
from services.triagem import SistemaTriagem

def exibir_menu():
    """Mostra as opções do painel exigidas no projeto."""
    print("\n" + "="*50)
    print("🏭 SISTEMA DE CONTROLE DE PRODUÇÃO 🏭")
    print("="*50)
    print("[1] Cadastrar nova peça")
    print("[2] Listar peças aprovadas/reprovadas")
    print("[3] Remover peça cadastrada")
    print("[4] Listar caixas fechadas")
    print("[5] Gerar relatório final")
    print("[0] Sair")
    print("="*50)

def main():
    triagem = SistemaTriagem()
    todas_pecas = [] # Armazena o histórico de todas as peças do turno
    contador_pecas = 1 

    while True:
        exibir_menu()
        opcao = input("Escolha a operação: ")

        if opcao == '1':
            print("\n--- 1. CADASTRAR NOVA PEÇA ---")
            try:
                peso = float(input("Peso (g): "))
                cor = input("Cor (ex: azul, verde): ").lower()
                comp = float(input("Comprimento (mm): "))
                # Largura e Altura preenchidas automaticamente pois não foram exigidas
                larg = 50 
                alt = 50

                id_peca = f"P-{contador_pecas:03d}"
                nova_peca = Peca(id_peca, peso, cor, comp, larg, alt)

                Inspetor.inspecionar_peca(nova_peca)
                todas_pecas.append(nova_peca) # Salva no histórico geral

                if nova_peca.status == "APROVADA":
                    triagem.alocar_peca(nova_peca)
                    print(f"✅ SUCESSO: Peça {id_peca} APROVADA e embalada!")
                else:
                    print(f"❌ REJEITADA: Peça {id_peca}. Motivo: {nova_peca.motivos_rejeicao}")

                contador_pecas += 1 
            except ValueError:
                print("⚠️ ERRO: Digite apenas números para peso e comprimento.")

        elif opcao == '2':
            print("\n--- 2. LISTA DE PEÇAS PROCESSADAS ---")
            if not todas_pecas:
                print("Nenhuma peça foi processada ainda.")
            for p in todas_pecas:
                print(p)

        elif opcao == '3':
            print("\n--- 3. REMOVER PEÇA DO SISTEMA ---")
            id_remover = input("Digite o ID da peça que deseja remover (ex: P-001): ")
            peca_encontrada = None
            
            # Procura a peça na lista
            for p in todas_pecas:
                if p.id_peca == id_remover:
                    peca_encontrada = p
                    break
            
            if peca_encontrada:
                todas_pecas.remove(peca_encontrada)
                print(f"✅ A peça {id_remover} foi removida do histórico do sistema.")
            else:
                print("⚠️ Peça não encontrada. Verifique o ID digitado.")

        elif opcao == '4':
            print("\n--- 4. RELATÓRIO DE CAIXAS FECHADAS ---")
            caixas_fechadas = [c for c in triagem.caixas if not c.aberta]
            if not caixas_fechadas:
                print("Nenhuma caixa foi fechada ainda. (Capacidade: 10 peças).")
            for c in caixas_fechadas:
                print(f"📦 Caixa {c.id_caixa} | Status: Fechada | Peças dentro: {len(c.pecas)}")

        elif opcao == '5':
            print("\n--- 5. RELATÓRIO FINAL DE PRODUTIVIDADE ---")
            aprovadas = sum(1 for p in todas_pecas if p.status == "APROVADA")
            reprovadas = len(todas_pecas) - aprovadas
            print(f"Total de peças processadas no turno: {len(todas_pecas)}")
            print(f"🟢 Total Aprovadas: {aprovadas}")
            print(f"🔴 Total Reprovadas: {reprovadas}")
            print(f"📦 Total de Caixas Utilizadas (Abertas e Fechadas): {len(triagem.caixas)}")

        elif opcao == '0':
            print("\nDesligando a esteira... Fim do turno!")
            break 
            
        else:
            print("\n⚠️ Opção inválida. Escolha um número de 0 a 5.")

if __name__ == "__main__":
    main()