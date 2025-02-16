import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, font=("Arial", 20), justify="right")
        self.entry.pack(fill="both", padx=10, pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
