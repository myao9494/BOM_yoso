import pandas as pd
from bom_calculator import BOMCalculator

# テストデータ
sample_data = {
    'index': ['a', 'a___b', 'a__b__c'],
    'quantity_per_item': [3, 1, 10]
}
df = pd.DataFrame(sample_data)

calculator = BOMCalculator(df)
result_df = calculator.calculate_required_quantities()

print("Original Data:")
print(df)
print("\nResult:")
print(result_df)

# 階層構造を詳細に分析
print("\n階層構造分析:")
for i, row in df.iterrows():
    item_index = row['index']
    parts = item_index.split('__')
    print(f"Index: {item_index}")
    print(f"Parts: {parts}")
    print(f"Parent paths:")
    for j in range(len(parts) - 1):
        parent_path = '__'.join(parts[:j + 1])
        print(f"  {parent_path}")
    print()