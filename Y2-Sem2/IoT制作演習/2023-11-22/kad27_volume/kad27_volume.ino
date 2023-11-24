const int volumePin = A3;
const int bluePin = 4;

void setup() {
  Serial.begin(115200);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  int ana = analogRead(volumePin);
  ledFlash(bluePin, 200);

  double v = map(ana, 0, 4095, 0, 3300) / 1E3;
  Serial.printf("アナログ入力：%d、単純変換値：%f[V]\n",ana,v);

  delay(1000);
}

void ledFlash(int ledPin, int delayTime){
  digitalWrite(ledPin, HIGH);
  delay(delayTime);
  digitalWrite(ledPin,LOW);
}
