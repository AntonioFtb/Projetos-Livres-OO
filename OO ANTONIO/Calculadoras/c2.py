import json

class Forma:

    def calcular_area(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

    def calcular_perimetro(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")

class Circulo(Forma):
    def __init__(self, raio):
        self.__raio = raio

    def calcular_area(self):
        return 3.14159 * (self.__raio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14159 * self.__raio

class Quadrado(Forma):
    def __init__(self, lado):
        self.__lado = lado

    def calcular_area(self):
        return self.__lado ** 2

    def calcular_perimetro(self):
        return 4 * self.__lado

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    def calcular_area(self):
        return self.__largura * self.__altura

    def calcular_perimetro(self):
        return 2 * (self.__largura + self.__altura)

class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.__base = base
        self.__altura = altura
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def calcular_area(self):
        return (self.__base * self.__altura) / 2

    def calcular_perimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3

class CalculadoraGeometrica:
    def __init__(self):
        self.__historico = []

    def adicionar_ao_historico(self, forma, tipo, area, perimetro):
        """Adiciona um cálculo ao histórico."""
        self.__historico.append({
            "forma": tipo,
            "dimensoes": forma.__dict__,
            "area": area,
            "perimetro": perimetro
        })

    def mostrar_historico(self):
       
        if not self.__historico:
            print("Nenhum cálculo realizado ainda.")
        else:
            for idx, item in enumerate(self.__historico, start=1):
                print(f"{idx}. Forma: {item['forma']} - Área: {item['area']} - Perímetro: {item['perimetro']}")

    def salvar_historico(self, arquivo="historico_formas.json"):
       
        with open(arquivo, "w") as file:
            json.dump(self.__historico, file, indent=4)
        print(f"Histórico salvo em '{arquivo}' com sucesso!")

    def carregar_historico(self, arquivo="historico_formas.json"):
        
        try:
            with open(arquivo, "r") as file:
                self.__historico = json.load(file)
            print(f"Histórico carregado de '{arquivo}' com sucesso!")
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado. Nenhum histórico carregado.")

def menu():
    print("\n=== Calculadora de Formas Geométricas ===")
    print("1. Círculo")
    print("2. Quadrado")
    print("3. Retângulo")
    print("4. Triângulo")
    print("5. Mostrar Histórico")
    print("6. Salvar Histórico")
    print("7. Carregar Histórico")
    print("8. Sair")

def main():
    calc = CalculadoraGeometrica()
    while True:
        menu()
        try:
            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                raio = float(input("Digite o raio do círculo: "))
                circulo = Circulo(raio)
                area = circulo.calcular_area()
                perimetro = circulo.calcular_perimetro()
                print(f"Área: {area}, Perímetro: {perimetro}")
                calc.adicionar_ao_historico(circulo, "Círculo", area, perimetro)

            elif escolha == 2:
                lado = float(input("Digite o lado do quadrado: "))
                quadrado = Quadrado(lado)
                area = quadrado.calcular_area()
                perimetro = quadrado.calcular_perimetro()
                print(f"Área: {area}, Perímetro: {perimetro}")
                calc.adicionar_ao_historico(quadrado, "Quadrado", area, perimetro)

            elif escolha == 3:
                largura = float(input("Digite a largura do retângulo: "))
                altura = float(input("Digite a altura do retângulo: "))
                retangulo = Retangulo(largura, altura)
                area = retangulo.calcular_area()
                perimetro = retangulo.calcular_perimetro()
                print(f"Área: {area}, Perímetro: {perimetro}")
                calc.adicionar_ao_historico(retangulo, "Retângulo", area, perimetro)

            elif escolha == 4:
                base = float(input("Digite a base do triângulo: "))
                altura = float(input("Digite a altura do triângulo: "))
                lado1 = float(input("Digite o lado 1 do triângulo: "))
                lado2 = float(input("Digite o lado 2 do triângulo: "))
                lado3 = float(input("Digite o lado 3 do triângulo: "))
                triangulo = Triangulo(base, altura, lado1, lado2, lado3)
                area = triangulo.calcular_area()
                perimetro = triangulo.calcular_perimetro()
                print(f"Área: {area}, Perímetro: {perimetro}")
                calc.adicionar_ao_historico(triangulo, "Triângulo", area, perimetro)

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