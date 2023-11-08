import pandas as pd
file_path = './dataset.xlsx'
sheet_name = 'Purchasing data'
df = pd.read_excel(file_path, sheet_name=sheet_name, header=None, skiprows=1)
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write(df.to_csv(sep=';', index=False, header=False))