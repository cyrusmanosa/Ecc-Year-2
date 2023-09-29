void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(17,INPUT);
  pinMode(16,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int b = digitalRead(17);
  if ( b == 1 ){
   Serial.println("押された"); 
   digitalWrite(16,HIGH);
  }else{
    Serial.println(" "); 
    digitalWrite(16,LOW);
  }
  delay(10);
}
