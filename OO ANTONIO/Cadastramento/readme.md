
# Sistema de Cadastramento

Este é um projeto de cadastramento simples, desenvolvido em Python, que permite a gestão de usuários. O sistema suporta diferentes tipos de usuários, como administradores e usuários comuns, além de funções para cadastro, listagem, busca e exclusão.

---

## Funcionalidades

- **Cadastrar Usuários**: Criação de usuários comuns ou administradores.
- **Listar Usuários**: Exibição de todos os usuários cadastrados.
- **Buscar Usuário**: Localização de um usuário pelo nome.
- **Excluir Usuário**: Remoção de usuários do sistema.

---

## Estrutura do Projeto

O projeto contém:
- **Classes Principais**:
  - `Usuario`: Classe base para os usuários.
  - `Admin`: Extensão de `Usuario` com permissões adicionais.
  - `UsuarioComum`: Subclasse de `Usuario` para usuários regulares.
- **Arquivos JSON**:
  - Armazena os dados de usuários em um arquivo chamado `usuarios.json`.

---

## Como Executar

1. Certifique-se de que o **Python 3.x** está instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/AntonioFtb/Projeto.git
