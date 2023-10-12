package com.example.foodlist

// Foodデータクラスを定義します。
// このクラスは食べ物の情報（名前、カテゴリ、画像リソース）を持っています。
data class Food(
    val name: String,     // 食べ物の名前
    val category: String,  // 食べ物のカテゴリ（例：果物、お菓子など）
    val imgResID: Int        // 画像のリソースID
)
