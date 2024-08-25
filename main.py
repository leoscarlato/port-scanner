import socket
import tkinter as tk
from tkinter import messagebox
from ports import well_known_ports

# Project: Port Scanner
# Details in README.md

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    
    except Exception as e:
        return_message = f"Erro ao verificar a porta {port}: {str(e)}\n"
        text_result.insert(tk.END, return_message)
        window.update_idletasks()
        return False

def scan_range():
    host = entry_host.get()
    
    if not host:
        messagebox.showerror("Erro", "Insira um host válido.")
        return

    try:
        start_port = int(entry_start_port.get())
        end_port = int(entry_end_port.get())
        if start_port < 0 or end_port < 0 or start_port > 65535 or end_port > 65535 or start_port > end_port:
            messagebox.showerror("Erro", "Insira um valor válido para a porta (0-65535), com a porta de início sendo menor que a porta final.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Insira valores inteiros válidos.")
        return

    text_result.delete("1.0", tk.END)
    status_label.config(text="Verificando portas, aguarde...") 

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            service = well_known_ports.get(port, "Unknown")
            result_message = f"Porta {port} está aberta - {service}.\n"
        else:
            result_message = f"Porta {port} está fechada\n"
        text_result.insert(tk.END, result_message)
        window.update_idletasks()
    text_result.insert(tk.END, "Verificação finalizada\n")
    status_label.config(text="")  

window = tk.Tk()
window.title("Port Scanner")
window.geometry("1280x720")

label_title = tk.Label(window, text="Port Scanner", font=("Arial Bold", 30))
label_title.pack()

label_host = tk.Label(window, text="Host:", font=("Arial", 12))
label_host.pack()
entry_host = tk.Entry(window)
entry_host.pack()

label_start_port = tk.Label(window, text="Porta inicial:", font=("Arial", 12))
label_start_port.pack()
entry_start_port = tk.Entry(window)
entry_start_port.pack()

label_end_port = tk.Label(window, text="Porta final:", font=("Arial", 12))
label_end_port.pack()
entry_end_port = tk.Entry(window)
entry_end_port.pack()

button_scan = tk.Button(window, text="Começar verificação", command=scan_range)
button_scan.pack()

text_result = tk.Text(window)
text_result.pack()

status_label = tk.Label(window, text="", font=("Arial", 12))
status_label.pack()

window.mainloop()
