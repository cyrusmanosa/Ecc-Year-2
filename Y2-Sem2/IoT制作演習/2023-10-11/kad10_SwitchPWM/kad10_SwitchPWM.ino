const int pwmPin = A10; // GPIO IO4pin 
const int btnPin = 17; // GPIO IO17pin 
bool flag = false; //フラグ初期値false:押されていない状態 //他にもグローバル変数を作ってもよい（配列も可）。  
bool laststate = false;
std::array<int,5> duty = {0,63,127,191,255};
int n = 0;


void setup() { 
  Serial.begin(115200);
  ledcSetup(0,12800,8);
  ledcAttachPin(pwmPin,0);
  pinMode(btnPin, INPUT); // Switch デジタル入力
}  


void loop() {   
   bool b = digitalRead(btnPin);
   if (b==true && !laststate){
    delay(100);
    b = digitalRead(btnPin);
    if (b){
      if (n == 4){
        n = 0;
      }else{
        n++;
      }
      Serial.print("duty=");
      Serial.print(duty[n]);
      Serial.println(" ");
      ledcWrite(0,duty[n]);
    }
   }
   laststate = b;
}
