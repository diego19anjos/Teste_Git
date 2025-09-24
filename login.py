import customtkinter as ctk
from PIL import Image


# === CONFIGURAÇÃO INICIAL ===
ctk.set_appearance_mode("light")   
ctk.set_default_color_theme("green")  

# === JANELA PRINCIPAL ===
app = ctk.CTk()  
app.geometry("400x500")   
app.title("Tela Login - Software Base")  

# === FRAME CENTRAL ===
frame = ctk.CTkFrame(master=app, width=320, height=420, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor="center")  

# === LOGO (IMAGEM) ===
# Carrega a imagem (use uma imagem sua, ex: "logo.png")
# logo_image = ctk.CTkImage(light_image=Image.open("logo.png"),
#                           dark_image=Image.open("logo.png"),
#                           size=(80, 80))  # tamanho da logo (80x80 px)

# Exibe a imagem no frame
# logo_label = ctk.CTkLabel(master=frame, image=logo_image, text="")  
# logo_label.pack(pady=(20, 10))  

# === TÍTULO ===
label_title = ctk.CTkLabel(master=frame, text="Bem-vindo!", 
                           font=("Arial", 20, "bold"))
label_title.pack(pady=(10, 5))  

# Subtítulo
label_subtitle = ctk.CTkLabel(master=frame, text="Faça login para continuar", 
                              font=("Arial", 12))
label_subtitle.pack(pady=(0, 20))

# === CAMPO USUÁRIO ===
entry_user = ctk.CTkEntry(master=frame, placeholder_text="Usuário", 
                          width=250, height=35, corner_radius=10)
entry_user.pack(pady=10)

# === CAMPO SENHA ===
entry_pass = ctk.CTkEntry(master=frame, placeholder_text="Senha", 
                          show="*", width=250, height=35, corner_radius=10)
entry_pass.pack(pady=10)

# === FUNÇÃO PARA ABRIR O MENU ===
def abrir_menu():
    app.destroy()     # Fecha a tela de login
    # Abre a tela do menu
 # menu_aba.abrir_menu()

# === BOTÃO DE LOGIN ===
btn_login = ctk.CTkButton(master=frame, text="Entrar", width=250, height=40, 
                          corner_radius=20, fg_color="#3290C6", hover_color="#45a049",  command=abrir_menu)
btn_login.pack(pady=20)

# === BOTÃO DE CADASTRO ===
btn_register = ctk.CTkButton(master=frame, text="Cadastre-se", width=250, height=40, 
                             corner_radius=20, fg_color="transparent", hover_color="lightblue",
                             border_width=3, border_color="#4CAF50", text_color="#0E140E")
btn_register.pack()

# === EXECUTA O APP ===
app.mainloop()
