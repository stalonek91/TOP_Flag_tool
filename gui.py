from customtkinter import *
import pandas as pd
import os
import logging

#Logging config
logging.basicConfig(level=logging.INFO)

#Column Definition
GIC = 'Group in Charge'
TRIBE = 'Tribe of Group in Charge'
TOP_FLAG_COLUMN = 'Top Importance'
PRONTO = 'Pronto ID'
TOP_FLAG_VALUE = 'TOP'

global_csv_df = None
selected_gic = None

app = CTk()
app.geometry("600x400")
app.title('TOP flag tool')

set_appearance_mode('dark')
set_default_color_theme('blue')


frame_top = CTkFrame(master=app, fg_color='white', width=400, height=300)
frame_top.grid(column=0, row=2, padx=5, pady=5, columnspan=3, sticky='w', rowspan=6)
frame_top.propagate(False)

label_file_path = CTkLabel(master=app, text=f"File location: ")
label_file_path.grid(column=1, row=0, sticky='w')



def select_file():
    logging.info(f"Function SELECT_FILE started")


    global global_csv_df
    file_path = filedialog.askopenfilename(title='Select a file',filetypes=[("CSV files", "*.csv")])
    logging.info(f"Opend Finder for CSV file")

    file_path_output = os.path.join(os.path.basename(os.path.dirname(file_path)), os.path.basename(file_path))
    if file_path:
            logging.info(f"File SELECTED SUCCESFULY")
            global_csv_df = pd.read_csv(file_path, delimiter=',')
            label_file_path.configure(text=f"{file_path_output}", text_color='green')
            logging.info(f"Label changed for FILE PATH")
            button_calculate.configure(state='normal')




def calculate_generic_view():
    logging.info(f"Function CALCULATE_GENERIC_VIEW started")

    global global_csv_df
    result = global_csv_df[global_csv_df[TOP_FLAG_COLUMN].str.contains(TOP_FLAG_VALUE, na=False, case=False)]
    gic_set = set(result[GIC].unique())
    gic_sorted = sorted(gic_set)

    top_set = list(result[TOP_FLAG_COLUMN].unique())
    
    flattened_list = list()

    for item in top_set:
        if isinstance(item, list):
            flattened_list.extend(item)
        elif isinstance(item, str) and ',' in item:
             flattened_list.extend(item.split(', '))
        else:
             flattened_list.append(item)

    combobox_gic.configure(values=gic_sorted)
    combobox_tops.configure(values=flattened_list)
    logging.info(f"Comboboxes updated with values")


    #Count of all Prontos:
    prontos_count = global_csv_df[PRONTO].count()
    label1.configure(text=f"Number of prontos: {prontos_count}   ")

    #Count of all TOP1 prontos
    top1_count = global_csv_df[global_csv_df[TOP_FLAG_COLUMN].str.contains('TOP1_', na=False)]
    top1_count = top1_count[TOP_FLAG_COLUMN].count()
    
    perc_top1 = (top1_count / prontos_count) * 100
 
    label2.configure(text=f"Number TOP1: {top1_count} which is: {perc_top1:.2f}% of all Prontos  ")

    #Count of TOP2 prontos 

    top2_count = global_csv_df[global_csv_df[TOP_FLAG_COLUMN].str.contains('TOP2_', na=False)]
    top2_count = top2_count[TOP_FLAG_COLUMN].count()
    
    perc_top2 = (top2_count / prontos_count) * 100
 
    label3.configure(text=f"Number TOP2: {top2_count} which is: {perc_top2:.2f}% of all Prontos  ")

    #Count of TOP3 prontos 

    top3_count = global_csv_df[global_csv_df[TOP_FLAG_COLUMN].str.contains('TOP3_', na=False)]
    top3_count = top3_count[TOP_FLAG_COLUMN].count()
    
    perc_top3 = (top3_count / prontos_count) * 100
 
    label4.configure(text=f"Number TOP3: {top3_count} which is: {perc_top3:.2f}% of all Prontos  ")

    #Count of NON TOP prontos 

    top_none_count = prontos_count - (top1_count + top2_count + top3_count)
    perc_top_none = (top_none_count / prontos_count) * 100
    label4.configure(text=f"Number non TOP prontos: {top_none_count} which is: {perc_top_none:.2f}% of all Prontos  ")

    logging.info(f'Generic view created')



def calculate_tops_per_gic():
    logging.info(f'calculate_tops_per_gic fuction started')
    global global_csv_df, selected_gic

    if not selected_gic:
         logging.error('GIC not selected')
         return

    result = global_csv_df[global_csv_df[GIC] == selected_gic]
    result['TOP_format'] = result[TOP_FLAG_COLUMN].str.extract(r'(TOP\d*)')
    top_flag_counts = result['TOP_format'].value_counts()

    top_counts = {}

    for top_flag, count in top_flag_counts.items():
        top_counts[top_flag] = count

    top_keys = ['TOP1', 'TOP2', 'TOP3']
    labels = [label1, label2, label3]
    
    print(f'Print count for selected GIC')
    for top_key, label in zip(top_keys, labels):
         count = top_counts.get(top_key, 0)
         print(f' {top_key} = {count}')
         label.configure(text=f"Count of {top_key}: {count}")
         logging.info(f'Updated label for {top_key} with count {count}')


    

    logging.info(f'updated labels for TOP"s')



def on_gic_select(event):
    global selected_gic
    selected_gic = combobox_gic.get()
    print(f"Selected GIC: {selected_gic}")  # Debugging print statement


def update_selected_gic(event=None):
     global selected_gic
     selected_gic = combobox_gic.get()
     print(f"Selected GIC: {selected_gic}")


     
    

button_load_file = CTkButton(master=app, text='Load csv file', command=select_file)
button_load_file.grid(column=0, row=0, padx=5, pady=5, sticky='w')

button_calculate = CTkButton(master=app, text="Calculate TOP's", command=calculate_generic_view, state='disabled')
button_calculate.grid(column=0, row=1, padx=5, pady=5, sticky='w')

button_calculate_top_gic = CTkButton(master=app, text="Calculate TOP/GIC count", command=calculate_tops_per_gic)
button_calculate_top_gic.grid(column=3, row=4, padx=5, pady=5, sticky='w')

combobox_tops = CTkComboBox(master=app, values=['--'])
combobox_tops.grid(column=3, row=2, sticky='n')

combobox_gic = CTkComboBox(master=app, values=['--'], command=update_selected_gic)
combobox_gic.grid(column=3, row=3, sticky='n')
combobox_gic.bind("<<ComboboxSelected>>", on_gic_select)

label1 = CTkLabel(master=frame_top, text='', text_color='black')
label1.grid(row=0, column=0, pady=5)

label2 = CTkLabel(master=frame_top, text='', text_color='black')
label2.grid(row=1, column=0, pady=5)

label3 = CTkLabel(master=frame_top, text='', text_color='black')
label3.grid(row=2, column=0, pady=5)

label4 = CTkLabel(master=frame_top, text='', text_color='black')
label4.grid(row=3, column=0, pady=5)

label5 = CTkLabel(master=frame_top, text='', text_color='black')
label5.grid(row=4, column=0, pady=5)






app.mainloop()