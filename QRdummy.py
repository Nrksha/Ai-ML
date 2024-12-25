import qrcode
import json
from tkinter import *


# Function to collect data and return it
def student_data():
    name = entry_name.get()  # get name from the entry widget
    rollno = entry_rollno.get()  # get roll no from the entry widget
    student_info = {"name": name, "rollno": rollno}
    return student_info


# Function to generate QR code
def qr():
    student_info = student_data()  # Get student info
    student_json = json.dumps(student_info)  # Convert info to JSON
    qr_code = qrcode.make(student_json)  # Generate QR code with JSON data
    qr_code.save("qr.jpg")  # Save the QR code as an image
    qr_label.config(text="QR Code generated and saved as qr.jpg")


def exit_qr():
    root.destroy()


# Create main Tkinter window
root = Tk()
root.title("---STUDENT QR CODE GENERATOR---")
root.config(bg="#000000")

# Label for name input
label_name = Label(root, text="name:", bg="#E6E6FA")
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Entry widget for name
entry_name = Entry(root, width=50)
entry_name.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Label for roll number input
label_rollno = Label(root, text="roll number:", bg="#E6E6FA")
label_rollno.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Entry widget for roll number
entry_rollno = Entry(root, width=50)
entry_rollno.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Button to trigger QR code generation
button = Button(root, bg="#008000", text="Generate QR Code", command=qr)
button.grid(row=2, column=0, columnspan=2, padx=100,pady=100, sticky="w")
exit_button = Button(root, bg="#AE2321", text="cancel", command=exit_qr)
exit_button.grid(row=2, column=0, columnspan=2, padx=100,pady=100,sticky="e")
# Label to show result of QR code generation
qr_label = Label(root)
qr_label.grid(row=3, column=0, columnspan=2, pady=10, sticky="w")

# Run the Tkinter main loop
root.mainloop()
