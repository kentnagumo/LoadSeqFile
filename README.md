# LoadSeqFile
seqファイルの読み込み用モジュール
https://github.com/LJMUAstroecology/flirpy/tree/master/flirpy のコードを改編

## 依存環境
### Windows 10
exiftool 12.03
https://exiftool.org/ からダウンロード

### Ubuntu 18.04

未検証

## 使い方

下記コードを実行すると，tempフォルダに温度値が保存されているpklファイルが出力される．

```python
import LoadSeqFile.io.seq as load_seq

# 入力ファイル（リストでも可能）
seq_file = '../data/20200803_172705.seq'
# 出力先のフォルダ
output_dir = '../data'

# メイン処理
seq_splitter = load_seq.splitter(output_folder=output_dir, width=640, height=480)
seq_splitter.load_temp(seq_file)
```




## バージョン履歴

| バージョン | 改定内容 |
| ---------- | -------- |
| 1.0.0      | 初版 画像が1枚毎にpklファイルで出力される     |

