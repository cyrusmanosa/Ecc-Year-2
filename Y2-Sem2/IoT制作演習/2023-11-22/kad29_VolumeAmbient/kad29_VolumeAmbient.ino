#include <Wire.h>
#include "Ambient.h"


WiFiClient client;
Ambient ambient;

const int volumePin = A3;
const int bluePin = 4;

const char* ssid = "CampusIoT-WiFi";
const char* password = "0b8b413f2c0fa6aa90e085e9431abbf1fa1b2bd2db0ecf4ae9ce4b2e87da770c";

unsigned int channelId = 70178; // AmbientのチャネルID
const char* writeKey = "a716d6cd5188ae0d"; // ライトキー

void setup(){
  Serial.begin(115200);
  pinMode(bluePin, OUTPUT);
  WiFi.begin(ssid, password);  //  Wi-Fi APに接続

  while (WiFi.status() != WL_CONNECTED) {  //  Wi-Fi AP接続待ち
      delay(500);
      Serial.print(".");
  }

  Serial.print("WiFi connected\r\nIP address: ");
  Serial.println(WiFi.localIP());

  ambient.begin(channelId, writeKey, &client); // チャネルIDとライトキーを指定してAmbientの初期化
}

void loop() {
  int rand;
  rand = random(1000);

  int ana = analogRead(volumePin);
  ledFlash(bluePin, 200);
  double v = map(ana, 0, 4095, 0, 3300) / 1E3;

  ambient.set(1,rand);
  ambient.set(2,v);
  ambient.send();
  
  Serial.printf("アナログ入力：%d、単純変換値：%f[V]\n",ana,v);
  Serial.println(rand);
  delay(1000);
}

void ledFlash(int ledPin, int delayTime){
  digitalWrite(ledPin, HIGH);
  delay(delayTime);
  digitalWrite(ledPin,LOW);
}
