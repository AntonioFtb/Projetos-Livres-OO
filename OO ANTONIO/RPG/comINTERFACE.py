import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from typing import List


class Personagem:
    def __init__(self, nome: str, vida: int, mana: int, ataque: int, defesa: int):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.ataque = ataque
        self.defesa = defesa
        self.vivo = True  

    def atacar(self, outro):
        pass  
    
    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            self.vivo = False  

    def reviver(self):
     
        self.vida = 100  
        self.mana = 50 
        self.vivo = True  

    def aumentar_atributos(self):
        
        self.vida += 10
        self.ataque += 5
        self.defesa += 3

    def __str__(self):
        return f"{self.nome} (Vida: {self.vida}, Mana: {self.mana}, Ataque: {self.ataque}, Defesa: {self.defesa}, Vivo: {'Sim' if self.vivo else 'Não'})"

class Guerreiro(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, vida=150, mana=30, ataque=50, defesa=40)
    
    def atacar(self, outro: Personagem):
        dano = self.ataque - outro.defesa
        if dano > 0:
            outro.receber_dano(dano)
        return f"{self.nome} atacou {outro.nome} causando {dano} de dano."

class Mago(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, vida=100, mana=100, ataque=40, defesa=30)
    
    def atacar(self, outro: Personagem):
        dano = self.ataque + self.mana // 10 - outro.defesa
        if dano > 0:
            outro.receber_dano(dano)
        return f"{self.nome} atacou {outro.nome} causando {dano} de dano com magia."

class Arqueiro(Personagem):
    def __init__(self, nome: str):
        super().__init__(nome, vida=120, mana=50, ataque=45, defesa=35)
    
    def atacar(self, outro: Personagem):
        dano = self.ataque - outro.defesa
        if dano > 0:
            outro.receber_dano(dano)
        return f"{self.nome} atacou {outro.nome} causando {dano} de dano com arco."


class CadastroRPG:
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.personagens = self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.arquivo, 'r') as f:
                data = json.load(f)
                return [self.criar_personagem(p) for p in data]
        except FileNotFoundError:
            return []

    def salvar_dados(self):
        data = [self.personagem_para_dict(p) for p in self.personagens]
        with open(self.arquivo, 'w') as f:
            json.dump(data, f)

    def adicionar_personagem(self, personagem: Personagem):
        self.personagens.append(personagem)
        self.salvar_dados()

    def remover_personagem(self, nome: str):
        self.personagens = [p for p in self.personagens if p.nome != nome]
        self.salvar_dados()

    def personagem_para_dict(self, personagem: Personagem):
        return {
            'nome': personagem.nome,
            'vida': personagem.vida,
            'mana': personagem.mana,
            'ataque': personagem.ataque,
            'defesa': personagem.defesa
        }

    def criar_personagem(self, dados):
        tipo = dados.get('tipo', '')
        if tipo == 'Guerreiro':
            return Guerreiro(dados['nome'])
        elif tipo == 'Mago':
            return Mago(dados['nome'])
        elif tipo == 'Arqueiro':
            return Arqueiro(dados['nome'])
        else:
            return Personagem(dados['nome'], dados['vida'], dados['mana'], dados['ataque'], dados['defesa'])


class App(tk.Tk):
    def __init__(self, cadastro):
        super().__init__()
        self.cadastro = cadastro
        self.title("Cadastro de Personagens RPG")
        self.geometry("600x700")
        self.configure(bg="#f4f4f4")
        
       
        self.title_label = tk.Label(self, text="Cadastro de Personagens", font=("Arial", 20, "bold"), bg="#f4f4f4", fg="#4CAF50")
        self.title_label.pack(pady=10)
        
        
        self.lista_personagens = tk.Listbox(self, height=10, width=50, font=("Arial", 12), selectmode=tk.MULTIPLE)
        self.lista_personagens.pack(pady=10)

        
        self.frame_buttons = tk.Frame(self, bg="#f4f4f4")
        self.frame_buttons.pack(pady=10)

        self.ver_button = tk.Button(self.frame_buttons, text="Ver Detalhes", command=self.ver_detalhes, width=15, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.ver_button.grid(row=0, column=0, padx=10)
        
        self.remover_button = tk.Button(self.frame_buttons, text="Remover", command=self.remover_personagem, width=15, bg="#f44336", fg="white", font=("Arial", 12))
        self.remover_button.grid(row=0, column=1, padx=10)
        
        
        self.reviver_button = tk.Button(self.frame_buttons, text="Reviver Personagem", command=self.reviver_personagem, width=15, bg="#FF5722", fg="white", font=("Arial", 12))
        self.reviver_button.grid(row=1, column=0, padx=10)

        self.redistribuir_button = tk.Button(self.frame_buttons, text="Redistribuir Atributos", command=self.redistribuir_atributos, width=15, bg="#9C27B0", fg="white", font=("Arial", 12))
        self.redistribuir_button.grid(row=1, column=1, padx=10)
        
       
        self.combate_button = tk.Button(self.frame_buttons, text="Iniciar Combate", command=self.iniciar_combate, width=15, bg="#FF9800", fg="white", font=("Arial", 12))
        self.combate_button.grid(row=2, column=0, padx=10)

        
        self.frame_formulario = tk.Frame(self, bg="#f4f4f4")
        self.frame_formulario.pack(pady=20)

        self.nome_label = tk.Label(self.frame_formulario, text="Nome:", bg="#f4f4f4", font=("Arial", 12))
        self.nome_label.grid(row=0, column=0, padx=10)
        self.nome_entry = tk.Entry(self.frame_formulario, font=("Arial", 12))
        self.nome_entry.grid(row=0, column=1)

        self.tipo_label = tk.Label(self.frame_formulario, text="Tipo:", bg="#f4f4f4", font=("Arial", 12))
        self.tipo_label.grid(row=1, column=0, padx=10)
        self.tipo_var = tk.StringVar(value="Guerreiro")
        self.tipo_menu = tk.OptionMenu(self.frame_formulario, self.tipo_var, "Guerreiro", "Mago", "Arqueiro")
        self.tipo_menu.grid(row=1, column=1)

        self.adicionar_button = tk.Button(self, text="Adicionar Personagem", command=self.adicionar_personagem, width=20, bg="#008CBA", fg="white", font=("Arial", 12))
        self.adicionar_button.pack(pady=10)

        self.atualizar_lista()

    def adicionar_personagem(self):
        nome = self.nome_entry.get()
        tipo = self.tipo_var.get()

        if not nome:
            messagebox.showerror("Erro", "O nome não pode ser vazio.")
            return
        
        if tipo == "Guerreiro":
            personagem = Guerreiro(nome)
        elif tipo == "Mago":
            personagem = Mago(nome)
        elif tipo == "Arqueiro":
            personagem = Arqueiro(nome)

        self.cadastro.adicionar_personagem(personagem)
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_personagens.delete(0, tk.END)
        for p in self.cadastro.personagens:
            self.lista_personagens.insert(tk.END, f"{p.nome} - {p.__class__.__name__} - {'Vivo' if p.vivo else 'Morto'}")

    def ver_detalhes(self):
        try:
            selecionado = self.lista_personagens.curselection()
            if not selecionado:
                raise IndexError
            indice = selecionado[0]
            personagem = self.cadastro.personagens[indice]
            detalhes = f"Nome: {personagem.nome}\nVida: {personagem.vida}\nMana: {personagem.mana}\nAtaque: {personagem.ataque}\nDefesa: {personagem.defesa}"
            messagebox.showinfo("Detalhes do Personagem", detalhes)
        except IndexError:
            messagebox.showwarning("Erro", "Selecione um personagem.")

    def remover_personagem(self):
        try:
            selecionado = self.lista_personagens.curselection()
            if not selecionado:
                raise IndexError
            indice = selecionado[0]
            personagem = self.cadastro.personagens[indice]
            self.cadastro.remover_personagem(personagem.nome)
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Erro", "Selecione um personagem para remover.")

    def reviver_personagem(self):
        try:
            selecionado = self.lista_personagens.curselection()
            if not selecionado:
                raise IndexError
            indice = selecionado[0]
            personagem = self.cadastro.personagens[indice]
            personagem.reviver()  
            self.atualizar_lista()
            messagebox.showinfo("Reviver Personagem", f"{personagem.nome} foi revivido com sucesso!")
        except IndexError:
            messagebox.showwarning("Erro", "Selecione um personagem para reviver.")

    def redistribuir_atributos(self):
        try:
            selecionado = self.lista_personagens.curselection()
            if not selecionado:
                raise IndexError
            indice = selecionado[0]
            personagem = self.cadastro.personagens[indice]

            if not personagem.vivo:
                messagebox.showwarning("Erro", "O personagem está morto. Não é possível redistribuir os atributos.")
                return

       
            redistribuir_window = tk.Toplevel(self)
            redistribuir_window.title("Redistribuir Atributos")

            tk.Label(redistribuir_window, text="Vida:", font=("Arial", 12)).grid(row=0, column=0, padx=10)
            vida_entry = tk.Entry(redistribuir_window, font=("Arial", 12))
            vida_entry.grid(row=0, column=1)
            vida_entry.insert(0, str(personagem.vida))

            tk.Label(redistribuir_window, text="Ataque:", font=("Arial", 12)).grid(row=1, column=0, padx=10)
            ataque_entry = tk.Entry(redistribuir_window, font=("Arial", 12))
            ataque_entry.grid(row=1, column=1)
            ataque_entry.insert(0, str(personagem.ataque))

            tk.Label(redistribuir_window, text="Defesa:", font=("Arial", 12)).grid(row=2, column=0, padx=10)
            defesa_entry = tk.Entry(redistribuir_window, font=("Arial", 12))
            defesa_entry.grid(row=2, column=1)
            defesa_entry.insert(0, str(personagem.defesa))

            def salvar_atributos():
                try:
                    personagem.vida = int(vida_entry.get())
                    personagem.ataque = int(ataque_entry.get())
                    personagem.defesa = int(defesa_entry.get())
                    self.atualizar_lista()
                    redistribuir_window.destroy()
                    messagebox.showinfo("Atributos Atualizados", "Atributos atualizados com sucesso!")
                except ValueError:
                    messagebox.showwarning("Erro", "Por favor, insira valores válidos.")

            salvar_button = tk.Button(redistribuir_window, text="Salvar", command=salvar_atributos, width=15, bg="#4CAF50", fg="white", font=("Arial", 12))
            salvar_button.grid(row=3, columnspan=2, pady=10)

        except IndexError:
            messagebox.showwarning("Erro", "Selecione um personagem para redistribuir atributos.")

    def iniciar_combate(self):
        try:
            selecionados = self.lista_personagens.curselection()
            if len(selecionados) != 2:
                raise IndexError
            personagem1 = self.cadastro.personagens[selecionados[0]]
            personagem2 = self.cadastro.personagens[selecionados[1]]

            resultado = self.combater(personagem1, personagem2)
            messagebox.showinfo("Resultado do Combate", resultado)
        except IndexError:
            messagebox.showwarning("Erro", "Selecione dois personagens para o combate.")

    def combater(self, personagem1, personagem2):
        while personagem1.vida > 0 and personagem2.vida > 0:
            resultado_ataque1 = personagem1.atacar(personagem2)
            if personagem2.vida <= 0:
                personagem1.aumentar_atributos()
                return f"{personagem1.nome} venceu o combate!\n{resultado_ataque1}"

            resultado_ataque2 = personagem2.atacar(personagem1)
            if personagem1.vida <= 0:
                personagem2.aumentar_atributos() 
                return f"{personagem2.nome} venceu o combate!\n{resultado_ataque2}"

        return "Empate!"


cadastro = CadastroRPG("personagens.json")
app = App(cadastro)
app.mainloop()