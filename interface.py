import tkinter as tk
from tkinter import messagebox

import random
from bd import con , cursor 
from quiz import quiz , opcoes_completas

score = 0
current_question = 0
nome = ""

def usuario_nome():
    global nome
    nome = entry_name.get()
    if nome:
        messagebox.showinfo("Sucesso!" , "Nome Registrado , agora você pode começar o quiz")
        name_label.config(state=tk.DISABLED)
        entry_name.config(state=tk.DISABLED)
        botao_confirmar.config(state=tk.DISABLED)


        cursor.execute("insert into respostas (nome) values (?)" , (nome,))
        con.commit()

        exibir_pergunta()
        
    else:
        messagebox.showwarning("Erro")

def armazenar_resposta(pergunta,resposta):
    cursor.execute("insert into respostas (nome,pergunta,resposta) values (?,?,?)",(nome,pergunta,resposta))
    con.commit()
    


def verificaR_resposta(answer):
    global score , current_question 

    pergunta_atual = quiz[current_question]["Pergunta"]

    if quiz[current_question]["resposta"] == answer:
        score += 1
        
    armazenar_resposta(pergunta_atual,answer)
    current_question += 1

    if current_question < len(quiz):
        exibir_pergunta()

    else:
        show_result()
        

    
def exibir_pergunta():
    global current_question
    pergunta_atual = quiz[current_question]
    
    question_label.config(text=pergunta_atual["Pergunta"])

    option1_btn.config(text=pergunta_atual["Opções"][0] , state=tk.NORMAL, command=lambda:verificaR_resposta("A"))
    option2_btn.config(text=pergunta_atual["Opções"][1],state=tk.NORMAL, command=lambda:verificaR_resposta("B"))
    option3_btn.config(text=pergunta_atual["Opções"][2],state=tk.NORMAL, command=lambda:verificaR_resposta("C"))
    option4_btn.config(text=pergunta_atual["Opções"][3],state=tk.NORMAL, command=lambda:verificaR_resposta("D"))
    
    
def show_result():

    dados = cursor.execute("""
            select nome, pergunta, resposta from respostas
            where pergunta is not null and resposta is not null
            Order by pergunta, nome
    """).fetchall()
    
    respostas_por_pergunta = {}
    
    # Organiza as respostas por pergunta com a pergunta sendo a chave e valor é o nome e resposta sendo uma tupla (nome,resposta)
    for nome, pergunta, resposta in dados:
        if pergunta not in respostas_por_pergunta:
            respostas_por_pergunta[pergunta] = []
        respostas_por_pergunta[pergunta].append((nome, resposta))
    
    
    respostas_texto = ""
    
    # Formata o texto para exibir as respostas
    for pergunta, respostas in respostas_por_pergunta.items():
        respostas_texto += f"\nPergunta: {pergunta}"
        resposta_correta = opcoes_completas.get(pergunta, {}).get("correta","Resposta Desconhecida")
        for nome, resposta in respostas:
            respostA_completa = opcoes_completas.get(pergunta, {}).get(resposta,resposta)
            
            respostas_texto += f"\n  {nome} respondeu: {respostA_completa}"
        respostas_texto += f"\n Resposta correta : {resposta_correta} \n "
    
    # janela mostrando os resultados

    result_window = tk.Toplevel(janela)
    result_window.title("Quiz Finalizado")
    
    # Adiciona um Canvas com barra de rolagem
    canvas = tk.Canvas(result_window)
    scrollbar = tk.Scrollbar(result_window, orient="vertical", command=canvas.yview)
    result_frame = tk.Frame(canvas)
    
    result_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    canvas.create_window((0, 0), window=result_frame, anchor="nw")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    canvas.config(yscrollcommand=scrollbar.set)
    
    # Adiciona o texto de resposta ao frame
    tk.Label(result_frame,text=f"Você acertou {score}/{len(quiz)}\n\nRespostas:\n{respostas_texto}", justify="left", padx=10, pady=10).pack()

    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    playagain_btn.pack(pady=10)
    
      
def jogar_dnv():
    global score , current_question
    score = 0 
    current_question = 0
    random.shuffle(quiz)

    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)

    playagain_btn.pack_forget()
    exibir_pergunta()



# interface gráfica
janela = tk.Tk()
janela.title("Quiz")
janela.geometry("400x600")

background_color = "#ECECEC"

text_color = "#333333"
button_color = "#57707A"
button_text_color = "#FFFFFF"

janela.config(bg = background_color)
janela.option_add("*Font" , "Arial")


# Interface

name_label = tk.Label(janela,text="Insira seu nome: ")
name_label.pack(pady=10)

entry_name = tk.Entry(janela)
entry_name.pack(pady=10)

botao_confirmar = tk.Button(janela, text="Confirmar", command=usuario_nome)
botao_confirmar.pack(pady=10)

question_label = tk.Label(janela,text="",wraplength="380" , bg=background_color , fg=text_color , font=("Arial" , 12, "bold"))
question_label.pack(pady=20)

option1_btn = tk.Button(janela,text="", width=30, height=2,bg=button_color , fg=button_text_color , state=tk.DISABLED  , font=("Arial" , 10 , "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela,text="", width=30,height=2,bg=button_color , fg=button_text_color , state=tk.DISABLED , font=("Arial" , 10 , "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela,text="", width=30,height=2,bg=button_color , fg=button_text_color , state=tk.DISABLED , font=("Arial" , 10 , "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela,text="", width=30,height=2,bg=button_color , fg=button_text_color , state=tk.DISABLED , font=("Arial" , 10 , "bold"))
option4_btn.pack(pady=10)

playagain_btn = tk.Button(janela,text="Jogar de novo", width=30,bg=button_color , fg=button_text_color, font=("Arial" , 10 , "bold") , command=jogar_dnv)

janela.mainloop()

con.close()