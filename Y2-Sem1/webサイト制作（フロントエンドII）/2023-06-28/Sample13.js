{
  // RESAS API関連
  const APIKey = "FP93jNInkB3RkUl94NzBYKMQoZLD3eORqDSZqd6s";
  const APIEndpoint = "https://opendata.resas-portal.go.jp";
  const prefAPI = "api/v1/prefectures"; // 都道府県一覧API
  const citiesAPI = "api/v1/cities"; // 市区町村一覧API

  // Element
  const selectPref = document.querySelector("#pref");
  const selectCity = document.querySelector("#city");

  fetch(`${APIEndpoint}/${prefAPI}`, { headers: { "X-API-KEY": APIKey } })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log(data);
      const prefs = data.result;
      prefs.forEach((pref) => {
        const item = document.createElement("option");
        item.value = pref.prefCode;
        item.innerText = pref.prefName;
        selectPref.append(item);
      });
    });

  fetch(`${APIEndpoint}/${citiesAPI}`, { headers: { "X-API-KEY": APIKey } })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const cities = data.result;
      cities.forEach((city) => {
        const item = document.createElement("option");
        item.value = city.cityCode;
        item.innerText = city.cityName;
        selectCity.append(item);
      });
    });

}
