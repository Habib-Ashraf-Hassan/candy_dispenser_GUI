import tkinter as tk
from Stacks import Stack
from tkinter.ttk import *
from PIL import Image, ImageTk


class CandyDispenserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Candy Dispenser")
        # Create a stack to store candy colors
        self.candy_colors = Stack()

        # Stack to store the reverse of org stack
        self.reved_candy_colors = Stack()

        # String label to show user the acceptable candy colors
        self.my_name_reg = "Ashraf Mohammed Hassan Anil: SCT211-0255/2021"

        # Declaring string var for the input of user's color
        self.color_var = tk.StringVar()
        # Create a label with a stylish font
        self.title_label = tk.Label(root, text="My Color Candy Dispenser", font=("Helvetica", 16, "bold"), fg="orange")
        self.my_name_label = tk.Label(root, text=self.my_name_reg, font=("Helvetica", 13, "bold"), fg="green")
        
        self.usr_entry = tk.Entry(root,textvariable = self.color_var, font=('Helvetica',14,'normal'),justify="center",
                                bg="black", fg="blue", width=20, insertbackground="blue")
        
        self.instruct_usr = tk.Label(root, text="Enter candy color:", font=("Helvetica", 12, "bold"), fg="Blue")
        # Create the candy dispenser frame
        self.candy_dispenser_frame = tk.Frame(root, bg='white', bd=2, relief="solid", width=280, height=500)
        self.candy_dispenser_frame.pack(side=tk.RIGHT, padx=5, ipadx=20, ipady=10)
        self.candy_dispenser_frame.pack_propagate(0)
         
        # Create buttons with larger font and size
        button_config = {'font': ('Arial', 12), 'height': 2, 'width': 8}
        self.push_button = tk.Button(root, text="Push", command=self.push_candy, **button_config)
        self.pop_button = tk.Button(root, text="Pop", command=self.pop_candy, **button_config)
        self.length_button = tk.Button(root, text="Size", command=self.update_length_label, **button_config)
        self.is_empty_button = tk.Button(root, text="Is Empty", command=self.update_is_empty_label, **button_config)
        self.top_candy_button = tk.Button(root, text="Peek", command=self.update_top_candy_label, **button_config)

        # Create label with larger font
        label_config = {'font': ('Arial', 12)}
        self.info_label = tk.Label(root, text="", padx=10, pady=10, **label_config)
        self.candy_dispenser_frame.config(bg="white", borderwidth=2, relief="solid")

        # Pack buttons and label
        self.push_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.pop_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.length_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.is_empty_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.top_candy_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.title_label.pack(side=tk.TOP,padx=10, pady=10)
        self.my_name_label.pack(side=tk.TOP)
        
        self.info_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20)
        
        self.instruct_usr.pack(padx=0, pady=10, anchor="sw")
        self.usr_entry.pack(padx=10, pady=10, anchor="sw")


        self.update_dispenser()

    def add_usr_candy(self):
        usr_color = str(self.color_var.get())

        if usr_color not in candy_colors:
            self.info_label.config(text="Only PUSH appropriate color candy", fg="red")
        else:
            self.candy_colors.push(usr_color)
            # self.candy_colors_list.append(usr_color)
            self.update_dispenser()
            added_candy = self.candy_colors.peek()
            self.color_var.set("")
            self.info_label.config(text="", fg="green")

    def remove_usr_candy(self):
        if not self.candy_colors.is_empty():
            top_candy = self.candy_colors.peek()
            self.candy_colors.pop()
            # self.candy_colors_list.pop()
            self.info_label.config(text=f"{top_candy} candy removed")
            self.update_dispenser()
        else:
            self.info_label.config(text="Cannot POP; Candy dispenser is empty", fg="red")

    def update_dispenser(self):
        for widget in self.candy_dispenser_frame.winfo_children():
            widget.destroy()
    
        self.spring_dynamic_height = 330 - 20*(self.candy_colors.size())
        

        # Read the Image
        self.image = Image.open("spring.png")
        
        # Resize the image using resize() method
        self.resize_image = self.image.resize((270, self.spring_dynamic_height))
        
        self.img = ImageTk.PhotoImage(self.resize_image)
        
        self.spring_label = tk.Label(self.candy_dispenser_frame, image=self.img, bg="white")
        self.spring_label.pack(side=tk.BOTTOM)

        while not self.candy_colors.is_empty():
            # color = str(self.candy_colors.peek())
            # candy = tk.Canvas(self.candy_dispenser_frame, width=250, height=20, bg=color, bd=2, relief="solid")
            # candy.pack(side=tk.BOTTOM)
            self.reved_candy_colors.push(self.candy_colors.pop())
        
        while not self.reved_candy_colors.is_empty():
            color = str(self.reved_candy_colors.pop())
            self.candy_colors.push(color)
            candy = tk.Canvas(self.candy_dispenser_frame, width=250, height=25, bg=color, bd=2, relief="solid")
            candy.pack(side=tk.BOTTOM)
        
    def update_length_label(self):
        length = self.candy_colors.size()
        self.info_label.config(text=f"{length} candies")

    def update_is_empty_label(self):
        is_empty = self.candy_colors.is_empty()
        self.info_label.config(text=str(is_empty))

    def update_top_candy_label(self):
        try:
            top_candy = self.candy_colors.peek()
            self.info_label.config(text=f"{top_candy} candy at the TOP")
        except IndexError:
            self.info_label.config(text="Cannot PEEK; Candy Dispenser is Empty", fg="red")

    def push_candy(self):
        if self.candy_colors.size() < 14:
            self.add_usr_candy()
        else:
            self.info_label.config(text="Cannot add more candies; Max candies(14) attained", fg="red")

    def pop_candy(self):
        self.remove_usr_candy()

# List of candy colors
candy_colors = ['red', 'yellow', 'blue', 'green', 'orange', 'pink',
                'black', 'purple', 'brown', 'white', 'cyan', 'gray', 'magenta',
                'indigo', 'violet', 'lightgray', 'darkorange', 'gold']

root = tk.Tk()
app = CandyDispenserApp(root)

root.mainloop()
