import pandas as pd
import tkinter as tk
from tkinter import StringVar, filedialog

# Tkinter
window = tk.Tk()
window.geometry('700x500')
window.title('TOP Flag Tool')

# Labels
label = tk.Label(window, text="Select an option:")
label.grid(row=0, column=0, pady=5)

label_file_path = tk.Label(window, text="Selected file from: ")
label_file_path.grid(row=1, column=1, pady=5)

label_for_confirmation = tk.Label(window, text=f'test', width=30)
label_for_confirmation.grid(row=2, column=0, columnspan=2)

#OptionBar
selected_option = StringVar(window)
options = ["Load CSV file", "Quit Program"]
selected_option.set(options[0])

# Global var
csv_df = None

#Column Definition
GIC = 'Group in Charge'
TRIBE = 'Tribe of Group in Charge'
TOP_FLAG = 'Top Importance'
PRONTO = 'Pronto ID'

TOP_FLAG_VALUE = 'TOP1_24R'

def calculate_tops():
    if csv_df:
        result = csv_df[csv_df[TOP_FLAG].str.contains(TOP_FLAG_VALUE, na=False, case=False)]
        print(result)
        return result


def calculate_top_for_gic(result = calculate_tops(), selected_gic=None):
    result = csv_df[csv_df[TOP_FLAG].str.contains(TOP_FLAG_VALUE, na=False, case=False)]
    gic_counts = result[GIC].value_counts()
    
    for gic, count in gic_counts.items():
        if (selected_gic is None or gic == selected_gic) and count >= 3:
            print(f"{gic}: {count}")


def top1_flag_counter():
    top_flag_count = csv_df['TOP']

def show_frontline():
    pronto_count = csv_df['Pronto ID'].count()
    # top1_count = calculate_tops()
    label_for_confirmation["text"] = f'Number of prontos: {pronto_count}'

    
    

# Execute option commands
def execute_option(*args):
    global csv_df

    if selected_option.get() == options[0]:
        file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])
        if file_path:
            print(f"Following file was selected: {file_path}")
            csv_df = pd.read_csv(file_path, delimiter=',')
            label_file_path["text"] = f"CSV file: {file_path}"
            show_frontline()
            
            
    elif selected_option.get() == options[1]:
        print('Selected QUIT')
        window.destroy()

dropdown_menu = tk.OptionMenu(window, selected_option, *options, command=execute_option)
dropdown_menu.grid(row=1, column=0, pady=5)

window.mainloop()



