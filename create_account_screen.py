import customtkinter as ctk
from PIL import Image

class InterfaceCreateAccount():
    def __init__(self):

        # Set defaults colors
        bg_color = "#121214"
        label_color = "#7C7C8A"
        entry_color = "#202024"
        placeholder_color = "#7C7C8A"
        btn_color= "#81D8F7"

        self.root = ctk.CTk()
        self.root.title('Ignite Lab - Criar conta')
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
        label_img.place(x=670, y=160)

        #Title
        title_ignite = ctk.CTkLabel(self.root, text="Ignite Lab", font=("Inter", 32, "bold"))
        title_ignite.place(x=650, y=280)

        # SubTitle
        label_description = ctk.CTkLabel(self.root, text="Crie sua conta e participe!", font=("Roboto", 18), text_color=label_color)
        label_description.place(x=620, y=340)

        # Entry Address Email
        label_address_email = ctk.CTkLabel(self.root, text="Endereço de e-mail", font=("Roboto", 14, "bold"))
        label_address_email.place(x=530, y=400)

        entry_address_email = ctk.CTkEntry(self.root, width=400, height=41, corner_radius=4, border_width=0, fg_color=entry_color, placeholder_text="Digite seu melhor email", placeholder_text_color=placeholder_color)
        entry_address_email.place(x=530, y=430)

        # Entry Password
        label_password = ctk.CTkLabel(self.root, text="Sua senha", font=("Roboto", 14, "bold"))
        label_password.place(x=530, y=480)

        entry_password = ctk.CTkEntry(self.root, width=400, height=41, corner_radius=4, border_width=0, fg_color=entry_color, placeholder_text="Digite uma senha", placeholder_text_color=placeholder_color)
        entry_password.place(x=530, y=510)

        entry_confirm_password = ctk.CTkEntry(self.root, width=400, height=41, corner_radius=4, border_width=0, fg_color=entry_color, placeholder_text="Confirme sua senha", placeholder_text_color=placeholder_color)
        entry_confirm_password.place(x=530, y=560)

        # Button Singup
        button_signup = ctk.CTkButton(self.root, text="Cadastrar", font=("Inter", 16, "bold"),text_color="black",width=400, height=49, corner_radius=4, border_width=0, border_color=label_color, fg_color=btn_color, hover_color="#9BE1FE")
        button_signup.configure(cursor="hand2")
        button_signup.place(x=530, y=630)


        #Label Create account
        self.label_have_account = ctk.CTkLabel(self.root, text="Já possui conta?", text_color=label_color)
        self.label_have_account.place(x=640, y=700)

        #Link Create account
        self.link_login_page = ctk.CTkButton(self.root, text="Faça login", text_color=label_color, hover=None, fg_color="transparent", width=0, height=0, command=login_page)
        self.link_login_page.configure(cursor="hand2")
        self.link_login_page.place(x=740, y=703)


    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    interface_create_account = InterfaceCreateAccount()
    interface_create_account.run()