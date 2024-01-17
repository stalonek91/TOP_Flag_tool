import pandas as pd
import tkinter as tk
from tkinter import StringVar, filedialog

# Tkinter
window = tk.Tk()
window.geometry('500x500')
window.title('TOP Flag Tool')

# Labels
label = tk.Label(window, text="Select an option:")
label.grid(row=0, column=0, pady=5)

label_file_path = tk.Label(window, text="Selected file from: ")
label_file_path.grid(row=1, column=1, pady=5)

#OptionBar
selected_option = StringVar(window)
options = ["Load CSV file", "Quit Program"]
selected_option.set(options[0])

# Global var
csv_df = None

# Execute option commands
def execute_option(*args):
    global csv_df

    if selected_option.get() == options[0]:
        file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])
        if file_path:
            print(f"Following file was selected: {file_path}")
            csv_df = pd.read_csv(file_path, delimiter=',')
            
            
    elif selected_option.get() == options[1]:
        print('Selected QUIT')
        window.destroy()

dropdown_menu = tk.OptionMenu(window, selected_option, *options, command=execute_option)
dropdown_menu.grid(row=1, column=0, pady=5)


window.mainloop()




# print(list(csv_df.columns))

# pronto_count = csv_df['Pronto ID'].count()
# print(f'Number of prontos: {pronto_count}')

#Column Definition
GIC = 'Group in Charge'
TRIBE = 'Tribe of Group in Charge'
TOP_FLAG = 'Top Importance'
PRONTO = 'Pronto ID'

TOP_FLAG_VALUE = 'TOP1_24R'

def calculate_tops():
    result = csv_df[csv_df[TOP_FLAG].str.contains(TOP_FLAG_VALUE, na=False, case=False)]
    return result
    

def calculate_top_for_gic(result = calculate_tops(), selected_gic=None):
    result = csv_df[csv_df[TOP_FLAG].str.contains(TOP_FLAG_VALUE, na=False, case=False)]
    gic_counts = result[GIC].value_counts()
    
    for gic, count in gic_counts.items():
        if (selected_gic is None or gic == selected_gic) and count >= 3:
            print(f"{gic}: {count}")
         


