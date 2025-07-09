#!/usr/bin/env python3
"""
BOM階層構造から必要手配個数を計算する使用例
"""

import pandas as pd
from bom_calculator import BOMCalculator

def main():
    # 仕様に基づくサンプルデータ
    sample_data = {
        'index': ['a', 'a___b', 'a__b__c'],
        'quantity_per_item': [3, 1, 10]
    }
    
    print("=== BOM階層構造と必要手配個数計算 ===")
    print()
    
    # 元のデータ
    df = pd.DataFrame(sample_data)
    print("元のデータ:")
    print(df)
    print()
    
    # 計算実行
    calculator = BOMCalculator(df)
    result_df = calculator.calculate_required_quantities()
    
    print("計算結果:")
    print(result_df)
    print()
    
    # 結果の説明
    print("計算式の説明:")
    for i, row in result_df.iterrows():
        print(f"{row['index']}: {row['formula']} = {row['required_quantity']}個")
    print()
    
    # より複雑な階層構造の例
    print("=== より複雑な階層構造の例 ===")
    complex_data = {
        'index': ['product_x', 'product_x___assembly_y', 'product_x___assembly_z', 
                  'product_x__assembly_y__part_w', 'product_x__assembly_z__part_v'],
        'quantity_per_item': [2, 3, 5, 4, 7]
    }
    
    df_complex = pd.DataFrame(complex_data)
    print("複雑な階層構造:")
    print(df_complex)
    print()
    
    calculator_complex = BOMCalculator(df_complex)
    result_complex = calculator_complex.calculate_required_quantities()
    
    print("計算結果:")
    print(result_complex)
    print()
    
    print("計算式の説明:")
    for i, row in result_complex.iterrows():
        print(f"{row['index']}: {row['formula']} = {row['required_quantity']}個")

if __name__ == "__main__":
    main()