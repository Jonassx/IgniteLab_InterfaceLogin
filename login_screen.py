import customtkinter as ctk
from PIL import Image

class InterfaceLogin():
    def __init__(self):

        # Set defaults colors
        bg_color = "#121214"
        label_color = "#7C7C8A"
        entry_color = "#202024"
        placeholder_color = "#7C7C8A"
        btn_color= "#81D8F7"

        self.root = ctk.CTk()
        self.root.title('Ignite Lab - Login')
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

        def create_account_page():
            self.root.destroy()
            from create_account_screen import InterfaceCreateAccount
            InterfaceCreateAccount().run()

        def forgot_password_page():
            self.root.destroy()
            from forgot_password_screen import InterfaceForgotPassword
            InterfaceForgotPassword().run()

        # Image Ignite
        img_ignite = ctk.CTkImage(Image.open("./images/ignite_logo.png"), size=(110, 90))

        label_img = ctk.CTkLabel(self.root, text="", image=img_ignite) 
        label_img.place(x=670, y=160)

        #Title
        title_ignite = ctk.CTkLabel(self.root, text="Ignite Lab", font=("Inter", 32, "bold"))
        title_ignite.place(x=650, y=280)

        # SubTitle
        label_description = ctk.CTkLabel(self.root, text="Faça login e comece a usar", font=("Roboto", 18), text_color=label_color)
        label_description.place(x=620, y=340)

        # Entry Address Email
        label_address_email = ctk.CTkLabel(self.root, text="Endereço de e-mail", font=("Roboto", 14, "bold"))
        label_address_email.place(x=530, y=400)

        entry_address_email = ctk.CTkEntry(self.root, width=400, height=41, corner_radius=4, border_width=0, fg_color=entry_color, placeholder_text="Digite seu email", placeholder_text_color=placeholder_color)
        entry_address_email.place(x=530, y=430)

        # Entry Password
        label_password = ctk.CTkLabel(self.root, text="Sua senha", font=("Roboto", 14, "bold"))
        label_password.place(x=530, y=480)

        entry_password = ctk.CTkEntry(self.root, width=400, height=41, corner_radius=4, border_width=0, fg_color=entry_color, placeholder_text="**********", placeholder_text_color=placeholder_color, show="*")
        entry_password.place(x=530, y=510)

        # Save passoword
        self.checkbox_save_passowrd = ctk.CTkCheckBox(self.root, text="", width=0, height=0, corner_radius=4, border_width=0, border_color=label_color, fg_color=entry_color, hover=None)
        self.checkbox_save_passowrd.place(x=530, y=570)

        self.label_save_password = ctk.CTkLabel(self.root,text="Lembrar senha por 30 dias", text_color=label_color, width=0, height=0)
        self.label_save_password.place(x=565, y=575)

        # Button Login
        button_login = ctk.CTkButton(self.root, text="Entrar na plataforma", font=("Inter", 16, "bold"),text_color="black",width=400, height=49, corner_radius=4, border_width=0, border_color=label_color, fg_color=btn_color, hover_color="#9BE1FE")
        button_login.configure(cursor="hand2")
        button_login.place(x=530, y=614)

        #Forgot password
        self.label_forgot_password = ctk.CTkButton(self.root, text="Esqueceu a sua senha?", text_color=label_color, hover=None, fg_color="transparent", command=forgot_password_page)
        self.label_forgot_password.configure(cursor="hand2")
        self.label_forgot_password.place(x=652, y=690)

        #Label Create account
        self.label_create_account = ctk.CTkLabel(self.root, text="Não possui conta?", text_color=label_color)
        self.label_create_account.place(x=610, y=720)

        #Link Create account
        self.link_create_account = ctk.CTkButton(self.root, text="Crie sua conta agora!", text_color=label_color, hover=None, fg_color="transparent", width=0, height=0, command=create_account_page)
        self.link_create_account.configure(cursor="hand2")
        self.link_create_account.place(x=717, y=723)


    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    interface = InterfaceLogin()
    interface.run()