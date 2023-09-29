const int pwmPin = A10; // GPIO IO4pin 
const int btnPin = 17; // GPIO IO17pin 
bool flag = false; //フラグ初期値false:押されていない状態 //他にもグローバル変数を作ってもよい（配列も可）。  
void setup() { 
  Serial.begin(115200);
  ledcSetup(0,12800,8);
  ledcAttachPin(pwmPin,0);
  pinMode(btnPin, INPUT); // Switch デジタル入力
}  

std::array<int,5> duty = [0,63,127,191,255];
int n = 0;
void loop() {   
   int b = digitalRead(btnPin);
   if (b==1){
    n++;
    Serial.println("duty=",duty[n]);
    ledcWrite(0,duty);
    delay(1000);
   }
}
