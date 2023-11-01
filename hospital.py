from Priority_Queue import*
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk


class CandyDispenserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Queue")
        # self.root.geometry("400x400")  # Set the size of the window

        self.patient_pq = Priority_queue() 

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
        self.add_button = tk.Button(self.left_frame, text="Add",**button_config)
        self.get_first_button = tk.Button(self.left_frame, text="Get First", **button_config)
        self.remove_first_button = tk.Button(self.left_frame, text="Remove First",**button_config)
        self.is_empty_button = tk.Button(self.left_frame, text="Is Empty",command=self.update_is_empty_label, **button_config)
        self.lenght_button = tk.Button(self.left_frame, text="Length", command=self.update_length_label, **button_config)

        # Create label with larger font
        label_config = {'font': ('Arial', 12)}
        self.info_label = tk.Label(root, text="", padx=10, pady=10, font=("Helvetica", 12, "bold"))

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

        self.add_button.pack(side=tk.TOP, padx=5, pady=5)
        self.get_first_button.pack(side=tk.TOP, padx=5, pady=5)
        self.remove_first_button.pack(side=tk.TOP, padx=5, pady=5)
        self.is_empty_button.pack(side=tk.TOP, padx=5, pady=5)
        self.lenght_button.pack(side=tk.TOP, padx=5, pady=5)

    def update_length_label(self):
        length = self.patient_pq.get_length()
        self.info_label.config(text=f"{length} Patients")

    def update_is_empty_label(self):
        is_empty = self.patient_pq.is_empty()
        self.info_label.config(text=f"Empty: {str(is_empty)}")
    

# List of candy colors
candy_colors = ['red', 'yellow', 'blue', 'green', 'orange', 'pink',
                'black', 'purple', 'brown', 'gray', 'cyan', 'magenta',
                'white', 'indigo']

root = tk.Tk()
app = CandyDispenserApp(root)
root.mainloop()

