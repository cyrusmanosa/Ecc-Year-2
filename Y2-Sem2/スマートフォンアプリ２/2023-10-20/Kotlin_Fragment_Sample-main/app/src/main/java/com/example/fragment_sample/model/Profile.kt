package com.example.fragment_sample.model

import android.os.Parcelable
import kotlinx.parcelize.Parcelize

@Parcelize
data class Profile(
    val name: String,
    val age: Int,
    val detail:String,
    val imgResID: Int
) : Parcelable

