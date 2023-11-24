#include <Wire.h>
#include "Ambient.h"


WiFiClient client;
Ambient ambient;

const int cdsPin = A0;
const int redPin = 16;
const int bluePin = 4;

const char* ssid = "CampusIoT-WiFi";
const char* password = "0b8b413f2c0fa6aa90e085e9431abbf1fa1b2bd2db0ecf4ae9ce4b2e87da770c";

unsigned int channelId = 72144; // AmbientのチャネルID
const char* writeKey = "1fc248c82778c3c8"; // ライトキー

void setup(){
  Serial.begin(115200);
  ledcSetup(0,12800,8);
  ledcAttachPin(redPin,0);
  pinMode(bluePin, OUTPUT);
  
  WiFi.begin(ssid, password);  //  Wi-Fi APに接続

  while (WiFi.status() != WL_CONNECTED) {  //  Wi-Fi AP接続待ち
      delay(500);
      Serial.print(".");
  }

  if (WiFi.status() == WL_CONNECTED){
    ledcWrite(0, 255);
  }

  Serial.print("WiFi connected\r\nIP address: ");
  Serial.println(WiFi.localIP());

  ambient.begin(channelId, writeKey, &client); // チャネルIDとライトキーを指定してAmbientの初期化
}

void loop() {
  int ana = analogRead(cdsPin);
  ledFlash(bluePin, 200);

  ambient.set(1,ana);
  ambient.send();
  
  Serial.printf("アナログ入力：%d\n",ana);
  delay(1000);
}

void ledFlash(int ledPin, int delayTime){
  digitalWrite(ledPin, HIGH);
  delay(delayTime);
  digitalWrite(ledPin,LOW);
}
