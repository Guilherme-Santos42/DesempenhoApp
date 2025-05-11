import tkinter as tk
from tkinter import messagebox
import os
import subprocess

def clear_temp_files():
    if os.name == 'nt':  # Windows
        temp_path = os.getenv('TEMP')
        subprocess.run(f'del /f /s /q {temp_path}\\*', shell=True)
    else:  # Unix/Linux/MacOS
        temp_path = '/tmp'
        subprocess.run(f'rm -rf {temp_path}/*', shell=True)
    messagebox.showinfo("Success", "Temporary files cleared!")

def manage_startup_apps():
    if os.name == 'nt':  # Windows
        subprocess.run('start shell:startup', shell=True)
    else:
        messagebox.showinfo("Info", "Startup app management is not implemented for this OS.")

def clear_system_cache():
    if os.name == 'nt':  # Windows
        subprocess.run('ipconfig /flushdns', shell=True)
    else:  # Unix/Linux/MacOS
        subprocess.run('sync; sudo sysctl -w vm.drop_caches=3', shell=True)
    messagebox.showinfo("Success", "System cache cleared!")

def defragment_disk():
    if os.name == 'nt':  # Windows
        subprocess.run('defrag C:', shell=True)
    else:
        messagebox.showinfo("Info", "Disk defragmentation is only available on Windows.")

def optimize_system():
    """Run system optimizations."""
    if platform.system() == "Windows":
        os.system('chkdsk /f /r')
    elif platform.system() == "Linux":
        os.system('sudo e4defrag /')
    elif platform.system() == "Darwin":
        print("No specific optimization commands for macOS.")
    print("System optimized.")

def free_memory():
    if os.name != 'nt':  # Unix/Linux/MacOS
        subprocess.run('sync; echo 3 | sudo tee /proc/sys/vm/drop_caches', shell=True)
    messagebox.showinfo("Success", "Memory freed!")

def create_gui():
    root = tk.Tk()
    root.title("Dempenho V2 - Guilherme Albertin")

    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20)

    tk.Button(frame, text="Limpar Itens Temporários", command=clear_temp_files, width=30).pack(pady=5)
    tk.Button(frame, text="Gerenciar Apps", command=manage_startup_apps, width=30).pack(pady=5)
    tk.Button(frame, text="Liberar Cache Sistema", command=clear_system_cache, width=30).pack(pady=5)
    tk.Button(frame, text="Liberar Memória", command=free_memory, width=30).pack(pady=5)
    tk.Button(frame, text="Desfragmentar Disco (Demora)", command=defragment_disk, width=30).pack(pady=5)
    tk.Button(frame, text="Verificação de disco (Demora)", command=optimize_system, width=30).pack(pady=5)

    root.mainloop()



if __name__ == "__main__":
    create_gui()