package com.example.fragmentmenulist

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.bumptech.glide.Glide
import com.example.fragmentmenulist.databinding.FragmentSecondBinding
import com.example.fragmentmenulist.model.Menu


class SecondFragment : Fragment() {
    // set layout page
    private lateinit var binding: FragmentSecondBinding

    override fun onCreateView( inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        binding = FragmentSecondBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        // argumentsでFragmentに渡されたメニューデータを取得し、それを利用してUIを更新する。
        parentFragmentManager.setFragmentResultListener(FirstFragment.REQUEST_PROFILE_DETAIL, this) { _, bundle ->
            val selectedProfile: Menu = bundle.getParcelable(FirstFragment.SELECTED_PROFILE)!!
            selectedProfile.let {
                binding.tvName.text = it.pname
                binding.tvDetail.text = selectedProfile.detail

                // send photo to next page
                Glide.with(binding.root.context)
                    .load(selectedProfile.image_url)
                    .into(binding.ivProfile)
            }
        }
    }
}