package com.example.fragmentmenulist

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.os.bundleOf
import androidx.recyclerview.widget.GridLayoutManager
import com.example.fragment_sample.SecondFragment
import com.example.fragmentmenulist.adapter.MenuAdapter
import com.example.fragmentmenulist.databinding.FragmentFirstBinding
import com.example.fragmentmenulist.model.Menu

class FirstFragment : Fragment() {
    private lateinit var binding:FragmentFirstBinding
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentFirstBinding.inflate(inflater, container, false)
        return binding.root
    }

    // ビューが作成された直後に呼ばれるメソッド
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // 表示するプロフィールリスト
        val profileList = listOf(
//            Profile(getString(R.string.text_monk_name),getString(R.string.text_monk_age).toInt(),R.string.text_monk_detail.toString(),R.drawable.monk),
            Menu("ドリア","メイン",getString(R.string.text_doria_detail),R.drawable.doria),
            Menu("チーズドリア","メイン",getString(R.string.text_cheese_doria_doria_detail),R.drawable.guratan),
            Menu("ガーデンサラダ","サラダ",getString(R.string.text_garden_salad_detail),R.drawable.onionzupa),
            Menu("ペコリーノチーズの温サラダ","サラダ",getString(R.string.text_cheese_salad_detail),R.drawable.sarada),
            Menu("コーンスープ","スープ",getString(R.string.text_corn_soup_detail),R.drawable.cornsoup),
            Menu("ハンバーグ","メイン",getString(R.string.text_hamburg_detail),R.drawable.hamburg),
            Menu("エビグラタン","メイン",getString(R.string.text_shrimp_gratin_detail),R.drawable.omeletrice),
            Menu("マルゲリータピザ","メイン",getString(R.string.text_margherita_pizza_detail),R.drawable.pizza),
        )

        // ハンズオン演習：クリック時処理とfragmentの画面遷移処理を実装
        val adapter = MenuAdapter(profileList){
            // onProfileClicked(Profile)の実際に行う処理を記述
            selectedProfile ->
                // データ
                parentFragmentManager.setFragmentResult(REQUEST_PROFILE_DETAIL, bundleOf("SELECTED_PROFILE" to selectedProfile))
                // 次のFragmentへ遷移
                parentFragmentManager.beginTransaction().replace(R.id.fragmentContainerView,SecondFragment()).addToBackStack(null).commit()
        }

        binding.rvProfilelist.adapter = adapter
        binding.rvProfilelist.layoutManager = GridLayoutManager(context,2)
    }
    companion object{
        const val REQUEST_PROFILE_DETAIL = "REQUEST_PROFILE_DETAIL"
    }
}