const int swPin = 17;
int count = 1;
bool flag = false;
bool lastState = false;

void setup() {
  Serial.begin(115200);
  pinMode(swPin, INPUT);
}

void loop() {
  bool currentState = digitalRead(swPin);
  if (currentState == true && lastState == false) {
    delay(50);
    currentState = digitalRead(swPin);
    
    if (currentState == true) {
      Serial.println(count);
      count++;
      flag = true;
    }
  }

  lastState = currentState;
}
