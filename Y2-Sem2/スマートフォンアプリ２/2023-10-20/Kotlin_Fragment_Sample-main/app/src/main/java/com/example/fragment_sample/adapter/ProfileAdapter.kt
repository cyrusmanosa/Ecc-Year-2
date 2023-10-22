package com.example.fragment_sample.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.fragment_sample.databinding.ProfileItemBinding
import com.example.fragment_sample.model.Profile

class ProfileAdapter(private val plofileList:List<Profile>, private val onProfileClicked:((Profile) -> Unit)) : RecyclerView.Adapter<ProfileAdapter.ProfileViewHolder>(){

    inner class ProfileViewHolder(private val binding:ProfileItemBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(plofile:Profile){
            binding.tvName.text = plofile.name
            binding.tvAge.text = plofile.age.toString()
            Glide.with(binding.root.context)
                .load(plofile.imgResID)
                .into(binding.ivProfile)

            // ハンズオン演習；クリックリスナーを実装
            binding.root.setOnClickListener{
                // 実行する処理
                onProfileClicked(plofile)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ProfileViewHolder {
        val binding = ProfileItemBinding.inflate(LayoutInflater.from(parent.context),parent,false)
        return ProfileViewHolder(binding)
    }

    override fun getItemCount(): Int {
        return plofileList.size
    }

    override fun onBindViewHolder(holder: ProfileViewHolder, position: Int) {
        val plofile : Profile = plofileList[position]
        holder.bind(plofile)
    }
}
