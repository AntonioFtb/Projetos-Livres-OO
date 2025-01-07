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


1. **Executar o código**:
   - Clone ou baixe este repositório para sua máquina.
   - Abra o terminal e navegue até o diretório do projeto.
   - Execute o script:
     ```bash
     python app.py
     ```

2. **Interação com o App**:
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




