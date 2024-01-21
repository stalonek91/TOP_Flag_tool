from customtkinter import *
import pandas as pd
import os

#Column Definition
GIC = 'Group in Charge'
TRIBE = 'Tribe of Group in Charge'
TOP_FLAG_COLUMN = 'Top Importance'
PRONTO = 'Pronto ID'
TOP_FLAG_VALUE = 'TOP1_'

global_csv_df = None

app = CTk()
app.geometry("600x400")
app.title('TOP flag tool')

set_appearance_mode('dark')
set_default_color_theme('blue')


frame_top = CTkFrame(master=app, fg_color='white', width=400, height=300)
frame_top.grid(column=0, row=2, padx=5, pady=5, columnspan=3, sticky='w', rowspan=6)

label_file_path = CTkLabel(master=app, text=f"File location: ")
label_file_path.grid(column=1, row=0, sticky='w')



def select_file():
    global global_csv_df
    file_path = filedialog.askopenfilename(title='Select a file',filetypes=[("CSV files", "*.csv")])
    file_path_output = os.path.join(os.path.basename(os.path.dirname(file_path)), os.path.basename(file_path))
    if file_path:
            global_csv_df = pd.read_csv(file_path, delimiter=',')
            label_file_path.configure(text=f"{file_path_output}", text_color='green')
            button_calculate.configure(state='normal')

        

def calculate_generic_view():
    global global_csv_df
    result = global_csv_df[global_csv_df[TOP_FLAG_COLUMN].str.contains(TOP_FLAG_VALUE, na=False, case=False)]
    gic_set = set(result[GIC].unique())
    gic_sorted = sorted(gic_set)

    top_set = set(result[TOP_FLAG_COLUMN].unique())
    print(top_set)



    
    combobox_gic.configure(values=gic_sorted)
    print(f'PRINTING TOPs: {top_set}')
    combobox_tops.configure(values=top_set)

    
    

button_load_file = CTkButton(master=app, text='Load csv file', command=select_file)
button_load_file.grid(column=0, row=0, padx=5, pady=5, sticky='w')

button_calculate = CTkButton(master=app, text="Calculate TOP's", command=calculate_generic_view, state='disabled')
button_calculate.grid(column=0, row=1, padx=5, pady=5, sticky='w')


combobox_tops = CTkComboBox(master=app, values=['Waiting for TOP flags'])
combobox_tops.grid(column=3, row=2, sticky='n')

combobox_gic = CTkComboBox(master=app, values=['Waiting for GIC'])
combobox_gic.grid(column=3, row=3, sticky='n')

label1 = CTkLabel(master=frame_top, text='Number of TOP1 prontos in metrics: ', text_color='black')
label1.grid(row=0, column=0, pady=5, sticky='w')

label2 = CTkLabel(master=frame_top, text='% of TOP1_program prontos in GIC:', text_color='black')
label2.grid(row=1, column=0, pady=5)

label3 = CTkLabel(master=frame_top, text='% of TOP1_program prontos in Tribe:', text_color='black')
label3.grid(row=2, column=0, pady=5)

label4 = CTkLabel(master=frame_top, text='% of all TOP1 in Tribe ', text_color='black')
label4.grid(row=3, column=0, pady=5, sticky='w')




app.mainloop()