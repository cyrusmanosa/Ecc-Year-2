import flickrapi  # FlickrAPIを使って写真をダウンロードするためのモジュール
import os         # ディレクトリを作るためのモジュール
import time       # スリープ時間を設定するためのモジュール
from urllib.request import urlretrieve  # 画像をダウンロードするためのモジュール

# FlickrAPIの認証情報（これによりFlickrのAPIを利用できます）
key = "53c16924d4cb185d03cf5a9bec45f172"
secret = "3db9a43ad180f2e0"


# 画像をダウンロードする関数
def download_images(keyword, folder_name):
    # 保存先のディレクトリを作成
    save_directory = f"./image/{folder_name}"
    os.makedirs(save_directory, exist_ok=True)

    # FlickrAPIに接続に接続しインスタンスを取得
    flickr = flickrapi.FlickrAPI(key, secret, format='parsed-json')
    
    # 指定したキーワードでFlickrから写真を検索
    response = flickr.photos.search(
            text= keyword,
            per_page=100,  # ページあたりの取得写真数
            media='photos',  # メディアのタイプ（ここでは'photos' = 写真）
            sort='relevance',  # 検索結果の並び順（ここでは'relevance' = 関連性順）
            safe_search=1,  # セーフサーチ（1 = セーフな内容のみ）
            extras='url_q, license'  # 取得する追加情報（url_q = 中サイズ画像のURL, license = ライセンス情報）
        )


    # 検索した写真の情報を取得
    photos = response['photos']['photo']
    

    # 取得した写真を1枚ずつダウンロードします
    for i, photo in enumerate(photos):
        image_url = photo['url_q']  # 画像のURL
        file_path = f"{save_directory}/{photo['id']}.jpg"  # 保存先のファイルパス

        # ファイルが既に存在しない場合のみダウンロードします
        if not os.path.exists(file_path):
            print(f"{i + 1}: downloading {image_url}")
            urlretrieve(image_url, file_path)  # 画像をダウンロードします



# メインの処理
if __name__ == '__main__':
    print("ダウンロード処理")
    # マグロ寿司の写真をダウンロード
    download_images('寿司', 'sushi')
    # サラダの写真をダウンロード
    download_images('サラダ', 'salad')
    # とんかつの写真をダウンロード
    download_images('とんかつ', 'pork')
    
