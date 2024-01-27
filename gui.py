import tkinter as tk
from tkinter import ttk
from quantum_xor import run_xor_simulation
from io import BytesIO
from PIL import Image, ImageTk


def run_simulation():
    input1 = int(input1_var.get())
    input2 = int(input2_var.get())
    output, circuit_image = run_xor_simulation(input1, input2)

    # Konwersja obrazu obwodu na format Tkinter
    img_buffer = BytesIO()
    circuit_image.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    pil_image = Image.open(img_buffer)
    tk_image = ImageTk.PhotoImage(pil_image)

    # Aktualizacja etykiet w GUI
    output_label.config(text=f"Wynik: {output}")
    circuit_label.config(image=tk_image)
    circuit_label.image = tk_image  # Trzymamy referencję do obrazu


# Ustawienie głównego okna
root = tk.Tk()
root.title("Kwantowa Bramka XOR")

# Tworzenie widgetów
input1_var = tk.StringVar(value='0')
input2_var = tk.StringVar(value='0')

input1_label = ttk.Label(root, text="Wejście 1 (0/1):")
input1_entry = ttk.Entry(root, textvariable=input1_var)

input2_label = ttk.Label(root, text="Wejście 2 (0/1):")
input2_entry = ttk.Entry(root, textvariable=input2_var)

run_button = ttk.Button(root, text="Uruchom symulację", command=run_simulation)
output_label = ttk.Label(root, text="Wynik: ")

# Dodanie etykiety do wyświetlania obwodu
circuit_label = ttk.Label(root)
circuit_label.pack()

# Układanie widgetów
input1_label.pack()
input1_entry.pack()
input2_label.pack()
input2_entry.pack()
run_button.pack()
output_label.pack()

# Uruchomienie głównej pętli
root.mainloop()
