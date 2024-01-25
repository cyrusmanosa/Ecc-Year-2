package com.example.firebasememo

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.firebasememo.databinding.ActivityUserBinding
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.storage.FirebaseStorage

class UserActivity : AppCompatActivity() {
    private lateinit  var binding: ActivityUserBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityUserBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // 前画面からユーザ情報を受け取る
        val myIntent = intent ;
        val user = myIntent.getStringExtra("userName")
        val email = myIntent.getStringExtra("email")
        binding.tvUser.text = user
        binding.tvEmail.text = email

        binding.button3.setOnClickListener {
            FirebaseAuth.getInstance().signOut()
            val intent = Intent(this, LoginActivity::class.java)
            intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP or Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK)
            startActivity(intent)
            finish()
        }

        binding.button4.setOnClickListener {
            val user = FirebaseAuth.getInstance().currentUser
            user?.delete()
                ?.addOnCompleteListener { task ->
                    if (task.isSuccessful) {
                        FirebaseDatabase.getInstance().reference.child("users").child(user.uid).removeValue()
                        FirebaseFirestore.getInstance().collection("users").document(user.uid).delete()
                        FirebaseStorage.getInstance().getReference("user_images/${user.uid}").delete()

                        Toast.makeText(applicationContext, "ユーザーを削除されました", Toast.LENGTH_SHORT).show()
                        finish()
                        val intent = Intent(this, LoginActivity::class.java)
                        startActivity(intent)
                    } else {
                        Toast.makeText(applicationContext, "失敗した", Toast.LENGTH_SHORT).show()
                    }
                }
        }

    }
}