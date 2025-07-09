import pandas as pd

# 仕様の例
sample_data = {
    'index': ['a', 'a___b', 'a__b__c'],
    'quantity_per_item': [3, 1, 10]
}
df = pd.DataFrame(sample_data)

print("階層構造の分析:")
print("仕様: a, a___b, a__b__c")
print("意味: a(ルート), a___b(aの子供b), a__b__c(bの子供c)")
print()

for i, row in df.iterrows():
    item_index = row['index']
    print(f"Index: {item_index}")
    
    # 階層レベルを分析
    level = item_index.count('__')
    print(f"  Level: {level}")
    
    # 親パスを探す
    if '__' in item_index:
        # 最後の '__' 以降を削除して親パスを取得
        last_separator_index = item_index.rfind('__')
        parent_path = item_index[:last_separator_index]
        print(f"  Parent path: {parent_path}")
        
        # 親が存在するかチェック
        parent_exists = parent_path in df['index'].values
        print(f"  Parent exists: {parent_exists}")
        
        if parent_exists:
            parent_qty = df[df['index'] == parent_path]['quantity_per_item'].iloc[0]
            print(f"  Parent quantity: {parent_qty}")
    else:
        print(f"  Root item")
    
    print()