import tkinter as tk
from tkinter import ttk
from cpu_memory import get_cpu_usage, get_memory_usage  # functions from cpu_memory
from disk_module import get_disk_info


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("System Monitoring Application")
        self.geometry("800x600")  # Initial size of the window

        # Adding a notebook widget to manage the tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        # Tabs
        self.cpu_tab = self.add_tab("CPU")
        self.memory_tab = self.add_tab("Memory")
        self.disk_tab = self.add_tab("Disk")  # Disk Tab
        self.network_tab = self.add_tab("Network", "Network Data")
        self.help_tab = self.add_tab("Help", "Help Content")

        # CPU and Memory Labels
        self.cpu_label = ttk.Label(self.cpu_tab, text="Initializing...")
        self.cpu_label.pack()
        self.memory_label = ttk.Label(self.memory_tab, text="Initializing...")
        self.memory_label.pack()

        # Disk Label (Integration)
        self.disk_label = ttk.Label(self.disk_tab, text="Initializing...")  # Disk Tab Content
        self.disk_label.pack()

        # Control Buttons
        self.add_control_buttons()

        # Update function metrics
        self.after(1000, self.update_metrics)

    def add_tab(self, text, content=None):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=text)

        if content:
            label = ttk.Label(tab, text=content)
            label.pack(expand=True, fill="both")
        return tab

    def add_control_buttons(self):
        button_frame = ttk.Frame(self)
        button_frame.pack(side="bottom", fill="x")

        refresh_button = ttk.Button(button_frame, text="Refresh", command=self.refresh_data)
        refresh_button.pack(side="left")

        settings_button = ttk.Button(button_frame, text="Settings", command=self.open_settings)
        settings_button.pack(side="left")

        exit_button = ttk.Button(button_frame, text="Exit", command=self.quit)
        exit_button.pack(side="right")

    def refresh_data(self):
        self.update_metrics()

    def open_settings(self):
        # Placeholder for settings dialog functionality
        pass

    def update_metrics(self):
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        self.cpu_label.config(text=f"CPU Usage: {cpu_usage:.2f}%")
        self.memory_label.config(text=f"Memory Usage: {memory_usage:.2f}%")

        disk_info = get_disk_info()
        disk_text = "\n".join([f"{disk['device']}: {disk['percent']}% used" for disk in disk_info])
        self.disk_label.config(text=f"Disk Usage:\n{disk_text}")

        self.after(1000, self.update_metrics)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
