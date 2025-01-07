
# RPG - Sistema de Combate e Cadastro de Personagens

Este projeto é um jogo simples de RPG desenvolvido em Python, onde você pode criar personagens, personalizá-los com diferentes classes, iniciar combates entre eles, e salvar os dados dos personagens em um arquivo JSON para utilização futura.

## Funcionalidades

- **Criação de Personagens**: O usuário pode criar personagens de 3 classes diferentes: Guerreiro, Mago e Arqueiro. Cada classe possui atributos específicos como vida, mana, ataque e defesa.
- **Combate entre Personagens**: Inicie um combate entre dois personagens criados. O combate ocorre turnos alternados, com os personagens atacando um ao outro até que um deles morra.
- **Salvamento e Carregamento de Personagens**: Os dados dos personagens são salvos em um arquivo `personagens.json` e podem ser carregados automaticamente na próxima execução do programa.
- **Exibição de Personagens**: O usuário pode visualizar todos os personagens criados e suas informações.
- **Reviver Personagens**: Personagens mortos podem ser revividos automaticamente com a função `reviver()`.


1. **Interação com o App**:
   - O jogo irá apresentar um menu onde você pode:
     1. Criar um novo personagem.
     2. Listar personagens criados.
     3. Iniciar um combate entre dois personagens.
     4. Salvar e sair do jogo.

## Estrutura do Código

### Classes

- **Personagem**: Classe base para todos os personagens, com atributos como nome, vida, mana, ataque, defesa e métodos para atacar, receber dano e reviver.
  
- **Guerreiro**: Subclasse de `Personagem`, com atributos e habilidades específicas para o tipo Guerreiro (alta vida e ataque).

- **Mago**: Subclasse de `Personagem`, com atributos e habilidades específicas para o tipo Mago (alta mana e ataque mágico).

- **Arqueiro**: Subclasse de `Personagem`, com atributos e habilidades específicas para o tipo Arqueiro (ataque à distância e boa defesa).

- **Funções principais**:
  - **criar_personagem()**: Função que cria um novo personagem baseado na escolha do usuário.
  - **combate()**: Função que simula um combate entre dois personagens até que um deles morra.
  - **salvar_personagens()**: Função que salva os dados dos personagens em um arquivo JSON.
  - **carregar_personagens()**: Função que carrega os personagens salvos de um arquivo JSON.
  - **menu()**: Função principal que gerencia a interação com o usuário, permitindo criar personagens, visualizar, iniciar combates e salvar o progresso.


