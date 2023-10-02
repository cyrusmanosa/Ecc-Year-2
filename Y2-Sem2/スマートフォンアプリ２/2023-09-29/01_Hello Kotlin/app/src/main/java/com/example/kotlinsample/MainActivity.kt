package com.example.kotlinsample

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.PersistableBundle
import android.util.Log

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Log.d("test","call onCreate()")
    }

    override fun onStart() {
        super.onStart()
        Log.d("test","call onStart")
    }

    override fun onResume() {
        super.onResume()
        Log.d("test","call onResume")
    }

    override fun onPause() {
        super.onPause()
        Log.d("test","call onPause")
    }

    override fun onStop() {
        super.onStop()
        Log.d("test","call onStop")
    }

    override fun onRestart() {
        super.onRestart()
        Log.d("test","call onRestart")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d("test","call onDestroy")
    }
}
