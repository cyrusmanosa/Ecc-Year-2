<?php
//
// gourmet.php
// グルメサーチAPI
//
require_once __DIR__ . "/config.php";

// ホットペッパーAPI グルメサーチ検索クエリ
$searchItems = [
    "key"    => API_KEY,
    "format" => API_RESPONSE_FORMAT,
];
foreach( $_GET as $key => $param ) { $searchItems[ $key ] = $param; }

// 検索クエリの項目を作成
$searchParams = [];
foreach( $searchItems as $key => $item ) {
    $searchParams[] = "{$key}={$item}";
}

// 検索クエリのGETパラメーターを作成
$searchParamString = implode( "&", $searchParams );

// グルメサーチAPIのURLを作成
$searchURL = API_GOURMET_URL . "?{$searchParamString}";

// クロスオリジンに対応したAPIからのデータを出力
// クロスオリジン: すべて許可
// ファイルの種類: JSONファイル
header( "Access-Control-Allow-Origin: *" );
header( "Content-Type: application/json" );
print file_get_contents( $searchURL );
