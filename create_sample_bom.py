#!/usr/bin/env python3
"""
複数のBOMサンプルデータを作成し、CSVで出力
"""

import pandas as pd
from bom_calculator import BOMCalculator

def create_sample_bom_data():
    """複数のBOMサンプルデータを作成"""
    
    # 複数の製品とその階層構造
    bom_data = {
        'index': [
            # 製品A系統
            'product_a',
            'product_a___frame',
            'product_a___engine',
            'product_a___wheel',
            'product_a__frame__steel_plate',
            'product_a__frame__bolt',
            'product_a__engine__cylinder',
            'product_a__engine__piston',
            'product_a__wheel__tire',
            'product_a__wheel__rim',
            
            # 製品B系統
            'product_b',
            'product_b___chassis',
            'product_b___motor',
            'product_b__chassis__aluminum_frame',
            'product_b__chassis__connector',
            'product_b__motor__coil',
            'product_b__motor__magnet',
            
            # 製品C系統
            'product_c',
            'product_c___body',
            'product_c___control_unit',
            'product_c__body__plastic_case',
            'product_c__body__screw',
            'product_c__control_unit__pcb',
            'product_c__control_unit__chip',
            
            # 製品D系統（単純な階層）
            'product_d',
            'product_d___assembly_x',
            'product_d__assembly_x__part_y',
            
            # 製品E系統（複雑な階層）
            'product_e',
            'product_e___main_assembly',
            'product_e___sub_assembly',
            'product_e__main_assembly__component_1',
            'product_e__main_assembly__component_2',
            'product_e__sub_assembly__component_3',
            'product_e__sub_assembly__component_4',
        ],
        'quantity_per_item': [
            # 製品A系統
            1,   # product_a
            1,   # product_a___frame
            1,   # product_a___engine
            4,   # product_a___wheel (4個の車輪)
            2,   # product_a__frame__steel_plate
            8,   # product_a__frame__bolt
            1,   # product_a__engine__cylinder
            4,   # product_a__engine__piston
            1,   # product_a__wheel__tire
            1,   # product_a__wheel__rim
            
            # 製品B系統
            2,   # product_b (2台製造)
            1,   # product_b___chassis
            2,   # product_b___motor (2個のモーター)
            1,   # product_b__chassis__aluminum_frame
            6,   # product_b__chassis__connector
            3,   # product_b__motor__coil
            2,   # product_b__motor__magnet
            
            # 製品C系統
            5,   # product_c (5台製造)
            1,   # product_c___body
            1,   # product_c___control_unit
            1,   # product_c__body__plastic_case
            4,   # product_c__body__screw
            1,   # product_c__control_unit__pcb
            1,   # product_c__control_unit__chip
            
            # 製品D系統
            3,   # product_d (3台製造)
            2,   # product_d___assembly_x
            10,  # product_d__assembly_x__part_y
            
            # 製品E系統
            1,   # product_e
            1,   # product_e___main_assembly
            2,   # product_e___sub_assembly
            3,   # product_e__main_assembly__component_1
            5,   # product_e__main_assembly__component_2
            4,   # product_e__sub_assembly__component_3
            6,   # product_e__sub_assembly__component_4
        ]
    }
    
    return pd.DataFrame(bom_data)

def main():
    """メイン処理"""
    print("=== 複数BOMサンプルデータの作成 ===")
    
    # サンプルデータ作成
    bom_df = create_sample_bom_data()
    
    print("作成されたBOMデータ:")
    print(bom_df)
    print(f"\n総レコード数: {len(bom_df)}")
    
    # CSVファイルとして出力
    output_file = "sample_bom_data.csv"
    bom_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\nBOMデータを {output_file} に保存しました。")
    
    # 必要手配個数を計算
    print("\n=== 必要手配個数の計算 ===")
    calculator = BOMCalculator(bom_df)
    result_df = calculator.calculate_required_quantities()
    
    print("計算結果:")
    print(result_df)
    
    # 結果をCSVで出力
    result_output_file = "sample_bom_result.csv"
    result_df.to_csv(result_output_file, index=False, encoding='utf-8')
    print(f"\n計算結果を {result_output_file} に保存しました。")
    
    # 製品別の集計情報を表示
    print("\n=== 製品別集計情報 ===")
    products = result_df[~result_df['index'].str.contains('___')]['index'].unique()
    
    for product in products:
        product_data = result_df[result_df['index'].str.startswith(product)]
        print(f"\n{product}:")
        print(f"  総部品数: {len(product_data)}")
        print(f"  最大必要手配個数: {product_data['required_quantity'].max()}")
        print(f"  部品一覧:")
        for _, row in product_data.iterrows():
            print(f"    {row['index']}: {row['required_quantity']}個")

if __name__ == "__main__":
    main()