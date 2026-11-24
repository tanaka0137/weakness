"""URL から QR コード画像を作り、同じ画像を読み取って内容が一致するか確認する。

使い方:
    pip install opencv-python-headless
    python make_qr.py https://ユーザー名.github.io/リポジトリ名/
"""
import sys
import cv2
import numpy as np

url = sys.argv[1] if len(sys.argv) > 1 else input("QRにするURL: ").strip()
if not url.startswith("https://"):
    sys.exit("URL は https:// で始めてください(カメラ利用にHTTPSが必須です)")

params = cv2.QRCodeEncoder_Params()
params.correction_level = cv2.QRCodeEncoder_CORRECT_LEVEL_Q  # 誤り訂正 Q(約25%)
qr = cv2.QRCodeEncoder_create(params).encode(url)

# 1セル=16px に拡大し、周囲に4セル分の白い余白(クワイエットゾーン)を付ける
cell, quiet = 16, 4
core = cv2.resize(qr, None, fx=cell, fy=cell, interpolation=cv2.INTER_NEAREST)
img = cv2.copyMakeBorder(core, quiet * cell, quiet * cell, quiet * cell, quiet * cell,
                         cv2.BORDER_CONSTANT, value=255)
cv2.imwrite("qr.png", img)
print("qr.png を作成しました")

# 読み取りテスト(画像を縮小して、スマホカメラ越しに近い状態でも読めるか確認)
detector = cv2.QRCodeDetector()
ok = True
for scale in (1.0, 0.5, 0.25):
    small = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    decoded, _, _ = detector.detectAndDecode(small)
    match = decoded == url
    ok = ok and match
    print(f"  縮尺 {scale:>4}: {'OK' if match else 'NG'} ({small.shape[1]}px)")
sys.exit(0 if ok else 1)
