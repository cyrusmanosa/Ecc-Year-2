#define LEDC_CHANNEL_0 0
#define LEDC_TIMER_13_BIT 13
#define LEDC_BASE_FREQ 5000

const int buzPin = 23;
const int btnPin = 17;
int noteDuration = 1000/8;

void setup() {
  Serial.begin(115200);
  ledcSetup(LEDC_CHANNEL_0,LEDC_BASE_FREQ,LEDC_TIMER_13_BIT);
  ledcAttachPin(buzPin,LEDC_CHANNEL_0);
  pinMode(btnPin,INPUT);
}

void loop() {
  if(digitalRead(btnPin) == HIGH){
    for(int i=25; i<120; i++){
      int x = 20*i;
      ledcWriteTone(LEDC_CHANNEL_0, x);
      if (x ==2400){
        Serial.println("");
      }
      Serial.print(x);
      Serial.print(" ");
      delay(noteDuration);
    }
    
    Serial.println(" ");

    for(int i = 120; i >=25; i--){
      int x = 20*i;
      ledcWriteTone(LEDC_CHANNEL_0, x);
      if (x ==2400){
        Serial.println("");
      }
      Serial.print(x);
      Serial.print(" ");
      delay(noteDuration);
    }
  }
  ledcWriteTone(LEDC_CHANNEL_0, 0);
}
