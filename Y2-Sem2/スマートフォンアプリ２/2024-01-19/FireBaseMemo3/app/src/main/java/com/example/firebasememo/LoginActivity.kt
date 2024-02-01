package com.example.firebasememo

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import com.example.firebasememo.databinding.ActivityLoginBinding
import com.firebase.ui.auth.AuthUI
import com.firebase.ui.auth.FirebaseAuthUIActivityResultContract
import com.firebase.ui.auth.data.model.FirebaseAuthUIAuthenticationResult
import com.google.firebase.auth.FirebaseAuth

class LoginActivity : AppCompatActivity() {
    // binding
    private lateinit var binding:ActivityLoginBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLoginBinding.inflate(layoutInflater)
        setContentView(binding.root)
        // click Login button
        binding.btLogin.setOnClickListener{
            // 認証プロバイダー設定
            val providers = arrayListOf(AuthUI.IdpConfig.GoogleBuilder().build(), AuthUI.IdpConfig.EmailBuilder().build())
            val signInIntent = AuthUI.getInstance()
                .createSignInIntentBuilder()
                .setAvailableProviders(providers)
                .setLogo(R.mipmap.ic_launcher) // UIにアイコンを表示
                .setTheme(R.style.Theme_FireBaseMemo)// テーマカラーをアプリに合わせる
                .setIsSmartLockEnabled(false) // スマートロックを無効にする
                .build()
            signInLauncher.launch(signInIntent)
        }
    }
    private val signInLauncher = registerForActivityResult(FirebaseAuthUIActivityResultContract()) { res -> this.onSignInResult(res) }
    private fun onSignInResult(result: FirebaseAuthUIAuthenticationResult) {
        if (result.resultCode == RESULT_OK) {
            // 認証ユーザ情報の取得
            val user = FirebaseAuth.getInstance().currentUser
            // 認証出来ていれば次の画面遷移する
            user?.let {
                val nextIntent = Intent(this, UserActivity::class.java)
                nextIntent.putExtra("userName", it.displayName)
                nextIntent.putExtra("email", it.email)
                startActivity(nextIntent)
            }
        } else {
            val response = result.idpResponse
            if(response == null){
                Toast.makeText(applicationContext,
                    "認証がキャンセルされました",
                    Toast.LENGTH_SHORT).show()
            }else{
                response.error?.let{ Log.e("err",it.toString()) }
            }
        }
    }

}