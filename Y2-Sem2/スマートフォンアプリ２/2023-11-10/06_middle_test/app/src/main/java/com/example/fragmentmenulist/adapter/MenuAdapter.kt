package com.example.fragmentmenulist.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.fragmentmenulist.databinding.ProfileItemBinding
import com.example.fragmentmenulist.model.Menu

class MenuAdapter(
    private val MfileList:List<Menu>,
    private val onMenuClicked:((Menu) -> Unit)) :
    RecyclerView.Adapter<MenuAdapter.MenuViewHolder>(){
    inner class MenuViewHolder(private val binding: ProfileItemBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(plofile:Menu){
            binding.tvName.text = plofile.pname
            binding.tvCategory.text = "￥"+plofile.price.toString()
            Glide.with(binding.root.context)
                .load(plofile.image_url)
                .into(binding.ivProfile)

            // ハンズオン演習；クリックリスナーを実装
            binding.root.setOnClickListener{
                // 実行する処理
                onMenuClicked(plofile)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MenuViewHolder {
        val binding = ProfileItemBinding.inflate(LayoutInflater.from(parent.context),parent,false)
        return MenuViewHolder(binding)
    }

    override fun getItemCount(): Int {
        return MfileList.size
    }

    override fun onBindViewHolder(holder: MenuViewHolder, position: Int) {
        val plofile : Menu = MfileList[position]
        holder.bind(plofile)
    }
}
