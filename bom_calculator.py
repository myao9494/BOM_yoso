import pandas as pd
from typing import List, Dict, Tuple


class BOMCalculator:
    """BOM（Bill of Materials）階層構造から必要手配個数を計算するクラス"""
    
    def __init__(self, df: pd.DataFrame):
        """
        初期化
        
        Args:
            df: 'index'と'quantity_per_item'列を持つDataFrame
        """
        self.df = df.copy()
    
    def calculate_required_quantities(self) -> pd.DataFrame:
        """
        BOM階層構造から各部品の必要手配個数を計算
        
        Returns:
            必要手配個数と計算式を追加したDataFrame
        """
        if self.df.empty:
            return pd.DataFrame({'index': [], 'quantity_per_item': [], 'formula': [], 'required_quantity': []})
        
        result_df = self.df.copy()
        formulas = []
        required_quantities = []
        
        for i, row in result_df.iterrows():
            item_index = row['index']
            quantity = row['quantity_per_item']
            
            # 階層レベルを'__'の数で計算
            level = self._get_hierarchy_level(item_index)
            
            # 親階層の個数を取得
            parent_quantities = self._get_parent_quantities(item_index, result_df)
            
            # 計算式を構築
            formula_parts = parent_quantities + [str(quantity)]
            formula = ' * '.join(formula_parts)
            
            # 必要手配個数を計算
            required_quantity = 1
            for parent_qty in parent_quantities:
                required_quantity *= int(parent_qty)
            required_quantity *= quantity
            
            formulas.append(formula)
            required_quantities.append(required_quantity)
        
        result_df['formula'] = formulas
        result_df['required_quantity'] = required_quantities
        
        return result_df
    
    def _get_hierarchy_level(self, item_index: str) -> int:
        """階層レベルを取得"""
        return item_index.count('__')
    
    def _get_parent_quantities(self, item_index: str, df: pd.DataFrame) -> List[str]:
        """親階層の個数のリストを取得"""
        parent_quantities = []
        
        # 全ての可能な親パスを収集
        parent_paths = []
        
        # 階層レベルを取得
        level = self._get_hierarchy_level(item_index)
        
        if level == 0:
            # ルートレベルの場合、親はなし
            return []
        
        # 階層を遡って親を検索
        current_item = item_index
        
        # レベル2: a__b__c の場合
        if level == 2:
            # a__b__c の親は a___b
            parts = current_item.split('__')
            if len(parts) == 3:
                parent_path = parts[0] + '___' + parts[1]
                parent_paths.append(parent_path)
                
                # a___b の親は a
                grandparent_path = parts[0]
                parent_paths.append(grandparent_path)
        
        # レベル1: a___b の場合
        elif level == 1:
            # a___b の親は a
            parts = current_item.split('___')
            if len(parts) == 2:
                parent_path = parts[0]
                parent_paths.append(parent_path)
        
        # 親パスの順序を逆にしてルートから順に並べる
        parent_paths.reverse()
        
        # 各親パスの数量を取得
        for parent_path in parent_paths:
            parent_record = df[df['index'] == parent_path]
            if not parent_record.empty:
                parent_quantities.append(str(parent_record.iloc[0]['quantity_per_item']))
        
        return parent_quantities