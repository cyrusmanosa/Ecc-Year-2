int HT = 200;
int LT = 200;
  

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(17,INPUT);
  pinMode(16,OUTPUT);
}

void loop() {
  int b = digitalRead(17);
  
  if ( b == 1 ){
    Serial.println("押された"); 
    // LED Loop
    for (int i=0; i<9;i++){
      if (i == 3){
        delay(200);
        HT = 600;
      }
      if (i == 6){
        delay(200);
        HT = 200;
      }
     digitalWrite(16,HIGH);
     delay(HT);
     digitalWrite(16, LOW);    
     delay(LT);  
    }
  }
}
