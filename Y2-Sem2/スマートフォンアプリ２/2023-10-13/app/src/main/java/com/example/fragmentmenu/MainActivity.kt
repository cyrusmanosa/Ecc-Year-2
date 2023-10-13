package com.example.fragmentmenu

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.fragmentmenu.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnTop.setOnClickListener{
            // ボタンクリック時の処理
            supportFragmentManager.beginTransaction().replace(R.id.fragmentContainerView,TopFragment.newInstance()).commit()
        }

        binding.btnMenu.setOnClickListener {
            supportFragmentManager.beginTransaction().replace(R.id.fragmentContainerView,MenuFragment.newInstance()).commit()
        }
    }
}