import pandas as pd
from datetime import datetime
import os

ARQUIVO = "gastos.xlsx"


def inicializar_arquivo():
    if not os.path.exists(ARQUIVO):
        df = pd.DataFrame(columns=["Data", "Categoria", "Descrição", "Valor"])
        df.to_excel(ARQUIVO, index=False)
        print("Arquivo criado: gastos.xlsx")

def registrar_gasto():
    data = input("Data (dd/mm/aaaa): ") or datetime.now().strftime("%d/%m/%Y")
    categoria = input("Categoria (Ex: Alimentação, Transporte, Lazer...): ")
    descricao = input("Descrição: ")
    valor = float(input("Valor (R$): "))

    novo_gasto = pd.DataFrame({
        "Data": [data],
        "Categoria": [categoria],
        "Descrição": [descricao],
        "Valor": [valor]
    })

    df = pd.read_excel(ARQUIVO)
    df = pd.concat([df, novo_gasto], ignore_index=True)
    df.to_excel(ARQUIVO, index=False)

    print(f"Gasto de R$ {valor:.2f} em {categoria} registrado!")

def visualizar_gastos():
    df = pd.read_excel(ARQUIVO)
    print("\n=== RESUMO GERAL ===")
    print(df.groupby("Categoria")["Valor"].sum())
    print("\nTotal Gasto: R$", df["Valor"].sum())

def main():
    inicializar_arquivo()
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
    main()
