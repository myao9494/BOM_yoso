import unittest
import pandas as pd
import sys
import os

# テスト対象のモジュールをインポート
from bom_calculator import BOMCalculator


class TestBOMCalculator(unittest.TestCase):
    
    def setUp(self):
        """テスト用のサンプルデータを準備"""
        self.sample_data = {
            'index': ['a', 'a___b', 'a__b__c'],
            'quantity_per_item': [3, 1, 10]
        }
        self.df = pd.DataFrame(self.sample_data)
    
    def test_calculate_required_quantity_simple_case(self):
        """単純な階層構造での必要手配個数計算テスト"""
        calculator = BOMCalculator(self.df)
        result_df = calculator.calculate_required_quantities()
        
        # 期待値：a=3, b=3*1=3, c=3*1*10=30
        expected_quantities = [3, 3, 30]
        
        self.assertEqual(list(result_df['required_quantity']), expected_quantities)
    
    def test_calculate_required_quantity_with_formula(self):
        """計算式が正しく追加されることをテスト"""
        calculator = BOMCalculator(self.df)
        result_df = calculator.calculate_required_quantities()
        
        # 期待される計算式
        expected_formulas = [
            '3',
            '3 * 1',
            '3 * 1 * 10'
        ]
        
        self.assertEqual(list(result_df['formula']), expected_formulas)
    
    def test_complex_hierarchy(self):
        """複雑な階層構造での計算テスト"""
        complex_data = {
            'index': ['x', 'x___y', 'x___z', 'x__y__w', 'x__z__v'],
            'quantity_per_item': [2, 3, 5, 4, 7]
        }
        df_complex = pd.DataFrame(complex_data)
        
        calculator = BOMCalculator(df_complex)
        result_df = calculator.calculate_required_quantities()
        
        # 期待値：x=2, y=2*3=6, z=2*5=10, w=2*3*4=24, v=2*5*7=70
        expected_quantities = [2, 6, 10, 24, 70]
        
        self.assertEqual(list(result_df['required_quantity']), expected_quantities)
    
    def test_empty_dataframe(self):
        """空のDataFrameに対するテスト"""
        empty_df = pd.DataFrame({'index': [], 'quantity_per_item': []})
        calculator = BOMCalculator(empty_df)
        result_df = calculator.calculate_required_quantities()
        
        self.assertEqual(len(result_df), 0)
    
    def test_single_item(self):
        """単一アイテムのテスト"""
        single_data = {
            'index': ['root'],
            'quantity_per_item': [5]
        }
        df_single = pd.DataFrame(single_data)
        
        calculator = BOMCalculator(df_single)
        result_df = calculator.calculate_required_quantities()
        
        self.assertEqual(result_df['required_quantity'].iloc[0], 5)
        self.assertEqual(result_df['formula'].iloc[0], '5')


if __name__ == '__main__':
    unittest.main()