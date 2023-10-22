package com.example.fragmentmenu

import android.content.Context
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.fragmentmenu.databinding.ActivityMainBinding
import com.example.fragmentmenu.databinding.FragmentMenuBinding
import com.example.fragmentmenu.databinding.FragmentTopBinding

class TopFragment : Fragment() {

    override fun onAttach(context: Context) {
        super.onAttach(context)
        Log.d("TopFragment","call onAttach()")
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d("TopFragment","call onCreate()")
    }



    // Fragmentに関連付けられたViewを作成する際に呼ばれる
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        Log.d("TopFragment","call onCreateView()")
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_top, container, false)
    }




    // ActivityでいうonCreateの処理（初期化など）を使用するメソッド
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        Log.d("TopFragment","call onViewCreated()")
    }
    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        Log.d("TopFragment","call onActivityCreated()")
    }
    override fun onStart() {
        super.onStart()
        Log.d("TopFragment","call onCreate()")
    }
    override fun onResume() {
        super.onResume()
        Log.d("TopFragment","call onResume()")
    }
    override fun onPause() {
        super.onPause()
        Log.d("TopFragment","call onPause()")
    }
    override fun onStop() {
        super.onStop()
        Log.d("TopFragment","call onStop()")
    }
    override fun onDestroyView() {
        super.onDestroyView()
        Log.d("TopFragment","call onDestroyView()")

    }
    override fun onDestroy() {
        super.onDestroy()
        Log.d("TopFragment","call onDestroy()")
    }
    override fun onDetach() {
        super.onDetach()
        Log.d("TopFragment","call onDetach()")
    }

    companion object {
        // Singletonで作成するテータ
        @JvmStatic
        fun newInstance() = TopFragment()
    }
}