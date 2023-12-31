import tkinter as tk
import random
from Stacks import Stack


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
        self.candy_dispenser_frame = tk.Frame(root, bg='white', bd=2, relief="solid")
        self.candy_dispenser_frame.pack(side=tk.RIGHT, padx=5, ipadx=20, ipady=10)

        # Add a rectangular object at the bottom of the candy dispenser frame which rep the SPRING
        self.rectangular_object = tk.Canvas(self.candy_dispenser_frame, width=300, height=20, bg='gray')
        self.rectangular_object.pack(side=tk.BOTTOM)

        # Create buttons with larger font and size
        button_config = {'font': ('Arial', 12), 'height': 2, 'width': 8}
        self.push_button = tk.Button(root, text="Push", command=self.push_candy, **button_config)
        self.pop_button = tk.Button(root, text="Pop", command=self.pop_candy, **button_config)
        self.length_button = tk.Button(root, text="Size", command=self.update_length_label, **button_config)
        self.is_empty_button = tk.Button(root, text="Is Empty", command=self.update_is_empty_label, **button_config)
        self.top_candy_button = tk.Button(root, text="Peek", command=self.update_top_candy_label, **button_config)

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

        # Create initial candy dispenser with 10 candies
        for _ in range(6):
            # self.add_candy()
            color = self.generate_unique_color()
            self.candy_colors.push(color)
            self.candy_colors_list.append(color)
        self.update_dispenser()

    def generate_unique_color(self):
        while True:
            color = random.choice(candy_colors)
            if color not in self.unique_colors:
                self.unique_colors.add(color)
                return color

    def add_candy(self):
        color = self.generate_unique_color()
        self.candy_colors.push(color)
        self.candy_colors_list.append(color)
        self.update_dispenser()
        
    def remove_candy(self):
        if not self.candy_colors.is_empty():
            top_candy = self.candy_colors.peek()

            self.unique_colors.remove(self.candy_colors.peek())
            self.candy_colors.pop()
            self.candy_colors_list.pop()
            self.info_label.config(text=f"{top_candy} candy removed")
            self.update_dispenser()
            
        else:
            self.info_label.config(text="Cannot POP; Candy dispenser is empty", fg="red")

    def update_dispenser(self):
        spring_dynamic_height = 160 - 10*(self.candy_colors.size())
        self.candy_dispenser_frame.destroy()

        self.candy_dispenser_frame = tk.Frame(self.root)
        self.candy_dispenser_frame.pack(side=tk.RIGHT, padx=10, ipadx=20, ipady=10, expand=True)
        self.candy_dispenser_frame.config(bg="white", borderwidth=2, relief="solid")

        self.rectangular_object = tk.Canvas(self.candy_dispenser_frame, width=300,
                                            height=spring_dynamic_height, bg='gray')
        self.rectangular_object.pack(side=tk.BOTTOM, padx=0, pady=0)

        for i in range(0, spring_dynamic_height, 4):
            self.rectangular_object.create_line(0, i, 300, i, fill='black')

        # for color in reversed(self.candy_colors_list):
        #     candy = tk.Canvas(self.candy_dispenser_frame, width=200, height=20, bg=color, bd=2, relief="solid")
        #     candy.pack()
        while not self.candy_colors.is_empty():
            color = str(self.candy_colors.peek())
            candy = tk.Canvas(self.candy_dispenser_frame, width=300, height=30, bg=color, bd=2, relief="solid")
            candy.pack()
            self.reved_candy_colors.push(self.candy_colors.pop())
        
        while not self.reved_candy_colors.is_empty():
            self.candy_colors.push(self.reved_candy_colors.pop())
        

    def update_length_label(self):
        length = self.candy_colors.size()
        self.info_label.config(text=f"{length} candies", fg="green")

    def update_is_empty_label(self):
        is_empty = self.candy_colors.is_empty()
        self.info_label.config(text=str(is_empty))

    def update_top_candy_label(self):
        try:
            top_candy = self.candy_colors.peek()
            self.info_label.config(text=f"{top_candy} candy is at the TOP", fg="green" )
        except IndexError:
            self.info_label.config(text="Cannot PEEK; Candy Dispenser is Empty", fg="red")

    def push_candy(self):
        if len(self.unique_colors) < len(candy_colors):
            self.add_candy()
            added_candy = self.candy_colors.peek()
            self.info_label.config(text="", fg="green")
        else:
            self.info_label.config(text="Cannot add more candies; Max candies attained", fg="red")

    def pop_candy(self):
        self.remove_candy()
        


# List of candy colors
candy_colors = ['red', 'yellow', 'blue', 'green', 'orange', 'pink',
                'black', 'purple', 'brown', 'gray', 'cyan', 'magenta',
                'white', 'indigo']

root = tk.Tk()
app = CandyDispenserApp(root)
root.mainloop()
