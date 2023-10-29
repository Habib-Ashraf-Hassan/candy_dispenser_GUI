import tkinter as tk
import random
from Stacks import Stack
from tkinter.ttk import *
from PIL import Image, ImageTk


class CandyDispenserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Candy Dispenser")
        # self.root.geometry("400x400")  # Set the size of the window

        # Create a stack to store candy colors
        self.candy_colors = Stack()

        # Stack to store the reverse of org stack
        self.reved_candy_colors = Stack()

        # Create a label with a stylish font
        self.title_label = tk.Label(root, text="My Color Candy Dispenser", font=("Helvetica", 16, "bold"), fg="orange")

        # Create the candy dispenser frame
        self.candy_dispenser_frame = tk.Frame(root, bg='white', bd=2, relief="solid", height=600, width=300)
        self.candy_dispenser_frame.pack(side=tk.RIGHT, padx=5, ipadx=20, ipady=10)

        

        # Create buttons with larger font and size
        button_config = {'font': ('Arial', 12), 'height': 2, 'width': 8}
        self.push_button = tk.Button(root, text="Push",**button_config)
        self.pop_button = tk.Button(root, text="Pop", **button_config)
        self.length_button = tk.Button(root, text="Size",**button_config)
        self.is_empty_button = tk.Button(root, text="Is Empty",**button_config)
        self.top_candy_button = tk.Button(root, text="Peek",**button_config)

        # Create label with larger font
        label_config = {'font': ('Arial', 10)}
        self.info_label = tk.Label(root, text="", padx=10, pady=10, **label_config)
        self.candy_dispenser_frame.config(bg="gray", borderwidth=2, relief="solid")

        # Pack buttons and label
        self.push_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.pop_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.length_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.is_empty_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.top_candy_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.title_label.pack(side=tk.TOP,padx=10, pady=10)
        self.info_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a list of unique candy colors
        self.candy_colors_list = []
        self.unique_colors = set()

        self.spring_image = tk.PhotoImage(file="spring.png")
        self.spring_label = tk.Label(self.candy_dispenser_frame, image=self.spring_image)
        self.update_dispenser()

    
    def update_dispenser(self):
        spring_dynamic_height = 160 - 10*(self.candy_colors.size())
        self.candy_dispenser_frame.destroy()

        self.candy_dispenser_frame = tk.Frame(self.root, bg='white', bd=2, relief="solid", height=600, width=300)
        self.candy_dispenser_frame.pack(side=tk.RIGHT, padx=10, ipadx=20, ipady=10, expand=True)
        self.candy_dispenser_frame.config(bg="white", borderwidth=2, relief="solid")

        # self.spring_image = tk.PhotoImage(file="spring.png")
        # self.spring_label = tk.Label(self.candy_dispenser_frame, image=self.spring_image, width=300, height=300)
        # self.spring_label.pack(side=tk.BOTTOM)

        # Read the Image
        self.image = Image.open("spring.png")
        
        # Resize the image using resize() method
        self.resize_image = self.image.resize((250, 100))
        
        self.img = ImageTk.PhotoImage(self.resize_image)
        
        self.spring_label = tk.Label(self.candy_dispenser_frame, image=self.img)
        self.spring_label.pack(side=tk.BOTTOM)

        
        

    

# List of candy colors
candy_colors = ['red', 'yellow', 'blue', 'green', 'orange', 'pink',
                'black', 'purple', 'brown', 'gray', 'cyan', 'magenta',
                'white', 'indigo']

root = tk.Tk()
app = CandyDispenserApp(root)
root.mainloop()
