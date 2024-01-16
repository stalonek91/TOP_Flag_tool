import pandas as pd

file_path = '/Users/sylwestersojka/Documents/TOP_FLAG_CHECKER/template.csv'

csv_df = pd.read_csv(file_path, delimiter=',')
# print(list(csv_df.columns))

# pronto_count = csv_df['Pronto ID'].count()
# print(f'Number of prontos: {pronto_count}')

#Column Definition
gic = 'Group in Charge'
top_flag = 'Top Importance'
pronto = 'Pronto ID'

top_flag_value = 'ABIP'

result = csv_df[csv_df[top_flag].str.contains(top_flag_value, na=False, case=False)]
print(result[gic])

gic_counts = result[gic].value_counts()

# Print the result
for gic, count in gic_counts.items():
    print(f"{gic}: {count}")





