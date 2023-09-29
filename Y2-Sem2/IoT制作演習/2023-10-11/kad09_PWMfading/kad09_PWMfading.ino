const int pwmPin = 4;

void setup() {
  Serial.begin(115200);
  ledcSetup(0,12800,8);
  ledcAttachPin(pwmPin,0);
}

void loop() {
  static uint8_t duty = 0;
  static int diff = 0;
  for ( diff; diff < 256; diff++){
      Serial.printf("%3d\n",diff);
      ledcWrite(0,diff);
      delay(10);
      if (diff == 255){
        for (diff; diff > 0; diff--){
          Serial.printf("%3d\n",diff);
          ledcWrite(0,diff);
          delay(10);
        }
      }
  }
}
