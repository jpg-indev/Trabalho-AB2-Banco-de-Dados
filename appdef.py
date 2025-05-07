import sqlite3

def carregar_banco(dadosvoos):
    try:
        conexao = sqlite3.connect("banco_de_dados.db")
        cursor = conexao.cursor()
        with open(dadosvoos, 'r', encoding='utf-8') as arquivo:
            script_sql = arquivo.read()
            cursor.executescript(script_sql)
        conexao.commit()
        print("Banco de dados carregado com sucesso.")
    except sqlite3.Error as erro:
        print(f"Erro ao carregar o banco de dados: {erro}")
    finally:
        conexao.close()

def listar_passageiros_voos():
    consulta = '''
    SELECT p.nome AS passageiro, a.numero_voo, c.nome AS companhia
    FROM Passageiros p
    JOIN Aviao a ON p.numero_voo = a.numero_voo
    JOIN CompanhiaAerea c ON a.companhia_id = c.id;
    '''
    executar_consulta(consulta, descricao="Passageiros e seus voos")

def contar_passageiros_por_companhia():
    consulta = '''
    SELECT c.nome AS companhia, COUNT(p.id) AS total_passageiros
    FROM Passageiros p
    JOIN Aviao a ON p.numero_voo = a.numero_voo
    JOIN CompanhiaAerea c ON a.companhia_id = c.id
    GROUP BY c.nome;
    '''
    executar_consulta(consulta, descricao="Passageiros por Companhia")

def mostrar_voos_extremos():
    consulta = '''
    SELECT MIN(data_viagem) AS primeira_viagem, MAX(data_viagem) AS ultima_viagem
    FROM Passagens;
    '''
    try:
        conexao = sqlite3.connect("banco_de_dados.db")
        cursor = conexao.cursor()
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        print("\nDatas dos voos:")
        print(f"Mais próximo: {resultado[0]}")
        print(f"Mais distante: {resultado[1]}")
    except sqlite3.Error as erro:
        print(f"Erro: {erro}")
    finally:
        conexao.close()

def executar_consulta(consulta, descricao="Resultado"):
    try:
        conexao = sqlite3.connect("banco_de_dados.db")
        cursor = conexao.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        print(f"\n{descricao}")
        for linha in resultados:
            print(" - ".join(str(valor) for valor in linha))
    except sqlite3.Error as erro:
        print(f"Erro na consulta: {erro}")
    finally:
        conexao.close()

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Carregar banco de dados")
        print("2. Listar passageiros com voo e companhia")
        print("3. Contar passageiros por companhia")
        print("4. Mostrar voo mais próximo e mais distante")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_arquivo = input("Digite o nome do arquivo .sql: ")
            carregar_banco(nome_arquivo)
        elif opcao == "2":
            listar_passageiros_voos()
        elif opcao == "3":
            contar_passageiros_por_companhia()
        elif opcao == "4":
            mostrar_voos_extremos()
        elif opcao == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
