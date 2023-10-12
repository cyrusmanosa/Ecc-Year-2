const int analogPin = A17;
int darkLevel = 1000;

void setup() {
  Serial.begin(115200);
  pinMode(4,OUTPUT);
  pinMode(16,OUTPUT);
}

void loop() {
  int a = analogRead(analogPin);
  double b = (3.3 * a) / 4096;
  Serial.print(a);
  Serial.print("=");
  Serial.print(b);
  Serial.println("[V]");

  if(a < darkLevel){
    digitalWrite(4,HIGH);
    digitalWrite(16,HIGH);
  }else{
    digitalWrite(4,LOW);
    digitalWrite(16,LOW);
  }
  
  delay(100);
}
