package com.example.firebasememo

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.Toolbar
import com.example.firebasememo.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    // ActivityMainBindingは、このアクティビティで使用するレイアウトのビューバインディングです。
    // ビューバインディングは、レイアウトXMLのビューに直接アクセスできるようにする機能です。
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // アプリのツールバーを設定します。
        val toolbar: Toolbar = binding.appToolbar
        setSupportActionBar(toolbar)

        val myIntent = intent
        val user = myIntent.getStringExtra("userName")
        val email = myIntent.getStringExtra("email")


        binding.button2.setOnClickListener {
                val nextIntent = Intent(this, UserActivity::class.java)
                nextIntent.putExtra("userName", user)
                nextIntent.putExtra("email", email)
                startActivity(nextIntent)
        }
    }
}
