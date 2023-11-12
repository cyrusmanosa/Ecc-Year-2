package com.example.fragmentmenulist

import com.example.fragmentmenulist.model.Menu
import retrofit2.http.GET
import retrofit2.Call
//
//interface MenuAPI {
//    @GET("ecc/yishida/pizzaDB.php")
//fun fetchMenu(): Call<Menu>
//}

interface MenuAPI {
    @GET("ecc/yishida/pizzaDB.php")
    fun fetchMenu(): Call<List<Menu>> // Change the return type to List<Menu>
}