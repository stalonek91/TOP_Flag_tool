from customtkinter import *
import pandas as pd
import os

app = CTk()
app.geometry("600x400")
app.title('TOP flag tool')

set_appearance_mode('dark')
set_default_color_theme('blue')


frame_top = CTkFrame(master=app, fg_color='white', width=400, height=300)
frame_top.grid(column=0, row=2, padx=5, pady=5, columnspan=3, sticky='w', rowspan=3)

label_file_path = CTkLabel(master=app, text=f"File location: ")
label_file_path.grid(column=1, row=0, sticky='w')

def select_file():
    file_path = filedialog.askopenfilename(title='Select a file',filetypes=[("CSV files", "*.csv")])
    file_path_output = os.path.join(os.path.basename(os.path.dirname(file_path)), os.path.basename(file_path))
    if file_path:
            csv_df = pd.read_csv(file_path, delimiter=',')
            label_file_path.configure(text=f"{file_path_output}", text_color='green')
        
    
button_load_file = CTkButton(master=app, text='Load csv file', command=select_file)
button_load_file.grid(column=0, row=0, padx=5, pady=5, sticky='w')

combobox_tops = CTkComboBox(master=app, values=['TOP1', 'TOP2', 'TOP3'])
combobox_tops.grid(column=3, row=2, sticky='n')






app.mainloop()