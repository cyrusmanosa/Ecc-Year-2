#include "ESP32_BME280_SPI.h"
#include <Wire.h>
#include "Ambient.h"

WiFiClient client;
Ambient ambient;

#define BATTERY 39

const uint8_t SCLK_bme280 = 14;
const uint8_t MOSI_bme280 =13; //Master Output Slave Input ESP32=Master,BME280=slave 
const uint8_t MISO_bme280 =12; //Master Input Slave Output
const uint8_t CS_bme280 = 26; //CS pin

const char* ssid = "CampusIoT-WiFi";
const char* password = "0b8b413f2c0fa6aa90e085e9431abbf1fa1b2bd2db0ecf4ae9ce4b2e87da770c";

unsigned int channelId = 75168;
const char* writeKey = "0d23b948a9182484";

ESP32_BME280_SPI bme280spi(SCLK_bme280, MOSI_bme280, MISO_bme280, CS_bme280, 10000000);

void setup(){
  Serial.begin(115200);
  delay(1000); //Take some time to open up the Serial Monitor
  WiFi.begin(ssid, password);  //  Wi-Fi APに接続

  while (WiFi.status() != WL_CONNECTED) {  //  Wi-Fi AP接続待ち
      delay(500);
      Serial.print(".");
  }

  Serial.print("WiFi connected\r\nIP address: ");
  Serial.println(WiFi.localIP());

  ambient.begin(channelId, writeKey, &client); // チャネルIDとライトキーを指定してAmbientの初期化

  uint8_t t_sb = 5; //stanby 1000ms
  uint8_t filter = 0; //filter O = off
  uint8_t osrs_t = 4; //OverSampling Temperature x4
  uint8_t osrs_p = 4; //OverSampling Pressure x4
  uint8_t osrs_h = 4; //OverSampling Humidity x4
  uint8_t Mode = 3; //Normal mode
 
  bme280spi.ESP32_BME280_SPI_Init(t_sb, filter, osrs_t, osrs_p, osrs_h, Mode);
  delay(1000);
}

void loop(){
  delay(5000);
  float temperature = bme280spi.Read_Temperature();
  float humidity = bme280spi.Read_Humidity();
  float pressure = bme280spi.Read_Pressure();
  float vbat = (analogRead(BATTERY) / 4095.0 * 3.3 + 0.1132) * 2.0;

  ambient.set(1,temperature);
  ambient.set(2,humidity);
  ambient.set(3,pressure);
  ambient.set(4,vbat);
  ambient.send();

  Serial.println("-----------------------");
  Serial.print("Temperature: ");
  Serial.println(temperature);
  Serial.print("Humidity: ");
  Serial.println(humidity);
  Serial.print("Pressure: ");
  Serial.println(pressure);
  Serial.print("Vbat: ");
  Serial.println(vbat);
  Serial.println("-----------------------");
}
