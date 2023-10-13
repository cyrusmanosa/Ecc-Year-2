package com.example.fragmentmenu

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.fragmentmenu.databinding.FragmentMenuBinding

@Suppress("DEPRECATION")
class MenuFragment : Fragment() {
    private lateinit var binding: FragmentMenuBinding

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        binding = FragmentMenuBinding.inflate(layoutInflater)
//         Inflate the layout for this fragment
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.btnNext.setOnClickListener {
            if (binding.ivMenu.drawable.constantState == resources.getDrawable(R.drawable.omeletrice).constantState) {
                binding.ivMenu.setImageResource(R.drawable.hamburg)
            }else{
                binding.ivMenu.setImageResource(R.drawable.omeletrice)
            }
        }
    }

    companion object {
        @JvmStatic
        fun newInstance() = MenuFragment()
    }
}

