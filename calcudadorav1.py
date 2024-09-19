import tkinter as tk

#Lógica do clique
def click(event): # event vai receber o evento de clique com o mouse
    
    text = event.widget.cget("text") # Aqui eu pego  texto do botão clicado
    
    if text == "=": # Se o botão for '='
        
        try:
            result = eval(entry.get()) # o programa tenta calcular a expressão que foi clicada
            entry.delete(0, tk.END) # limpa a tela da calculadora
            entry.insert(tk.END, str(result)) # exibe o resultado inserindo após deletar o antigo
        except Exception as e: # caso tenha algum problema ele exibe 'Error' na tela
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            
    elif text == "C": # Se o texto digitado for 'C' ele também limpa a tela
        entry.delete(0, tk.END)
    
    else: # Se tudo tiver normal ele só mostra o que já tá sendo digitado
        entry.insert(tk.END, text)

#Criar a tela
root = tk.Tk() #Crio a janela
root.title("Calculadora") #Dou um nome pra janela

#Aqui eu crio o campo onde vai aparecer os numeros e tambem posso digitar nele
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, insertwidth=4, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4) # Aqui defini que o campo vai ter 4 colunas de comprimento

#Os botões que eu vou usar são esses, posteriormente vou colocar mais
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Variáveis pra me ajudar a alocar os botões sem precisar definir um lugar pra cada um
row_val = 1
col_val = 0

# Exibindo meus botões
for button in buttons: # Itero dentro da minha lista 
    b = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18)) #crio o botão e passo o botão da iteração como argumento de texto
    b.grid(row=row_val, column=col_val) # defino onde ele vai ficar na matriz (grid)
    b.bind("<Button-1>", click) # associo o botão ao evento de click o '<Button-1>' é usado para clique com botão esquerdo do mouse
    
    # Aqui apenas vou incrementando as colunas para poder exibir corretamente e ao final redefino para o loop não ter problemas
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
