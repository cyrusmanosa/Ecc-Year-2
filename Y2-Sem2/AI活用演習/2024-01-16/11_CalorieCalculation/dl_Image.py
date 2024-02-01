import flickrapi  # FlickrAPIを使って写真をダウンロードするためのモジュール
import os         # ディレクトリを作るためのモジュール
import time       # スリープ時間を設定するためのモジュール
from urllib.request import urlretrieve  # 画像をダウンロードするためのモジュール

# FlickrAPIの認証情報（これによりFlickrのAPIを利用できます）



# 画像をダウンロードする関数
def download_images(keyword, folder_name):
    # 保存先のディレクトリを作成
    save_directory = f"./image/{folder_name}"
    os.makedirs(save_directory, exist_ok=True)

    # FlickrAPIに接続
    
    # 指定したキーワードでFlickrから写真を検索します


    # 検索した写真の情報を取得
    

    # 取得した写真を1枚ずつダウンロードします



# メインの処理
if __name__ == '__main__':
    print("ダウンロード処理")
    # マグロ寿司の写真をダウンロード
    
    # サラダの写真をダウンロード
    
