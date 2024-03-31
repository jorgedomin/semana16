from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tasks = []
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)

        self.task_list = tk.Listbox(root, width=50)
        self.task_list.pack()

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(root, text="Completada", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(root, text="Eliminar", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.root.bind("<Escape>", self.close_app)
        self.root.bind("<Delete>", self.delete_task)
        self.root.bind("<KeyPress-c>", self.complete_task)

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def complete_task(self, event=None):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            self.task_list.itemconfig(index, {'bg': 'green'})
            self.tasks[index] = "✓ " + self.tasks[index]

    def delete_task(self, event=None):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            self.task_list.delete(index)
            del self.tasks[index]

    def close_app(self, event=None):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
