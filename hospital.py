from Priority_Queue import*
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk


class CandyDispenserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Queue")
        # self.root.geometry("400x400")  # Set the size of the window

        # Create a label with a stylish font
        self.title_label = tk.Label(root, text="Hospital queue", font=("Helvetica", 16, "bold"), fg="orange")

        # Create the  frame for patients
        self.right_frame = tk.Frame(root, bg='white', bd=2, relief="solid", width=800, height=500)
        self.right_frame.pack(side=tk.RIGHT, padx=5, ipadx=20, ipady=10)
        self.right_frame.pack_propagate(0)

        # declaring string to hold patient's name and age
        self.patient_name = tk.StringVar()
        self.patient_age = tk.StringVar()

        # Create frame for buttons
        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side=tk.LEFT, padx=5, pady=5)
        # Create buttons with larger font and size
        button_config = {'font': ('Arial', 12), 'height': 2, 'width': 10}
        self.push_button = tk.Button(self.left_frame, text="Add",**button_config)
        self.pop_button = tk.Button(self.left_frame, text="Get First", **button_config)
        self.length_button = tk.Button(self.left_frame, text="Remove First",**button_config)
        self.is_empty_button = tk.Button(self.left_frame, text="Is Empty",**button_config)
        self.top_candy_button = tk.Button(self.left_frame, text="Length",**button_config)

        # Create label with larger font
        label_config = {'font': ('Arial', 10)}
        self.info_label = tk.Label(root, text="", padx=10, pady=10, **label_config)

        # Create labels in the waiting room
        self.waiting_room_label = tk.Label(self.right_frame, text="Waiting room", padx=10, pady=10, **label_config, fg="green")
        self.waiting_room_label.pack(side=tk.TOP)

        self.front_label = tk.Label(self.right_frame, text="FRONT", padx=10, pady=20, **label_config, fg="black", bg='white')
        self.front_label.pack(side=tk.RIGHT)

        self.back_label = tk.Label(self.right_frame, text="BACK", padx=10, pady=20, **label_config, fg="black", bg='white')
        self.back_label.pack(side=tk.LEFT)

        # create the receptionist
        self.receptionist = tk.Label(root, text="Receptionist", padx=10, pady=20, **label_config, fg="black", bg='brown')
        self.receptionist.pack(side=tk.RIGHT)

        # create labels and entry widget for age and name
        self.age_label = tk.Label(self.left_frame, text="Enter Age", padx=5, pady=10, **label_config, fg="black")
        self.name_label = tk.Label(self.left_frame, text="Enter Name", padx=5, pady=10, **label_config, fg="black")
        self.enter_age = tk.Entry(self.left_frame,textvariable = self.patient_age, font=('Helvetica',14,'normal'),justify="center",
                                bg="black", fg="blue", width=20, insertbackground="blue")
        self.enter_name = tk.Entry(self.left_frame,textvariable =self.patient_name, font=('Helvetica',14,'normal'),justify="center",
                                bg="black", fg="blue", width=20, insertbackground="blue")

        # Pack buttons and label
        self.title_label.pack(side=tk.TOP,padx=5, pady=5)
        self.info_label.pack(side=tk.TOP,padx=10, fill=tk.BOTH, expand=True)

        self.name_label.pack(side=tk.TOP, padx=5, pady=5)
        self.enter_name.pack(side=tk.TOP, padx=5, pady=5) 

        self.age_label.pack(side=tk.TOP, padx=5, pady=5)
        self.enter_age.pack(side=tk.TOP, padx=5, pady=5)    

        self.push_button.pack(side=tk.TOP, padx=5, pady=5)
        self.pop_button.pack(side=tk.TOP, padx=5, pady=5)
        self.length_button.pack(side=tk.TOP, padx=5, pady=5)
        self.is_empty_button.pack(side=tk.TOP, padx=5, pady=5)
        self.top_candy_button.pack(side=tk.TOP, padx=5, pady=5)

        # Create a list of unique candy colors
        self.candy_colors_list = []
        self.unique_colors = set()

    def update_dispenser(self):
        spring_dynamic_height = 160 - 10*(self.candy_colors.size())
        self.candy_dispenser_frame.destroy()

        self.candy_dispenser_frame = tk.Frame(self.root, bg='white', bd=2, relief="solid", height=600, width=300)
        self.candy_dispenser_frame.pack(side=tk.RIGHT, padx=10, ipadx=20, ipady=10, expand=True)
        self.candy_dispenser_frame.config(bg="white", borderwidth=2, relief="solid")

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
