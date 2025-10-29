from main import inicializar_arquivo,registrar_gasto,visualizar_gastos
def menu():

    while True:
        print("\n===== GESTOR DE GASTOS =====")
        print("1. Registrar novo gasto")
        print("2. Ver resumo por categoria")
        print("3. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            registrar_gasto()
        elif opcao == "2":
            visualizar_gastos()
        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
            menu()



