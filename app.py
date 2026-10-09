import customtkinter as ctk
from main import criar_senha

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("PassWord Generator")
root.geometry("420x320")
root.resizable(False, False)


def gerar_senha():
    try:
        tamanho = int(campo_tamanho.get())
    except ValueError:
        mensagem_erro.configure(text="Digite um número válido.")
        campo_senha.delete("0.0", "end")
        return

    if tamanho < 6 or tamanho > 14:
        mensagem_erro.configure(text="Tamanho inválido. A senha deve ter entre 6 e 14 caracteres.")
        campo_senha.delete("0.0", "end")
        return

    senha = criar_senha(tamanho)
    mensagem_erro.configure(text="")
    campo_senha.delete("0.0", "end")
    campo_senha.insert("0.0", senha)


texto = ctk.CTkLabel(master=root, text="Digite o tamanho da senha abaixo (6-14):", font=("Arial", 16))
texto.pack(pady=(30, 10))

campo_tamanho = ctk.CTkEntry(master=root, placeholder_text="Tamanho da senha...", width=200)
campo_tamanho.pack(pady=10)

botao = ctk.CTkButton(master=root, text="Gerar senha", command=gerar_senha)
botao.pack(pady=10)

mensagem_erro = ctk.CTkLabel(master=root, text="", font=("Arial", 12), text_color="red")
mensagem_erro.pack(pady=5)

campo_senha = ctk.CTkTextbox(master=root, width=260, height=80)
campo_senha.pack(pady=10)

root.mainloop()
