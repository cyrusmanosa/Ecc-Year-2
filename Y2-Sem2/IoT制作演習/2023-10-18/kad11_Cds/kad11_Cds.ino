const int analogPin = A17;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int a = analogRead(analogPin);
  double b = (3.3 * a) / 4096;
  Serial.print(a);
  Serial.print("=");
  Serial.print(b);
  Serial.println("[V]");
  
  delay(100);
}
