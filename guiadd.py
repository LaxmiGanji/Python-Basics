import tkinter as tk

def add_numbers():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    label_result.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Addition Calculator")
label_num1 = tk.Label(root, text="Enter number 1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()
label_num2 = tk.Label(root, text="Enter number 2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()
add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack()
label_result = tk.Label(root, text="")
label_result.pack()
root.mainloop()
