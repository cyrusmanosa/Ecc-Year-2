const int pwmPin = A10;

void setup() {
  ledcSetup(0,12800,8);
  ledcAttachPin(pwmPin,0);
}

void loop() {
  ledcWrite(0,255);
  delay(1000);
  ledcWrite(0,127);
  delay(1000);
  ledcWrite(0,0);
  delay(1000);
}
