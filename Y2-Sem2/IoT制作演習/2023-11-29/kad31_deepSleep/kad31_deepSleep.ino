#include "esp_sleep.h"
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Start");
  esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_PERIPH, ESP_PD_OPTION_OFF);
  esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_SLOW_MEM, ESP_PD_OPTION_OFF);
  esp_sleep_pd_config(ESP_PD_DOMAIN_RTC_FAST_MEM, ESP_PD_OPTION_OFF);
  esp_sleep_pd_config(ESP_PD_DOMAIN_MAX, ESP_PD_OPTION_OFF);
}
void loop() {
  delay(10000);
  Serial.print("goo");
  esp_sleep_enable_timer_wakeup(10 * 1000);
  esp_deep_sleep_start();
}
