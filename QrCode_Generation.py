from tkinter import *
from tkinter import messagebox, colorchooser
import qrcode
from PIL import Image, ImageTk
import os

# Function to generate QR code
def generate_qr():
    # Get user input
    url = entry_url.get()
    
    # Validate input
    if not url.strip():
        messagebox.showwarning("Warning", "Please enter a URL or text!")
        return
    
    try:
        # Get selected colors
        fill = fill_color.get()
        back = back_color.get()
        
        # Create QR code 
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create image with custom colors
        img = qr.make_image(fill_color=fill, back_color=back)
        
        # Save the image
        img.save("Generated_QRCode.png")
        
        # Display the QR code in the GUI
        display_qr = Image.open("Generated_QRCode.png")
        display_qr = display_qr.resize((180, 180), Image.Resampling.LANCZOS)
        qr_image = ImageTk.PhotoImage(display_qr)
        
        label_qr_display.config(image=qr_image)
        label_qr_display.image = qr_image
        
        # Show success message
        label_status.config(text="✓ QR Code Generated Successfully!", fg="#10b981")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR code: {str(e)}")
        label_status.config(text="✗ Generation Failed", fg="#ef4444")

# Function to choose fill color
def choose_fill_color():
    color = colorchooser.askcolor(title="Choose QR Code Color")
    if color[1]:
        fill_color.set(color[1])
        btn_fill_color.config(bg=color[1])

# Function to choose background color
def choose_back_color():
    color = colorchooser.askcolor(title="Choose Background Color")
    if color[1]:
        back_color.set(color[1])
        btn_back_color.config(bg=color[1])

# Function to clear all fields
def clear_all():
    entry_url.delete(0, END)
    label_qr_display.config(image='')
    label_status.config(text="")
    fill_color.set("black")
    back_color.set("white")
    btn_fill_color.config(bg="black")
    btn_back_color.config(bg="white")

# Create main window
root = Tk()
root.title("QR Code Generator")
root.geometry("600x650")
root.config(bg="#f8fafc")
root.resizable(False, False)

# Header Frame
header_frame = Frame(root, bg="#8b5cf6", height=100)
header_frame.pack(fill=X)

label_title = Label(
    header_frame,
    text="✨ QR Code Generator ✨",
    font=("Arial", 28, "bold"),
    bg="#8b5cf6",
    fg="white"
)
label_title.pack(pady=25)

# Main content frame
content_frame = Frame(root, bg="#f8fafc")
content_frame.pack(pady=20, padx=40, fill=BOTH, expand=True)

# URL Input Section
label_url = Label(
    content_frame,
    text="Enter URL or Text:",
    font=("Arial", 12, "bold"),
    bg="#f8fafc",
    fg="#1e293b"
)
label_url.pack(anchor=W, pady=(0, 5))

entry_url = Entry(
    content_frame,
    font=("Arial", 12),
    bg="white",
    fg="#1e293b",
    relief=SOLID,
    bd=2,
    highlightthickness=0
)
entry_url.pack(fill=X, ipady=10)

# Color customization frame
color_frame = Frame(content_frame, bg="#f8fafc")
color_frame.pack(pady=15, fill=X)

# Fill color
fill_color = StringVar(value="black")
label_fill = Label(
    color_frame,
    text="QR Code Color:",
    font=("Arial", 10, "bold"),
    bg="#f8fafc",
    fg="#1e293b"
)
label_fill.grid(row=0, column=0, sticky=W, pady=5)

btn_fill_color = Button(
    color_frame,
    text="Choose",
    command=choose_fill_color,
    bg="black",
    fg="white",
    font=("Arial", 9),
    relief=SOLID,
    bd=1,
    cursor="hand2",
    width=15
)
btn_fill_color.grid(row=0, column=1, padx=10)

# Background color
back_color = StringVar(value="white")
label_back = Label(
    color_frame,
    text="Background Color:",
    font=("Arial", 10, "bold"),
    bg="#f8fafc",
    fg="#1e293b"
)
label_back.grid(row=1, column=0, sticky=W, pady=5)

btn_back_color = Button(
    color_frame,
    text="Choose",
    command=choose_back_color,
    bg="white",
    fg="black",
    font=("Arial", 9),
    relief=SOLID,
    bd=1,
    cursor="hand2",
    width=15
)
btn_back_color.grid(row=1, column=1, padx=10)

# Button frame
button_frame = Frame(content_frame, bg="#f8fafc")
button_frame.pack(pady=12, fill=X)

btn_generate = Button(
    button_frame,
    text="Generate QR Code",
    command=generate_qr,
    bg="#8b5cf6",
    fg="white",
    font=("Arial", 12, "bold"),
    relief=FLAT,
    bd=0,
    cursor="hand2",
    padx=20,
    pady=12
)
btn_generate.pack(side=LEFT, expand=True, fill=X, padx=(0, 5))

btn_clear = Button(
    button_frame,
    text="Clear",
    command=clear_all,
    bg="#ef4444",
    fg="white",
    font=("Arial", 12, "bold"),
    relief=FLAT,
    bd=0,
    cursor="hand2",
    padx=20,
    pady=12
)
btn_clear.pack(side=LEFT, expand=True, fill=X, padx=(5, 0))

# Status label
label_status = Label(
    content_frame,
    text="",
    font=("Arial", 10, "bold"),
    bg="#f8fafc"
)
label_status.pack(pady=8)

# QR Code display frame
qr_display_frame = Frame(content_frame, bg="white", relief=SOLID, bd=2)
qr_display_frame.pack(pady=5)

label_qr_display = Label(
    qr_display_frame,
    bg="white",
    width=180,
    height=180
)
label_qr_display.pack(padx=8, pady=8)

# Footer
label_footer = Label(
    root,
    text="QR Code will be saved as 'Generated_QRCode.png' in the current directory",
    font=("Arial", 9),
    bg="#f8fafc",
    fg="#64748b"
)
label_footer.pack(side=BOTTOM, pady=10)

# Run the application
root.mainloop()