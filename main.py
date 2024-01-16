import pandas as pd

file_path = '/Users/sylwestersojka/Documents/TOP_FLAG_CHECKER/template.csv'

csv_df = pd.read_csv(file_path, delimiter=',')
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
         
calculate_top_for_gic()


