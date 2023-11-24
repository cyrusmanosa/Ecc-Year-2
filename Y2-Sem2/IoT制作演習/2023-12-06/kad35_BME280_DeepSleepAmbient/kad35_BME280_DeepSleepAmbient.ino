#include "ESP32_BME280_SPI.h"
#include "esp_sleep.h"

const uint8_t SCLK_bme280 = 14;
const uint8_t MOSI_bme280 =13; //Master Output Slave Input ESP32=Master,BME280=slave 
const uint8_t MISO_bme280 =12; //Master Input Slave Output
const uint8_t CS_bme280 = 26; //CS pin

ESP32_BME280_SPI bme280spi(SCLK_bme280, MOSI_bme280, MISO_bme280, CS_bme280, 10000000);

void setup(){
  Serial.begin(115200);
  Serial.println("Start");
  esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_PERIPH, ESP_PD_OPTION_OFF);
  esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_SLOW_MEM, ESP_PD_OPTION_OFF);
  esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_FAST_MEM, ESP_PD_OPTION_OFF);
  esp_sleep_pd_config(ESP_PD_DOMAIN_MAX, ESP_PD_OPTION_OFF);
  
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
  esp_sleep_enable_timer_wakeup(10 * 100);
  float temperature = bme280spi.Read_Temperature();
  float humidity = bme280spi.Read_Humidity();
  float pressure = bme280spi.Read_Pressure();

  Serial.println("-----------------------");
  Serial.print("Temperature: ");
  Serial.print(temperature,1);
  Serial.println("℃");
  Serial.print("Humidity: ");
  Serial.print(humidity,1);
  Serial.println("%");
  Serial.print("Pressure: ");
  Serial.println(pressure,1);
  Serial.print("hPa");
  Serial.println("-----------------------");
  delay(5000);
  esp_deep_sleep_start();
}
