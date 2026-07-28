import pandas as pd

data = {
    ' Name ': [' zahid ', 'ZA HID', ' Zahid ', None, '  syed  ', 'ZAHID'],
    'Amount': ['500', ' 600 ', None, '450', 'abc', '350'],
    ' Date ': ['2026-07-01', '01/07/2026', '2026/07/02', 'July 3 2026', None, '2026-07-03'],
    'Category': [' FOOD ', 'food', 'FOOD', ' Movie ', 'transport', ' FOOD  ']
}

df = pd.DataFrame(data)
df.to_excel('week1_python/dirty_expenses.xlsx', index=False)
print("dirty_expenses.xlsx created with mess")