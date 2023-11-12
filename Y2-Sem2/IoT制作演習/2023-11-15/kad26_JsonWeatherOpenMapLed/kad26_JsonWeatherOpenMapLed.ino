#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h> //JasonParserExampleからコピー

// 接続先のSSIDとパスワード 学内CampusIOT
const char ssid[] = "CampusIoT-WiFi";
const char passwd[] = "0b8b413f2c0fa6aa90e085e9431abbf1fa1b2bd2db0ecf4ae9ce4b2e87da770c";

const int ledPinA = 16;
const int ledPinB = 4;

void setup() {
  Serial.begin(115200);
  pinMode(ledPinA, OUTPUT);

  // WiFi接続シーケンス
  Serial.print("Connecting...");
  WiFi.begin(ssid, passwd);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
  Serial.println("connected");
  Serial.println(WiFi.localIP());
}

void loop() {
  if ((WiFi.status() == WL_CONNECTED)) {
    HTTPClient http;
    Serial.print("[HTTP] begin...\n");

    String api_key = "6e0583c3f253d57c0d62419bb344d30f";
    String base_url = "http://api.openweathermap.org/data/2.5/weather";
    String url = base_url + "?zip=530-0015,JP&units=metric&APPID=" + api_key;

    Serial.println(url);
    http.begin(url); //HTTP
    Serial.print("[HTTP] GET...\n");
    int httpCode = http.GET();

    if (httpCode > 0) {
      Serial.printf("[HTTP] GET... code: %d\n", httpCode);
      if (httpCode == HTTP_CODE_OK) {
        String payload = http.getString();

        StaticJsonDocument<2000> doc;
        DeserializationError error = deserializeJson(doc, payload);
        if (error) {
          Serial.print(F("deserializeJson() failed: "));
          Serial.println(error.c_str());
          return;
        }
        JsonObject root = doc.as<JsonObject>();

        const char* cityName = root["name"];
        const char* icon = root["weather"][0]["icon"];
        float temp = root["main"]["temp"];
        int pres = root["main"]["pressure"];
        int hum = root["main"]["humidity"];
        Serial.printf("都市名:%s 天気アイコン:%s\n", cityName, icon);
        Serial.printf("温度:%.1f℃ 気圧:%dhPa 湿度%d%%\n", temp, pres, hum);
        Serial.println(" ");
        Serial.println(" ");

        if (icon == "01d" || icon == "01n"){
          digitalWrite(ledPinA, HIGH);
        }else if (icon == "02d" || icon == "02n"){
          digitalWrite(ledPinA, HIGH);
        }else{
          digitalWrite(ledPinA, LOW);
        }
        
      }
    } else {
      Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
    }
    http.end();
  }
  
  delay(5000);
}
