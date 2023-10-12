package com.example.foodlist

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.recyclerview.widget.GridLayoutManager
import com.example.foodlist.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    // bindingの変数宣言
    private lateinit var binding : ActivityMainBinding

    // 食べ物リストの定義
    private val foods = listOf(
        Food("apple","果物",R.drawable.apple),
        Food("orange","果物",R.drawable.orange),
        Food("Kiwi","果物",R.drawable.kiwi),
        Food("mango","果物",R.drawable.mango),
        Food("avocado","果物",R.drawable.avocado),
        Food("banana","果物",R.drawable.banana),
        Food("watermelon","果物",R.drawable.watermelon),
        )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // bindingのインスタンス生産
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root) // bindingの省略版
        // recyclerViewの表示形式の設定
        binding.rvFood.layoutManager = GridLayoutManager(this,2)

        // アダプターの定義
        val adapter = FoodAdapter(foods)
        binding.rvFood.adapter = adapter

        // 為適配器中的項目設置點擊監聽器
        adapter.setOnItemClickListener(object : FoodAdapter.OnItemClickListener {
            override fun onItemClick(food: Food) {
                Toast.makeText(this@MainActivity, "選択された食べ物： ${food.name}", Toast.LENGTH_SHORT).show()
            }
        })
    }
}