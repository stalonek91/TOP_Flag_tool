import pandas as pd
file_path = '/Users/sylwestersojka/Documents/TOP_FLAG_CHECKER/template.csv'
csv_df = pd.read_csv(file_path, delimiter=',')

#Column Definition
GIC = 'Group in Charge'
TRIBE = 'Tribe of Group in Charge'
TOP_FLAG = 'Top Importance'
PRONTO = 'Pronto ID'
TOP_FLAG_VALUE = 'TOP1_'

result = csv_df[csv_df[TOP_FLAG].str.contains(TOP_FLAG_VALUE, na=False, case=False)]
# print(result[TRIBE].value_counts())

gic_set = set(result[GIC].unique())
gic_sorted = sorted(gic_set)
print(gic_sorted)

