package com.example.fragmentmenulist.model

import android.os.Parcelable
import kotlinx.parcelize.Parcelize
import retrofit2.http.Url

@Parcelize
data class Menu(
    val pname: String,
    val category:String,
    val price: Int,
    val image_url: String,
    val detail: String,
) : Parcelable
