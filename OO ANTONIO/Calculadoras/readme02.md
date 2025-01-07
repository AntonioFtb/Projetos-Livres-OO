# Calculadora Geométrica

Este projeto é uma calculadora de formas geométricas que permite calcular a área e o perímetro de diferentes figuras, como círculo, quadrado, retângulo e triângulo. Ele também mantém um histórico das operações realizadas, permitindo que os cálculos sejam salvos e carregados de um arquivo.

## Funcionalidades

- **Círculo**: Calcula a área e o perímetro do círculo com base no raio.
- **Quadrado**: Calcula a área e o perímetro do quadrado com base no lado.
- **Retângulo**: Calcula a área e o perímetro do retângulo com base na largura e altura.
- **Triângulo**: Calcula a área e o perímetro do triângulo com base na base, altura e nos lados.
- **Histórico de Cálculos**: O histórico de todas as operações realizadas é mantido, e pode ser visualizado a qualquer momento.
- **Salvar e Carregar Histórico**: O histórico pode ser salvo em um arquivo JSON e carregado novamente para a continuidade dos cálculos.


## Estrutura do Projeto

- **Forma**: Classe base abstrata para formas geométricas, com métodos para calcular área e perímetro.
- **Circulo, Quadrado, Retangulo, Triangulo**: Subclasses que implementam os métodos de cálculo de área e perímetro de cada forma geométrica.
- **CalculadoraGeometrica**: Classe principal que gerencia o histórico de cálculos e oferece funcionalidades para salvar e carregar o histórico.
- **menu()**: Função que exibe o menu de opções.
- **main()**: Função principal que executa a lógica do programa.

## Exemplo de Execução

```text
=== Calculadora de Formas Geométricas ===
1. Círculo
2. Quadrado
3. Retângulo
4. Triângulo
5. Mostrar Histórico
6. Salvar Histórico
7. Carregar Histórico
8. Sair
Escolha uma opção: 1
Digite o raio do círculo: 5
Área: 78.53975, Perímetro: 31.4159
