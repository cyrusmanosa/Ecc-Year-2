const int analogPin = A17;
int darkLevel = 1000;
int n = 0;

void setup() {
  Serial.begin(115200);
  ledcSetup(0,12800,8);
  ledcAttachPin(4,0);
}

void loop() {
  int a = analogRead(analogPin);
  int b = map(a,0,4095,255,0);
  Serial.print(a);
  Serial.print(" / ");
  Serial.println(b);
  ledcWrite(0,b);
  delay(10);
}
