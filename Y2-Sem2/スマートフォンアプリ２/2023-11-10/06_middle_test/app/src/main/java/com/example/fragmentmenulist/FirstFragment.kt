package com.example.fragmentmenulist

import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.os.bundleOf
import androidx.recyclerview.widget.GridLayoutManager
import com.example.fragmentmenulist.adapter.MenuAdapter
import com.example.fragmentmenulist.databinding.FragmentFirstBinding
import com.example.fragmentmenulist.model.Menu
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class FirstFragment : Fragment() {
    private lateinit var binding: FragmentFirstBinding
    private val menuList = mutableListOf<Menu>()

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        binding = FragmentFirstBinding.inflate(inflater, container, false)
        return binding.root
    }

    // ビューが作成された直後に呼ばれるメソッド
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        fetchData()

        // ハンズオン演習：クリック時処理とfragmentの画面遷移処理を実装
        val adapter = MenuAdapter(menuList) {
            // onProfileClicked(Profile)の実際に行う処理を記述
                selectedProfile ->
            // データ
            parentFragmentManager.setFragmentResult(
                REQUEST_PROFILE_DETAIL,
                bundleOf("SELECTED_PROFILE" to selectedProfile)
            )
            // 次のFragmentへ遷移
            parentFragmentManager.beginTransaction()
                .replace(R.id.fragmentContainerView, SecondFragment()).addToBackStack(null).commit()
        }

        binding.rvProfilelist.adapter = adapter
        binding.rvProfilelist.layoutManager = GridLayoutManager(context, 2)
    }


    private fun fetchData() {
        menuList.clear()
        val retrofit = Retrofit.Builder()
            .baseUrl("https://click.ecc.ac.jp/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        val api = retrofit.create(MenuAPI::class.java)
        api.fetchMenu().enqueue(object : Callback<List<Menu>> { // Change the callback type to List<Menu>
            override fun onResponse(call: Call<List<Menu>>, response: Response<List<Menu>>) {
                if (response.isSuccessful) {
                    val menus = response.body()
                    if (menus != null) {
                        menuList.addAll(menus)
                        binding.rvProfilelist.adapter?.notifyDataSetChanged()
                    }
                } else { Log.e("API_ERROR", "Failed to fetch Menu data: ${response.code()}") }
            }
            override fun onFailure(call: Call<List<Menu>>, t: Throwable) {
                Log.e("API_ERROR", "Failed to fetch Menu data", t)
            }
        })
    }
    companion object {
        const val REQUEST_PROFILE_DETAIL = "REQUEST_PROFILE_DETAIL"
        const val SELECTED_PROFILE = "SELECTED_PROFILE"
    }
}