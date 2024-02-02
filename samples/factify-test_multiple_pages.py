import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import os


customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(os.path.join("", "custom_theme.json"))  # Themes: "blue" (standard), "green", "dark-blue"
# customtkinter.set_default_color_theme("dark-blue") 


#Content Text
content1 = "Experience clarity and precision with our innovative solution. \nStreamlined and efficient, our product delivers a seamless experience."
content2 = "Experience clarity and precision with our innovative solution. \nStreamlined and efficient, our product delivers a seamless experience."
content3 = "Experience clarity and precision with our innovative solution. \nStreamlined and efficient, our product delivers a seamless experience."

#get images
chat_img_data = Image.open(os.path.join('images', "chat.png"), 'r')
logo_img_data = Image.open(os.path.join('images', "logo.png"), 'r')
about_img_data = Image.open(os.path.join('images', "about.png"), 'r')
add_img_data = Image.open(os.path.join('images', "add.png"), 'r')
delete_img_data = Image.open(os.path.join('images', "delete.png"), 'r')
updates_img_data = Image.open(os.path.join('images', "updates.png"), 'r')
target_img_data = Image.open(os.path.join('images', "target.png"), 'r')
trendup_img_data = Image.open(os.path.join('images', "trend_up.png"), 'r')

#set it to CTKImages
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(60, 60))
about_img = CTkImage(dark_image=about_img_data, light_image=about_img_data)
add_img = CTkImage(dark_image=add_img_data, light_image=add_img_data)
delete_img = CTkImage(dark_image=delete_img_data, light_image=delete_img_data)
updates_img = CTkImage(dark_image=updates_img_data, light_image=updates_img_data)
chat_img = CTkImage(dark_image=chat_img_data, light_image=chat_img_data)
target_img = CTkImage(dark_image=target_img_data, light_image=target_img_data)
trendup_img = CTkImage(dark_image=trendup_img_data, light_image=trendup_img_data)

class PreviousChats(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.radiobuttons = []
        for i in range(30):
            self.sidebar = customtkinter.CTkButton(self,  height=48, width=280, text="Values here", image=chat_img, compound=LEFT, anchor="w")
            self.sidebar.grid(row=i, column=0, padx=20, pady=(20, 10))

class StartPage(customtkinter.CTkFrame):
    # def __init__(self):
    #     super().__init__()
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self,parent)
        font_main = customtkinter.CTkFont(family="inter", size=48)
        font_sub_header = customtkinter.CTkFont(family="Inter", size=16, weight="bold")
        font_content =customtkinter.CTkFont(family="Inter", size=14, weight="normal")
    #     class StartPage(tk.Frame):

    # def __init__(self, parent, controller):
    #     tk.Frame.__init__(self,parent)
        
       

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # SIDEBAR
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, height=48, width=280, text="Factify", image=logo_img, font=customtkinter.CTkFont(family="Inter", size=24, weight="bold"), compound=LEFT)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # TODO must get to a data to database
        self.my_frame = PreviousChats(master=self.sidebar_frame, width=300, fg_color="#F8F8F8")
        self.my_frame.grid(row=1, column=0, sticky="nsew")
      

        self.new_chat = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280 , text="Start a new chat",text_color="white", fg_color="#004CC6", image=add_img, command=self.sidebar_button_event,compound=LEFT)
        self.new_chat.grid(row=4, column=0, pady=10)

        self.delete_conversation = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="Clear all conversation", image=delete_img, command=self.sidebar_button_event,compound=LEFT , anchor="w")
        self.delete_conversation.grid(row=6, column=0, pady=(10, 0))

        self.updates_and_faq = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="Updates and FAQ", image=updates_img, command=self.sidebar_button_event,compound=LEFT , anchor="w")
        self.updates_and_faq.grid(row=7, column=0, pady=(10, 0))

        self.about_btn = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="About", image=about_img, command=self.sidebar_button_event,compound=LEFT , anchor="w")
        self.about_btn.grid(row=8, column=0, pady=(10, 20))

        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling_event)
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        # MAIN CONTENT
        self.main_content = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_content.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), rowspan=4 , sticky="nsew")
        self.main_content.grid_rowconfigure(4, weight=1)
        self.main_content.grid_columnconfigure(4, weight=1)
       
        self.main_header = customtkinter.CTkLabel(self.main_content, text="Welcome to Page2", font=font_main, text_color="#004CC6")
        self.main_header.grid(row=4, column=4, pady=(0,600))

        self.sub_header = customtkinter.CTkLabel(self.main_content,text="The power of AI at your service - Tame the knowledge.", font=font_sub_header)
        self.sub_header.grid(row=4, column=4, pady=(0,510))

        self.cta = customtkinter.CTkButton(self.main_content,  height=48, width=70, text="Start", command=lambda: controller.show_frame(StartPage) , fg_color="#004CC6", text_color="white")
        self.cta.grid(row=4, column=4, pady=(0,300))

        self.card_title1 = customtkinter.CTkLabel(self.main_content,text="Clear and precise", font=font_sub_header, image=about_img, compound=TOP)
        self.card_title1.grid(row=4, column=4, padx=(0,1000))
        self.card_content1 = customtkinter.CTkLabel(self.main_content, font=font_content, width=300,text=content1, anchor="w")
        self.card_content1.grid(row=4, column=4, padx=(0,1000), pady=(100,0))

        self.card_title2 = customtkinter.CTkLabel(self.main_content,text="Personalized answers", font=font_sub_header, image=target_img, compound=TOP)
        self.card_title2.grid(row=4, column=4)
        self.card_content2 = customtkinter.CTkLabel(self.main_content, font=font_content, width=300, text=content2, anchor="w")
        self.card_content2.grid(row=4, column=4,pady=(100,0))
        
        self.card_title3 = customtkinter.CTkLabel(self.main_content,text="Increased efficiency", font=font_sub_header, image=trendup_img, compound=TOP)
        self.card_title3.grid(row=4, column=4, padx=(1000,0))
        self.card_content3 = customtkinter.CTkLabel(self.main_content, font=font_content, width=300,text=content3, anchor="w")                                                   
        self.card_content3.grid(row=4, column=4, padx=(1000,0) , pady=(100,0))
       
        
      


        # Page 2

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        # create textbox 
        # self.textbox = customtkinter.CTkTextbox(self)
        # self.textbox.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        print(new_scaling_float)
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

class LandingPage(customtkinter.CTkFrame):
    # def __init__(self):
    #     super().__init__()
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self,parent)
        font_main = customtkinter.CTkFont(family="inter", size=48)
        font_sub_header = customtkinter.CTkFont(family="Inter", size=16, weight="bold")
        font_content =customtkinter.CTkFont(family="Inter", size=14, weight="normal")
    #     class StartPage(tk.Frame):

    # def __init__(self, parent, controller):
    #     tk.Frame.__init__(self,parent)
        
       

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # SIDEBAR
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, height=48, width=280, text="Factify", image=logo_img, font=customtkinter.CTkFont(family="Inter", size=24, weight="bold"), compound=LEFT)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # TODO must get to a data to database
        self.my_frame = PreviousChats(master=self.sidebar_frame, width=300, fg_color="#F8F8F8")
        self.my_frame.grid(row=1, column=0, sticky="nsew")
      

        self.new_chat = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280 , text="Start a new chat",text_color="white", fg_color="#004CC6", image=add_img, command=self.sidebar_button_event,compound=LEFT)
        self.new_chat.grid(row=4, column=0, pady=10)

        self.delete_conversation = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="Clear all conversation", image=delete_img, command=self.sidebar_button_event,compound=LEFT , anchor="w")
        self.delete_conversation.grid(row=6, column=0, pady=(10, 0))

        self.updates_and_faq = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="Updates and FAQ", image=updates_img, command=self.sidebar_button_event,compound=LEFT , anchor="w")
        self.updates_and_faq.grid(row=7, column=0, pady=(10, 0))

        self.about_btn = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="About", image=about_img, command=self.sidebar_button_event,compound=LEFT , anchor="w")
        self.about_btn.grid(row=8, column=0, pady=(10, 20))

        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling_event)
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        # MAIN CONTENT
        self.main_content = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_content.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), rowspan=4 , sticky="nsew")
        self.main_content.grid_rowconfigure(4, weight=1)
        self.main_content.grid_columnconfigure(4, weight=1)
       
        self.main_header = customtkinter.CTkLabel(self.main_content, text="Welcome to Factify", font=font_main, text_color="#004CC6")
        self.main_header.grid(row=4, column=4, pady=(0,600))

        self.sub_header = customtkinter.CTkLabel(self.main_content,text="The power of AI at your service - Tame the knowledge.", font=font_sub_header)
        self.sub_header.grid(row=4, column=4, pady=(0,510))

        self.cta = customtkinter.CTkButton(self.main_content,  height=48, width=70, text="Start", command=lambda: controller.show_frame(StartPage) , fg_color="#004CC6", text_color="white")
        self.cta.grid(row=4, column=4, pady=(0,300))

        self.card_title1 = customtkinter.CTkLabel(self.main_content,text="Clear and precise", font=font_sub_header, image=about_img, compound=TOP)
        self.card_title1.grid(row=4, column=4, padx=(0,1000))
        self.card_content1 = customtkinter.CTkLabel(self.main_content, font=font_content, width=300,text=content1, anchor="w")
        self.card_content1.grid(row=4, column=4, padx=(0,1000), pady=(100,0))

        self.card_title2 = customtkinter.CTkLabel(self.main_content,text="Personalized answers", font=font_sub_header, image=target_img, compound=TOP)
        self.card_title2.grid(row=4, column=4)
        self.card_content2 = customtkinter.CTkLabel(self.main_content, font=font_content, width=300, text=content2, anchor="w")
        self.card_content2.grid(row=4, column=4,pady=(100,0))
        
        self.card_title3 = customtkinter.CTkLabel(self.main_content,text="Increased efficiency", font=font_sub_header, image=trendup_img, compound=TOP)
        self.card_title3.grid(row=4, column=4, padx=(1000,0))
        self.card_content3 = customtkinter.CTkLabel(self.main_content, font=font_content, width=300,text=content3, anchor="w")                                                   
        self.card_content3.grid(row=4, column=4, padx=(1000,0) , pady=(100,0))
       
        
      


        # Page 2

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        # create textbox 
        # self.textbox = customtkinter.CTkTextbox(self)
        # self.textbox.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        print(new_scaling_float)
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LandingPage,StartPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LandingPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.after(0, lambda:app.state('zoomed'))
    
    # TODO Resolve Logo of the app
    # app.iconphoto(True, tkinter.PhotoImage(file=os.path.join('images', "logo.png")))
    app.title("Factify")
    app.mainloop()