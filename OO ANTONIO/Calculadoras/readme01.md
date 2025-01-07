# Calculadora com Histórico

Este projeto implementa uma calculadora simples com histórico de operações matemáticas. O código permite realizar operações de soma, subtração, multiplicação e divisão, com a opção de salvar, carregar e visualizar o histórico de cálculos feitos. O histórico é armazenado em um arquivo JSON.

## Funcionalidades

- **Operações Matemáticas**: A calculadora suporta quatro operações principais:
  - Soma
  - Subtração
  - Multiplicação
  - Divisão (com verificação para divisão por zero)
  
- **Histórico de Cálculos**: A cada operação realizada, o cálculo e o resultado são armazenados em um histórico.
  - **Mostrar Histórico**: Exibe o histórico de todas as operações realizadas.
  - **Salvar Histórico**: Permite salvar o histórico de operações em um arquivo JSON.
  - **Carregar Histórico**: Permite carregar o histórico de um arquivo JSON previamente salvo.

## Classes

### 1. `Calculadora`

A classe principal que gerencia o histórico de operações. 
- **Atributos**:
  - `__historico`: Uma lista privada que armazena o histórico das operações realizadas.

- **Métodos**:
  - `adicionar_ao_historico(operacao, resultado)`: Adiciona uma operação realizada ao histórico.
  - `mostrar_historico()`: Exibe todas as operações realizadas.
  - `salvar_historico(arquivo)`: Salva o histórico em um arquivo JSON.
  - `carregar_historico(arquivo)`: Carrega o histórico de um arquivo JSON.

### 2. `Operacao`

Classe base para todas as operações matemáticas. Define o método `calcular`, que deve ser implementado pelas subclasses.

### 3. Subclasses de `Operacao`

- **`Soma`**: Implementa a operação de soma.
- **`Subtracao`**: Implementa a operação de subtração.
- **`Multiplicacao`**: Implementa a operação de multiplicação.
- **`Divisao`**: Implementa a operação de divisão, com verificação para evitar divisão por zero.

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/Calculadora-com-Historico.git
