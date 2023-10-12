<?php
header('Content-Type: application/json; charset=utf-8');
$host = 'localhost';
$db   = 'DB名';          // ダミー
$user = 'USER名';        // ダミー
$pass = 'PASSWORD';     // ダミー
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

// クエリパラメータの取得
$category = $_GET['category'] ?? null;

try {
    $pdo = new PDO($dsn, $user, $pass, $options);

    if ($category) {
        // プリペアドステートメントを使用してSQLインジェクションを防ぐ
        $stmt = $pdo->prepare('SELECT * FROM PRODUCT WHERE CATEGORY = :category');
        $stmt->bindParam(':category', $category, PDO::PARAM_STR);
        $stmt->execute();
    } else {
        $stmt = $pdo->query('SELECT * FROM PRODUCT');
    }

    $products = $stmt->fetchAll();

    echo json_encode($products, JSON_UNESCAPED_UNICODE);

} catch (\PDOException $e) {
    // ユーザーにはジェネリックなメッセージを表示し、詳細はログに保存
    error_log($e->getMessage());  // エラーメッセージをログに記録
    echo json_encode(['error' => 'An error occurred.'], JSON_UNESCAPED_UNICODE);
}
?>