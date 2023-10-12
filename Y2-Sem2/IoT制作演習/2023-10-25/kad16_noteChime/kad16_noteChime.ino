#define LEDC_CHANNEL_0 0
#define LEDC_TIMER_13_BIT 13
#define LEDC_BASE_FREQ 5000

const int buzPin = 23;
const int btnPin = 17;
const int NOTE_NONE = NOTE_MAX;

int melody[] = {
  NOTE_C,NOTE_G,NOTE_G,NOTE_A,NOTE_G,NOTE_NONE,NOTE_B,NOTE_C
};

int m[] = {
  NOTE_E,NOTE_C,NOTE_D,NOTE_G, NOTE_NONE ,NOTE_G,NOTE_D,NOTE_E,NOTE_C
};

int noteOctaves[] = {4,3,3,3,3,0,3,4};
int noteDurations[] = {4,8,8,4,4,4,4,4};

int Octaves[] = {4,4,4,3, 0 ,3,4,4,4};
int Durations[] = {2,2,2,1, 4 ,4,2,2,2};

void setup(){
  ledcSetup(LEDC_CHANNEL_0,LEDC_BASE_FREQ,LEDC_TIMER_13_BIT);
  ledcAttachPin( buzPin, LEDC_CHANNEL_0);
  pinMode(btnPin,INPUT);
}

void loop(){
  if(digitalRead(btnPin) == HIGH){
    for (int thisNote = 0; thisNote < 9; thisNote++){
      ledcWriteNote( LEDC_CHANNEL_0 , (note_t)m[thisNote] , Octaves[thisNote] );
      
      int pauseBetweenNotes = 1000 / Durations[thisNote] * 1.30;
      
      delay(pauseBetweenNotes);
      ledcWriteTone( LEDC_CHANNEL_0 , 0);
    }
    delay(2000);
  }
}
