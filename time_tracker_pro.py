import tkinter as tk
import datetime
import csv

class TimeTrackerPro:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x350+50+50")
        self.root.title("Time Tracker Pro")

        self.timer_running = False
        self.start_time = None
        self.project_name = ""
        self.task_description = ""

        self.lbl_time = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.lbl_project = tk.Label(root, text="Project: ")
        self.lbl_description = tk.Label(root, text="Task Description: ")
        self.entry_project = tk.Entry(root)
        self.entry_description = tk.Entry(root)
        self.btn_start = tk.Button(root, text="Start", command=self.start_timer)
        self.btn_stop = tk.Button(root, text="Stop", command=self.stop_timer)
        self.btn_save = tk.Button(root, text="Save", command=self.save_entry)

        self.lbl_time.pack(pady=20)
        self.lbl_project.pack()
        self.entry_project.pack()
        self.lbl_description.pack()
        self.entry_description.pack()
        self.btn_start.pack(pady=10)
        self.btn_stop.pack(pady=10)
        self.btn_save.pack(pady=10)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = datetime.datetime.now()
            self.update_timer()

            self.project_name = self.entry_project.get()
            self.task_description = self.entry_description.get()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False

    def save_entry(self):
        entry_data = {
            "Project": self.project_name,
            "Description": self.task_description,
            "StartTime": self.start_time,
            "EndTime": datetime.datetime.now()
        }
        
        now = datetime.datetime.now()
        filename = entry_data["Project"] + '-' + str(now) + ".csv"
        with open(filename, 'w') as f:
            w = csv.DictWriter(f, entry_data.keys())
            w.writeheader()
            w.writerow(entry_data)


    def update_timer(self):
        if self.timer_running:
            elapsed_time = datetime.datetime.now() - self.start_time
            elapsed_time_str = str(elapsed_time).split(".")[0]  # Format: HH:MM:SS
            self.lbl_time.config(text=elapsed_time_str)
            self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeTrackerPro(root)
    root.iconphoto(False, tk.PhotoImage(file="icon.png"))
    root.mainloop()

