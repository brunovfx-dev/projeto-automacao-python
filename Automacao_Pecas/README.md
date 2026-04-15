# 🏭 Automação Digital: Gestão de Peças e Qualidade

## 📌 Explicação do Funcionamento
Este projeto é um protótipo em Python desenvolvido para automatizar a inspeção e o controle de qualidade em uma linha de montagem industrial. O sistema recebe os dados físicos de uma peça (peso, cor e comprimento) e, através de um algoritmo de validação, decide instantaneamente se a peça está **Aprovada** ou **Reprovada** com base nos limites de tolerância exigidos. As peças aprovadas são automaticamente alocadas em caixas (com capacidade máxima de 10 unidades), fechando a caixa automaticamente quando o limite é atingido.

## 🚀 Como rodar o programa
Para executar este sistema na sua máquina, siga os passos abaixo:

1. Certifique-se de ter o **Python 3** instalado em seu computador.
2. Faça o download ou clone este repositório para a sua máquina.
3. Abra o terminal (ou prompt de comando) e navegue até a pasta raiz do projeto.
4. Execute o arquivo principal com o seguinte comando:
   python main.py
5. O Menu Interativo será exibido no terminal. Utilize os números de `0` a `5` para navegar pelas opções e interagir com o sistema.

## 📊 Exemplos de Entradas e Saídas

**Exemplo de Entrada (Opção 1 - Cadastrar Peça):**
- Peso (g): `100`
- Cor: `azul`
- Comprimento (mm): `150`

**Exemplo de Saída Esperada (Aprovação):**
✅ SUCESSO: Peça P-001 APROVADA e embalada!

**Exemplo de Saída Esperada (Opção 5 - Relatório Final):**
--- 5. RELATÓRIO FINAL DE PRODUTIVIDADE ---
Total de peças processadas no turno: 1
🟢 Total Aprovadas: 1
🔴 Total Reprovadas: 0
📦 Total de Caixas Utilizadas (Abertas e Fechadas): 1