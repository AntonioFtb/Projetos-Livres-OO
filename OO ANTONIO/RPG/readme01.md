# Cadastro de Personagens RPG

Este projeto é uma aplicação gráfica em Python, utilizando o módulo `tkinter` para criar uma interface para o cadastro e gerenciamento de personagens de RPG. Ele permite adicionar, remover, visualizar detalhes e reviver personagens, além de redistribuir seus atributos e iniciar combates.

## Funcionalidades

- **Cadastro de Personagens**: O usuário pode criar personagens do tipo Guerreiro, Mago ou Arqueiro, fornecendo o nome do personagem.
- **Gerenciamento de Personagens**: 
  - Ver detalhes dos personagens, como Vida, Mana, Ataque e Defesa.
  - Remover personagens do cadastro.
  - Reviver personagens mortos.
  - Redistribuir os atributos dos personagens.
- **Combate**: Iniciar um combate entre dois personagens.
- **Armazenamento de Dados**: Todos os dados dos personagens são salvos em um arquivo JSON, permitindo que as informações sejam carregadas automaticamente na próxima execução do programa.

## Como Executar

1. **Instalar dependências**:
   - Certifique-se de ter o Python 3 instalado. Caso não tenha, baixe [aqui](https://www.python.org/downloads/).
   - O projeto utiliza a biblioteca `tkinter`, que geralmente vem pré-instalada com o Python. Se necessário, instale usando:
     ```bash
     pip install tk
     ```

2. **Executar o código**:
   - Clone ou baixe este repositório para sua máquina.
   - Abra o terminal e navegue até o diretório do projeto.
   - Execute o script:
     ```bash
     python app.py
     ```

3. **Interação com o App**:
   - Na interface gráfica, você pode adicionar personagens, visualizar detalhes, reviver ou remover personagens, entre outras opções.

## Estrutura do Código

### Classes

- **Personagem**: Classe base para todos os personagens com atributos como nome, vida, mana, ataque e defesa. Também possui métodos para ataque, receber dano, reviver e aumentar atributos.
  
- **Guerreiro**: Subclasse de `Personagem` com atributos específicos para o tipo Guerreiro (mais vida e ataque).

- **Mago**: Subclasse de `Personagem` com atributos específicos para o tipo Mago (mais mana e ataque mágico).

- **Arqueiro**: Subclasse de `Personagem` com atributos específicos para o tipo Arqueiro (ataque de longo alcance com arco).

- **CadastroRPG**: Classe que gerencia o cadastro de personagens, com métodos para carregar e salvar dados, adicionar e remover personagens.

- **App**: Classe principal que cria a interface gráfica com tkinter, gerenciando as interações do usuário com o sistema.

## Funcionalidades de Combate

- **Guerreiro**: Realiza ataques baseados em seu ataque físico, que é reduzido pela defesa do oponente.
- **Mago**: Realiza ataques mágicos que também utilizam mana, reduzidos pela defesa do oponente.
- **Arqueiro**: Realiza ataques à distância com arco, baseados no ataque físico, também reduzido pela defesa do oponente.

## Como Contribuir

Sinta-se à vontade para contribuir com este projeto, seja corrigindo bugs, sugerindo melhorias ou adicionando novas funcionalidades. Para isso, basta seguir os seguintes passos:

1. Faça um fork deste repositório.
2. Crie uma branch para sua modificação (`git checkout -b minha-modificacao`).
3. Faça suas modificações.
4. Faça commit das mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
5. Envie para o repositório remoto (`git push origin minha-modificacao`).
6. Abra um Pull Request.



