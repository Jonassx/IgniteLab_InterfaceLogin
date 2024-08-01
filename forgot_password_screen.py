import customtkinter as ctk
from PIL import Image

class InterfaceForgotPassword():
    def __init__(self):

        # Set defaults colors
        bg_color = "#121214"
        label_color = "#7C7C8A"
        entry_color = "#202024"
        placeholder_color = "#7C7C8A"
        btn_color= "#81D8F7"

        self.root = ctk.CTk()
        self.root.title('Ignite Lab - Esqueceu a senha')
        self.root_widht = 1440
        self.root_height = 900
        self.root.resizable(False, False)
        self.root._set_appearance_mode("dark")
        self.root.configure(fg_color = bg_color)

        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()    
        x=(screen_width - self.root_widht) // 2
        y=(screen_height - self.root_height) // 2 - 30
        self.root.geometry(f"{self.root_widht}x{self.root_height}+{x}+{y}")

        def login_page():
            self.root.destroy()
            from login_screen import InterfaceLogin
            InterfaceLogin().run()
            
        # Image Ignite
        img_ignite = ctk.CTkImage(Image.open("./images/ignite_logo.png"), size=(110, 90))

        label_img = ctk.CTkLabel(self.root, text="", image=img_ignite) 
        label_img.place(x=670, y=260)

        #Btn return
        img_btn_return = ctk.CTkImage(Image.open("./images/arrow.png"), size=(32, 32))
        self.btn_return = ctk.CTkButton(self.root, text="Voltar", text_color=btn_color, fg_color="transparent", image=img_btn_return, width=40, height=40, font=("Inter", 16, "bold"), hover=None, command=login_page)
        self.btn_return.configure(cursor="hand2")
        self.btn_return.place(x=500, y=200)

        #Title
        title_ignite = ctk.CTkLabel(self.root, text="Ignite Lab", font=("Inter", 32, "bold"))
        title_ignite.place(x=650, y=380)

        # SubTitle
        label_description = ctk.CTkLabel(self.root, text="Digite seu email para enviar o link \nde recuperação de senha.", font=("Roboto", 18), text_color=label_color)
        label_description.place(x=595, y=440)

        # Entry Address Email
        label_address_email = ctk.CTkLabel(self.root, text="Endereço de e-mail", font=("Roboto", 14, "bold"))
        label_address_email.place(x=530, y=520)

        entry_address_email = ctk.CTkEntry(self.root, width=400, height=41, corner_radius=4, border_width=0, fg_color=entry_color, placeholder_text="Digite seu email", placeholder_text_color=placeholder_color)
        entry_address_email.place(x=530, y=550) 

        # Button Signup
        button_login = ctk.CTkButton(self.root, text="Enviar código para o email", font=("Inter", 16, "bold"),text_color="black",width=400, height=49, corner_radius=4, border_width=0, border_color=label_color, fg_color=btn_color, hover_color="#9BE1FE")
        button_login.configure(cursor="hand2")
        button_login.place(x=530, y=630)


    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    interface_forgot_password = InterfaceForgotPassword()
    interface_forgot_password.run()