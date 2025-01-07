import json

class Calculadora:
    def __init__(self):
        self.__historico = []  

    def adicionar_ao_historico(self, operacao, resultado):
        
        self.__historico.append({"operacao": operacao, "resultado": resultado})

    def mostrar_historico(self):
        
        if not self.__historico:
            print("Nenhum cálculo realizado ainda.")
        else:
            for idx, item in enumerate(self.__historico, start=1):
                print(f"{idx}. {item['operacao']} = {item['resultado']}")

    def salvar_historico(self, arquivo="historico.json"):
        
        with open(arquivo, "w") as file:
            json.dump(self.__historico, file, indent=4)
        print(f"Histórico salvo em '{arquivo}' com sucesso!")

    def carregar_historico(self, arquivo="historico.json"):
        
        try:
            with open(arquivo, "r") as file:
                self.__historico = json.load(file)
            print(f"Histórico carregado de '{arquivo}' com sucesso!")
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado. Nenhum histórico carregado.")

class Operacao:
    
    def calcular(self, a, b):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

class Soma(Operacao):
    def calcular(self, a, b):
        return a + b

class Subtracao(Operacao):
    def calcular(self, a, b):
        return a - b

class Multiplicacao(Operacao):
    def calcular(self, a, b):
        return a * b

class Divisao(Operacao):
    def calcular(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

def menu():
    print("\n=== Calculadora ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Mostrar Histórico")
    print("6. Salvar Histórico")
    print("7. Carregar Histórico")
    print("8. Sair")

def main():
    calc = Calculadora()
    operacoes = {
        1: Soma(),
        2: Subtracao(),
        3: Multiplicacao(),
        4: Divisao()
    }

    while True:
        menu()
        try:
            escolha = int(input("Escolha uma opção: "))

            if escolha in operacoes:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                operacao = operacoes[escolha]
                resultado = operacao.calcular(a, b)
                print(f"Resultado: {resultado}")
                calc.adicionar_ao_historico(f"{a} {operacao.__class__.__name__.lower()} {b}", resultado)

            elif escolha == 5:
                calc.mostrar_historico()

            elif escolha == 6:
                calc.salvar_historico()

            elif escolha == 7:
                calc.carregar_historico()

            elif escolha == 8:
                print("Saindo... Até mais!")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

if __name__ == "__main__":
    main()
