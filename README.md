# BOM階層構造必要手配個数計算システム

製造業のBOM（Bill of Materials）階層構造から、各部品の必要手配個数を計算するPythonプログラムです。

## 概要

このシステムは、製造業で使用されるBOMの階層構造を解析し、各部品の必要手配個数を自動計算します。
階層構造は `a`, `a___b`, `a__b__c` のような形式で表現され、各階層の個数を掛け合わせて最終的な必要個数を求めます。

### 主な機能

- BOM階層構造の解析
- 必要手配個数の自動計算
- 計算式の生成
- CSVファイル入出力対応
- 複数製品の一括処理

## 階層構造の表現

```
a                    (ルート製品: 3個)
├── a___b           (aの子部品b: 1個/製品)
│   └── a__b__c     (bの子部品c: 10個/b)
```

この場合、cの必要手配個数は `3 × 1 × 10 = 30個` となります。

## インストール

### 必要な環境

- Python 3.7以上
- pandas

### 依存関係のインストール

```bash
pip install pandas
```

## ファイル構成

```
BOM/
├── README.md                   # このファイル
├── 仕様.md                     # システム仕様書
├── bom_calculator.py           # BOM計算メインクラス
├── test_bom_calculator.py      # テストファイル
├── example_usage.py            # 使用例
├── create_sample_bom.py        # サンプルデータ作成
├── sample_bom_data.csv         # サンプルBOMデータ
└── sample_bom_result.csv       # 計算結果サンプル
```

## 使用方法

### 基本的な使用例

```python
import pandas as pd
from bom_calculator import BOMCalculator

# BOMデータの準備
bom_data = {
    'index': ['a', 'a___b', 'a__b__c'],
    'quantity_per_item': [3, 1, 10]
}
df = pd.DataFrame(bom_data)

# 計算実行
calculator = BOMCalculator(df)
result_df = calculator.calculate_required_quantities()

print(result_df)
```

### CSVファイルからの読み込み

```python
import pandas as pd
from bom_calculator import BOMCalculator

# CSVファイルから読み込み
df = pd.read_csv('sample_bom_data.csv')

# 計算実行
calculator = BOMCalculator(df)
result_df = calculator.calculate_required_quantities()

# 結果をCSVで保存
result_df.to_csv('result.csv', index=False)
```

### サンプルデータの作成と実行

```bash
# サンプルデータの作成と計算
python create_sample_bom.py

# 使用例の実行
python example_usage.py
```

## 出力例

### 入力データ
```
     index  quantity_per_item
0        a                  3
1    a___b                  1
2  a__b__c                 10
```

### 計算結果
```
     index  quantity_per_item     formula  required_quantity
0        a                  3           3                  3
1    a___b                  1       3 * 1                  3
2  a__b__c                 10  3 * 1 * 10                 30
```

## テスト

テスト駆動開発（TDD）で開発されています。

```bash
# テストの実行
python -m pytest test_bom_calculator.py -v

# 特定のテストの実行
python -m pytest test_bom_calculator.py::TestBOMCalculator::test_calculate_required_quantity_simple_case -v
```

## API仕様

### BOMCalculator クラス

#### コンストラクタ
```python
BOMCalculator(df: pd.DataFrame)
```
- `df`: 'index'と'quantity_per_item'列を持つDataFrame

#### メソッド

##### calculate_required_quantities()
```python
calculate_required_quantities() -> pd.DataFrame
```
必要手配個数を計算し、結果をDataFrameで返します。

**戻り値**
- `index`: 部品インデックス
- `quantity_per_item`: 部品ごとの個数
- `formula`: 計算式
- `required_quantity`: 必要手配個数

## 階層構造の命名規則

- ルート製品: `product_name`
- 第1階層: `product_name___component_name`
- 第2階層: `product_name__component_name__part_name`
- 第3階層以降: `__` で区切りを追加

## サンプルデータ

`sample_bom_data.csv` には以下の製品が含まれています：

- **product_a**: 自動車部品（フレーム、エンジン、ホイール）
- **product_b**: 電子機器（シャーシ、モーター）
- **product_c**: 制御装置（ボディ、制御ユニット）
- **product_d**: 単純な階層構造
- **product_e**: 複雑な階層構造

## 開発

### 開発方針

- テスト駆動開発（TDD）
- 期待される入出力に基づくテストファースト
- 実装後のテスト確認

### 貢献

1. フォークしてください
2. 機能ブランチを作成してください (`git checkout -b feature/amazing-feature`)
3. 変更をコミットしてください (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュしてください (`git push origin feature/amazing-feature`)
5. プルリクエストを作成してください

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 著者

Claude Code - BOM階層構造必要手配個数計算システム

## 更新履歴

- v1.0.0: 初期リリース
  - BOM階層構造解析機能
  - 必要手配個数計算機能
  - CSV入出力対応
  - テストスイート完備