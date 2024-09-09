import tkinter as tk
from tkinter import messagebox
import random
from quiz import quiz

score = 0
current_question = 0


def verificaR_resposta(answer):
    global score , current_question 

    if quiz[current_question]["resposta"] == answer:
        score += 1
    
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
    messagebox.showinfo("Quiz Finalizado" , f"Parabéns! Você conseguiu finalizar o quiz \nVocê acertou {score}/{len(quiz)}")
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
janela.geometry("400x450")

background_color = "#ECECEC"

text_color = "#333333"
button_color = "#57707A"
button_text_color = "#FFFFFF"

janela.config(bg = background_color)
janela.option_add("*Font" , "Arial")


# Interface

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




exibir_pergunta()
janela.mainloop()