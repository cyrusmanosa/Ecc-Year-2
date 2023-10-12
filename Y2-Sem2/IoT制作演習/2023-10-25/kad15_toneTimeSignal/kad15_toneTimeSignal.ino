#define LEDC_CHANNEL_0 0
#define LEDC_TIMER_13_BIT 13
#define LEDC_BASE_FREQ 5000

const int buzPin = 23;
const int btnPin = 17;
int noteDuration = 1000/8;

double note_half = noteDuration*4;
double note_whole = noteDuration*8;
double note_16th = noteDuration/2;

void setup() {
  Serial.begin(115200);
  ledcSetup(LEDC_CHANNEL_0,LEDC_BASE_FREQ,LEDC_TIMER_13_BIT);
  ledcAttachPin(buzPin,LEDC_CHANNEL_0);
  pinMode(btnPin,INPUT);
}

void loop() {
  if(digitalRead(btnPin) == HIGH){
    for(int i=1; i<8; i++){
      if (i == 7){
        ledcWriteTone(LEDC_CHANNEL_0, 880);
        delay(note_whole);  
      }else if(i % 2 == 1){
        ledcWriteTone(LEDC_CHANNEL_0, 440);
        delay(note_half);
      }else if (i % 2 == 0){
        ledcWriteTone(LEDC_CHANNEL_0, 0);
        delay(note_16th);
      }
    }
  }
  ledcWriteTone(LEDC_CHANNEL_0, 0);
}
