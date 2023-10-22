package com.example.fragmentmenulist.model

import android.os.Parcelable
import kotlinx.parcelize.Parcelize

@Parcelize
data class Menu(
    val name: String,
    val category: String,
    val detail:String,
    val imgResID: Int
) : Parcelable
