# LoadSeqFile
seqファイルの読み込み用モジュール
https://github.com/LJMUAstroecology/flirpy/tree/master/flirpy のコードを改編

## 依存環境
### Windows 10
exiftool 12.03を
https://exiftool.org/ からダウンロード
※binディレクトリにある場合はインストール不要

必要なパッケージは以下の通りである．
```bash
conda install -c conda-forge imagecodecs
conda install -c conda-forge imagecodecs-lite
pip install opencv-python
```

### Ubuntu 18.04

必要なパッケージは以下の通りである．
```bash
conda install -c conda-forge imagecodecs
conda install -c conda-forge imagecodecs-lite
pip install opencv-python
sudo apt install libimage-exiftool-perl
```

## 使い方

下記コードを実行すると，tempフォルダに温度値が保存されているpklファイルが出力される．export_meta=Trueにすると，rawフォルダにmetaデータが出力されるが，処理時間がかなり長くなる（デフォルトはFalse）．熱画像の最初行にNanが出力される場合はheader_lengthに数字を入力して解決する場合がある．

```python
import LoadSeqFile.io.seq as load_seq

# 入力ファイル（リストでも可能）
seq_file = '../data/20200803_172705.seq'
# 出力先のフォルダ
output_dir = '../data'

# メイン処理
# out_temp: 室温, out_rh: 湿度, distance: 対象物までの距離
seq_splitter = load_seq.splitter(output_folder=output_dir, width=640, height=480, header_length=None, export_meta=False, out_temp=None, out_rh=None, distance=None)

# 温度値変換の実行
seq_splitter.load_temp(seq_file)
```




## バージョン履歴

| バージョン | 改定内容 |
| ---------- | -------- |
| 1.0.0      | 初版 画像が1枚毎にpklファイルで出力される     |
| 1.0.1      | Linuxでエラーが出る現象の修正     |
| 1.0.2      | A35に対応，画像の位置ずれの修正     |
| 1.0.3      | metaデータの出力を追加     |
| 1.0.4 | 画像が左右に分割される問題の解決用にheader_lengthを追加 |
| 1.0.5 | 温度、湿度、距離のパラメータを追加 |
