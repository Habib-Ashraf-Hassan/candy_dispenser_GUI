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

        # Create the  frame for patients
        self.right_frame = tk.Frame(root, bg='white', bd=2, relief="solid", width=900, height=500)
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
        self.add_button = tk.Button(self.left_frame, text="Add",command=self.add_patient, **button_config)
        self.get_first_button = tk.Button(self.left_frame, text="Get First",command=self.get_first_patient,  **button_config)
        self.remove_first_button = tk.Button(self.left_frame, text="Remove First",command=self.remove_first_patient, **button_config)
        self.is_empty_button = tk.Button(self.left_frame, text="Is Empty",command=self.update_is_empty_label, **button_config)
        self.lenght_button = tk.Button(self.left_frame, text="Length", command=self.update_length_label, **button_config)

        # Create label with larger font
        label_config = {'font': ('Arial', 12)}
        self.info_label = tk.Label(self.right_frame, text="", padx=10, pady=10, font=("Helvetica", 12, "bold"), bg="white")

        # Create a label with a stylish font
        self.title_label = tk.Label(self.left_frame, text="Hospital queue", font=("Helvetica", 16, "bold"), fg="orange")
        # Create labels in the waiting room
        self.waiting_room_label = tk.Label(self.right_frame, text="BACK<------    Waiting room       ----->FRONT", padx=10, pady=10, **label_config, fg="green")
        self.waiting_room_label.pack(side=tk.TOP)
        self.info_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # self.front_label = tk.Label(self.right_frame, text="FRONT", padx=10, pady=20, **label_config, fg="black", bg='white')
        # self.front_label.pack(side=tk.RIGHT)

        # self.back_label = tk.Label(self.right_frame, text="BACK", padx=10, pady=20, **label_config, fg="black", bg='white')
        # self.back_label.pack(side=tk.LEFT)

        # create the receptionist
        self.recept_img = Image.open('receptionist_desk.png')  # Replace with your icon image
        self.recept_img = self.recept_img.resize((50, 50))
        self.recept_icon = ImageTk.PhotoImage(self.recept_img)
        
        self.receptionist = tk.Label(root, text="Receptionist", image=self.recept_icon, compound="top", padx=10, pady=20, **label_config, fg="black", bg='gray')
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
        

        self.name_label.pack(side=tk.TOP, padx=5, pady=5)
        self.enter_name.pack(side=tk.TOP, padx=5, pady=5) 

        self.age_label.pack(side=tk.TOP, padx=5, pady=5)
        self.enter_age.pack(side=tk.TOP, padx=5, pady=5)    

        self.add_button.pack(side=tk.TOP, padx=5, pady=5)
        self.get_first_button.pack(side=tk.TOP, padx=5, pady=5)
        self.remove_first_button.pack(side=tk.TOP, padx=5, pady=5)
        self.is_empty_button.pack(side=tk.TOP, padx=5, pady=5)
        self.lenght_button.pack(side=tk.TOP, padx=5, pady=5)
        
        # self.draw_patients()

    def draw_patients(self):
    # Clear existing icons by destroying all widgets in self.right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Add the updated patient icons
        patient_icons = []
        self.waiting_room_label = tk.Label(self.right_frame, text="BACK<------    Waiting room       ----->FRONT", padx=10, pady=10, font=("Helvetica", 12, "bold"), fg="green")
        self.waiting_room_label.pack(side=tk.TOP)

        self.info_label = tk.Label(self.right_frame, text="", padx=10, pady=10, font=("Helvetica", 12, "bold"), bg="white")

        self.info_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for age, name in self.patient_pq.get_pq():
            img = Image.open('user.png')  # Replace with your icon image
            img = img.resize((40, 40))
            img = ImageTk.PhotoImage(img)
            
            icon_label = tk.Label(self.right_frame, bg='white', text=f'{name} {age} years', image=img, compound="bottom")
            icon_label.image = img
            icon_label.pack(side=tk.RIGHT, padx=5)
            patient_icons.append(icon_label)

  

    def update_length_label(self):
        length = self.patient_pq.get_length()
        self.info_label.config(text=f"{length} Patients")

    def update_is_empty_label(self):
        is_empty = self.patient_pq.is_empty()
        self.info_label.config(text=f"Empty: {str(is_empty)}")

    def add_patient(self):
        age = int(self.patient_age.get())
        name = str(self.patient_name.get())
        self.patient_pq.add(age, name)

        self.draw_patients()

        self.patient_age.set("")
        self.patient_name.set("")

    def get_first_patient(self):
        if not self.patient_pq.is_empty():
            first_age, first_name = self.patient_pq.first_item()
            self.info_label.config(text=f"1st patient in queue: {first_name}, {first_age} years old", fg="green")
        else:
            self.info_label.config(text=f"No patient in the queue", fg="red")

    def remove_first_patient(self):
        if not self.patient_pq.is_empty():
            first_age, first_name = self.patient_pq.remove_first()
            self.draw_patients()
            self.info_label.config(text=f"Patient: {first_name}, {first_age} years old removed", fg="green")
        else:
            self.draw_patients()
            self.info_label.config(text=f"No patient in the queue", fg="red")
    

# List of candy colors
candy_colors = ['red', 'yellow', 'blue', 'green', 'orange', 'pink',
                'black', 'purple', 'brown', 'gray', 'cyan', 'magenta',
                'white', 'indigo']

root = tk.Tk()
app = CandyDispenserApp(root)
root.mainloop()

