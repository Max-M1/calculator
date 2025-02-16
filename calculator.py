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
        self.buttons_frame.pack(expand=True, fill="both")

        btn_clear = tk.Button(
            self.buttons_frame, text="C", font=("Arial", 18), command=self.clear_entry
        )
        btn_clear.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text == "=":
                    btn_command = self.calculate
                else:
                    btn_command = lambda value=btn_text: self.add_to_expression(value)
                btn = tk.Button(
                    self.buttons_frame,
                    text=btn_text,
                    font=("Arial", 18),
                    command=btn_command,
                )
                btn.grid(row=i + 1, column=j, sticky="nsew")

        total_rows = len(buttons) + 1
        total_columns = 4
        for i in range(total_rows):
            self.buttons_frame.rowconfigure(i, weight=1)
        for j in range(total_columns):
            self.buttons_frame.columnconfigure(j, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
