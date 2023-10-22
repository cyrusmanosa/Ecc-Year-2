package com.example.fragment_sample

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.bumptech.glide.Glide
import com.example.fragmentmenulist.FirstFragment
import com.example.fragmentmenulist.databinding.FragmentSecondBinding
import com.example.fragmentmenulist.model.Menu


class SecondFragment : Fragment() {
    private lateinit var binding: FragmentSecondBinding
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentSecondBinding.inflate(inflater, container, false)
        return binding.root
    }

    // ビューが作成された直後に呼ばれるメソッド。
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        // argumentsでFragmentに渡されたメニューデータを取得し、それを利用してUIを更新する。
        parentFragmentManager.setFragmentResultListener(FirstFragment.REQUEST_PROFILE_DETAIL, this) { _, bundle ->

            val selectedProfile: Menu = bundle.getParcelable("SELECTED_PROFILE")!!
            binding.tvName.text = selectedProfile.name
            binding.tvCategory.text = selectedProfile.category
            binding.tvDetail.text = selectedProfile.detail.toString()

            Glide.with(binding.root.context)
                .load(selectedProfile.imgResID)
                .into(binding.ivProfile)
        }
    }
}