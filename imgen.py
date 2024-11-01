from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
from tkinter import simpledialog
from PIL import ImageTk, Image
import cv2
import PIL
import numpy as np

window = Tk()
window.geometry("1000x700")
window.title("Image Encryption Decryption")
window.configure(bg='pink')

# Global variables
count, emig = 0, None
frp = []
tname = []
con, bright = 1, 0
panelB, panelA = None, None
encryption_key = None
decryption_key = None  # Initialize decryption_key

def getpath(path):
    a = path.split(r'/')
    fname = a[-1]
    l = len(fname)
    location = path[:-l]
    return location

def getfoldername(path):
    a = path.split(r'/')
    name = a[-1]
    return name

def getfilename(path):
    a = path.split(r'/')
    fname = a[-1]
    a = fname.split('.')
    a = a[0]
    return a

def openfilename():
    filename = filedialog.askopenfilename(title='"pen')
    return filename

def open_img():
    global x, panelA, panelB, enb, deb
    global count, eimg, location, filename
    count = 0
    x = openfilename()
    img = Image.open(x)

    # Resize the image to 12x12
    target_size = (320, 320)
    img = img.resize(target_size, resample=Image.BICUBIC)

    eimg = img
    img = ImageTk.PhotoImage(img)
    temp = x
    location = getpath(temp)
    filename = getfilename(temp)

    if panelA is None or panelB is None:
        panelA = Label(image=img)
        panelA.image = img
        panelA.pack(side="left", padx=10, pady=10)

        panelB = Label(image=img)
        panelB.image = img
        panelB.pack(side="right", padx=10, pady=10)

        enb = Button(window, text="Encrypt", command=ask_encryption_key, font=("Arial", 20), bg="green",
                     fg="blue", borderwidth=3, relief="raised")
        enb.place(x=150, y=620)

        deb = Button(window, text="Decrypt", command=ask_decryption_key, font=("Arial", 20), bg="green", fg="white",
                     borderwidth=3, relief="raised")
        deb.place(x=450, y=620)

    else:
        panelA.configure(image=img)
        panelB.configure(image=img)
        panelA.image = img
        panelB.image = img

        if deb is not None:
            deb.destroy()

    deb['state'] = NORMAL if enb is not None else DISABLED

def ask_encryption_key():
    global encryption_key
    encryption_key = simpledialog.askstring("Encryption Key", "Enter the encryption key:")
    if encryption_key:
        en_fun()

def ask_decryption_key():
    global decryption_key
    decryption_key = simpledialog.askstring("Decryption Key", "Enter the decryption key:")
    if decryption_key:
        de_fun()

def en_fun():
    global x, image_encrypted, key, panelB
    image_input = cv2.imread(x, 0)
    (x1, y) = image_input.shape
    image_input = image_input.astype(float) / 255.0

    mu, sigma = 0, 0.1
    key = np.random.normal(mu, sigma, (x1, y)) + np.finfo(float).eps
    image_encrypted = image_input / key

    # Resize the encrypted image to fit the target size (e.g., 12x12)
    target_size = (320, 320)
    encrypted_image_resized = cv2.resize(image_encrypted, target_size)

    cv2.imwrite('image_encrypted.jpg', encrypted_image_resized * 255)

    imge = Image.open('image_encrypted.jpg')
    imge = ImageTk.PhotoImage(imge)
    panelB.configure(image=imge)
    panelB.image = imge
    mbox.showinfo("Encrypt Status", "Image Encrypted successfully.")

def de_fun():
    global image_encrypted, key, panelB, decryption_key, encryption_key
    if decryption_key == encryption_key:
        image_output = image_encrypted * key
        image_output *= 255.0

        # Resize the decrypted image to fit the target size (e.g., 12x12)
        target_size = (320, 320)
        decrypted_image_resized = cv2.resize(image_output, target_size)

        cv2.imwrite('image_output.jpg', decrypted_image_resized)

        imgd = Image.open('image_output.jpg')
        imgd = ImageTk.PhotoImage(imgd)
        panelB.configure(image=imgd)
        panelB.image = imgd
        mbox.showinfo("Decrypt Status", "Image decrypted successfully.")
    else:
        mbox.showwarning("Warning", "Invalid Decryption Key. Please enter the correct key.")

def reset():
    global x, panelB, eimg
    image = cv2.imread(x)[:, :, ::-1]

    # Resize the image to fit the target size (e.g., 12x12)
    target_size = (320, 320)
    resized_image = cv2.resize(image, target_size)

    eimg = Image.fromarray(resized_image)
    img = ImageTk.PhotoImage(eimg)

    panelB.configure(image=img)
    panelB.image = img

    mbox.showinfo("Success", "Image reset to original format!")

def save_img():
    global location, filename, image_encrypted
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    cv2.imwrite(filename.name, image_encrypted * 255)  # Save the encrypted image
    mbox.showinfo("Success", "Encrypted Image Saved Successfully!")


start1 = tk.Label(text="Image Encryption \nDecryption", font=("Times new roman", 40), fg="slate blue")
start1.place(x=350, y=10)

start1 = tk.Label(text="Original\nImage", font=("Times new roman", 25), fg="grey")
start1.place(x=100, y=270)

start1 = tk.Label(text="Encrypted or\nDecrypted\nImage", font=("Times new roman", 25), fg="grey")
start1.place(x=700, y=230)

chooseb = Button(window, text="Choose", command=open_img, font=("Times new roman", 20), bg="plum", fg="navy", borderwidth=3,
                 relief="raised")
chooseb.place(x=30, y=20)

saveb = Button(window, text="Save", command=save_img, font=("Times new roman", 20), bg="plum", fg="navy", borderwidth=3,
               relief="raised")
saveb.place(x=170, y=20)

enb = Button(window, text="Encrypt", command=ask_encryption_key, font=("Times new roman", 20), bg="aqua", fg="darkmagenta",
             borderwidth=3, relief="raised")
enb.place(x=150, y=620)

deb = Button(window, text="Decrypt", command=ask_decryption_key, font=("Times new roman", 20), bg="hotpink", fg="darkmagenta",
             borderwidth=3, relief="raised")
deb.place(x=450, y=620)

resetb = Button(window, text="Reset", command=reset, font=("Times new roman", 20), bg="mediumseagreen", fg="darkviolet", borderwidth=3,
                relief="raised")
resetb.place(x=800, y=620)

exitb = Button(window, text="EXIT", command=window.destroy, font=("Times new roman", 20), bg="red", fg="dodgerblue", borderwidth=3,
               relief="raised")
exitb.place(x=880, y=20)

window.protocol("WM_DELETE_WINDOW", window.destroy)
window.mainloop()