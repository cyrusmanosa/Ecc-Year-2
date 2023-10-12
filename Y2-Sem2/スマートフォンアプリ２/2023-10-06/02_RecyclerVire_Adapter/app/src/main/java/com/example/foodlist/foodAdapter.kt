package com.example.foodlist

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.foodlist.databinding.FoodItemBinding

class FoodAdapter(private val foods:List<Food>) : RecyclerView.Adapter<FoodAdapter.FoodViewHolder>() {
        inner class FoodViewHolder(private val binding: FoodItemBinding) :
                RecyclerView.ViewHolder(binding.root) {
                fun bind(food: Food) {
                        // レイアウトに反映させる
                        binding.foodName.text = food.name
                        binding.foodCategory.text = food.category
                        Glide.with(binding.root.context).load(food.imgResID).into(binding.foodImage)

                        binding.root.setOnClickListener{onItemClickListener?.onItemClick(food)}
                }
        }

        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): FoodViewHolder {
                val binding = FoodItemBinding.inflate(LayoutInflater.from(parent.context),parent,false)
                return FoodViewHolder(binding)
        }

        override fun getItemCount(): Int {
                return foods.size
        }

        override fun onBindViewHolder(holder: FoodViewHolder, position: Int) {
                holder.bind(foods[position])
        }



        private var onItemClickListener: OnItemClickListener? = null
        fun setOnItemClickListener(listener: OnItemClickListener) {
                onItemClickListener = listener
        }
        interface OnItemClickListener {
                fun onItemClick(food: Food)
        }
}
