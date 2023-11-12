#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#define USE_SERIAL Serial

const char ssid[] = "CampusIoT-WiFi";
const char passwd[] = "0b8b413f2c0fa6aa90e085e9431abbf1fa1b2bd2db0ecf4ae9ce4b2e87da770c";

void setup() {

  USE_SERIAL.begin(115200);

  Serial.print("Connecting....");
  WiFi.begin(ssid,passwd);
  while (WiFi.status() != WL_CONNECTED){
    delay(100);
    Serial.print(".");
  }
  Serial.println("connected");
  Serial.println(WiFi.localIP());

}

void loop() {
    // wait for WiFi connection
    if(WiFi.status() == WL_CONNECTED) {

        HTTPClient http;

        USE_SERIAL.print("[HTTP] begin...\n");
        http.begin("http://arduinojson.org/example.json"); //HTTP

        USE_SERIAL.print("[HTTP] GET...\n");
        int httpCode = http.GET();
        if(httpCode > 0) {
            USE_SERIAL.printf("[HTTP] GET... code: %d\n", httpCode);
            if(httpCode == HTTP_CODE_OK) {
                String payload = http.getString();
                USE_SERIAL.println(payload);
            }
        } else {
            USE_SERIAL.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
        }

        http.end();
    }

    delay(5000);
}
