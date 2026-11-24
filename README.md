# weakness
# QR → カメラ + 半透明スクロールテキスト

QRコードを読み取るとページが開き、カメラ映像の上に半透明でスクロールできる文章が重なります。

## ファイル
- `index.html` … ページ本体(1ファイル完結)。文章は `<div id="text">` の中身を書き換える
- `make_qr.py` … URLからQR画像(`qr.png`)を作り、読み取りテストまで行う

## 公開手順(GitHub Pages)
1. この2ファイルをリポジトリのルートに置いて push
2. GitHub のリポジトリ → Settings → Pages
3. Source を「Deploy from a branch」、Branch を `main` / `/ (root)` にして Save
4. 数分待つと `https://ユーザー名.github.io/リポジトリ名/` で公開される(HTTPSは自動)

## QR作成
```
pip install opencv-python-headless
python make_qr.py https://ユーザー名.github.io/リポジトリ名/
```
`qr.png` ができます。印刷するときは白地に黒のまま、周囲の余白を削らないでください。

## 動作確認チェックリスト
- [ ] PCのブラウザでURLを開き、ページが表示される
- [ ] iPhone の標準カメラで `qr.png` を読み、Safari でページが開く
- [ ] カメラの許可ダイアログが出て、許可すると背景にカメラが映る
- [ ] 文章のパネルが指でスクロールできる
- [ ] 許可を拒否しても、文章だけは読める(「カメラを再試行」が出る)
- [ ] Android の標準カメラ(またはGoogleレンズ)+ Chrome でも同じ
- [ ] 印刷するなら、実際の印刷サイズで離れた距離から読めるか
