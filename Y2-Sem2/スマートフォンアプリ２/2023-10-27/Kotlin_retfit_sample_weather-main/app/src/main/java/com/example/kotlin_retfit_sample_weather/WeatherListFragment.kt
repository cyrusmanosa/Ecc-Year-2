package com.example.kotlin_retfit_sample_weather

import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.os.bundleOf
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.kotlin_retfit_sample_weather.adapter.WeatherAdapter
import com.example.kotlin_retfit_sample_weather.databinding.FragmentWeatherListBinding
import com.example.kotlin_retfit_sample_weather.model.Weather
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory


class WeatherListFragment : Fragment() {
    private lateinit var binding: FragmentWeatherListBinding
    // OpenWeatherMapのAPIアクセスに必要なキー
    private val API_KEY = "003ef1d65597b85d2ab6fa19b59383b6"
    // 対象となる日本の都市のリスト
    private val cities = listOf("Tokyo", "Osaka", "Kyoto", "Hiroshima", "Fukuoka", "Hokkaido", "Okinawa", "Aomori", "Nagano", "Tottori", "Nagoya")
    // 取得した天気情報を保存するためのリスト
    private val weatherList = mutableListOf<Weather>()

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        binding = FragmentWeatherListBinding.inflate(inflater, container, false)
        return binding.root
    }

    // このフラグメントのビューが初めて作成されたときに呼ばれる関数
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        // RecyclerViewのデザインを定義するLayoutManagerを設定
        binding.rvCitylist.layoutManager = LinearLayoutManager(context)
        // APIから天気データを取得する関数を呼び出し
        fetchData()
    }


    // OpenWeatherMap APIから天気データを取得する関数
    private fun fetchData() {
        // 既存のリストのデータをクリア
        weatherList.clear()
        val completedRequests = 0  // 成功したAPIリクエストの数をカウントする変数

        // Retrofitを使用してAPI通信を行う準備
        // Retrofitインスタンスを作成するためには、まず設定となるRetrofit.Builderクラスを使用します。
        val retrofit = Retrofit.Builder()

        // retrofitのbaseUrl() メソッドを使用して、APIのベースURLを設定します。
        // このURLは、後で定義するエンドポイントのURLの基盤となります。
        .baseUrl("https://api.openweathermap.org/")

        // APIからのレスポンスデータは通常JSON形式です。
        // このJSONデータをJavaのオブジェクトに変換するために、GsonConverterFactoryを追加します。
        .addConverterFactory(GsonConverterFactory.create()).build()

        // 各都市の天気情報をAPIから取得
        val api = retrofit.create(WeatherApi::class.java)

        for (i in cities) {
            api.fetchWeather(i, "ja", API_KEY)
                .enqueue(object : Callback<Weather> {
                    // API リクエストが成功したときの処理
                    override fun onResponse(call: Call<Weather>, response: Response<Weather>) {
                        response.body()?.let { weather ->
                            weatherList.add(weather) // 取得した天気情報をリストに追加
                            binding.rvCitylist.adapter = WeatherAdapter(weatherList) {
                                    selectedWeather ->
                                    // 次のFramentへ渡すデータを格納
                                    parentFragmentManager.setFragmentResult(
                                        REQUEST_WEATHER_DETAIL,
                                        bundleOf(SELECTED_WEATHER to selectedWeather)
                                    )
                                    // 画面遷移
                                    parentFragmentManager.beginTransaction()
                                        .replace(
                                            R.id.fragmentContainer,
                                            WeatherDetailsFragment()
                                        ) // 新しいフラグメントに切り替える
                                        .addToBackStack(null) // バックスタックに追加して、戻るボタンで前のフラグメントに戻れるようにする
                                        .commit() // 変更を確定する
                                }
                        }
                    }

                    // API リクエストが失敗したときの処理
                    override fun onFailure(call: Call<Weather>, t: Throwable) {
                        Log.e("API_ERROR", "Failed to fetch weather data", t) // エラーログを出力
                    }
                })
        }
    }

    companion object {
        val REQUEST_WEATHER_DETAIL = "REQUEST_WEATHER_DETAIL"
        val SELECTED_WEATHER = "SELECTED_WEATHER"
    }


}