#include <WiFi.h>
#include <PubSubClient.h>
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
 #include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif
#define LED_PIN    17
#define LED_COUNT 60
#define MSG_BUFFER_SIZE  (50)

const char* ssid = "CampusIoT-WiFi";
const char* password = "0b8b413f2c0fa6aa90e085e9431abbf1fa1b2bd2db0ecf4ae9ce4b2e87da770c";
const char* mqtt_server = "team-d.cloud.shiftr.io";
const int swPin = 17;
unsigned long lastMsg = 0;
char msg[MSG_BUFFER_SIZE];
char teamLED = 0;

WiFiClient espClient;
PubSubClient client(espClient);
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  randomSeed(micros());
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    String clientId = "SK2A03";
    if(client.connect(clientId.c_str(),"team-d","xrg5nDrNKfut9rnA")){
      Serial.println("connected");
      client.publish("SK2A/team-d","ブン");
      client.subscribe("SK2A/#");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  strip.show();            // Turn OFF all pixels ASAP
  strip.setBrightness(50); // Set BRIGHTNESS to about 1/5 (max = 255)
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  bool open = false;
  bool currentState = digitalRead(swPin);
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  unsigned long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    if (currentState == true) {


      
      open = true;


      
       if(teamLED == 0){
         teamLED = 1;
       }else{
        teamLED = 0;
       }


       
    }
    if (open){
      snprintf (msg,50,"%d", teamLED);
      Serial.print("Publish message ブン: ");
      Serial.println(msg);
      client.publish("SK2A/team-d", msg);
    }
  }
}

void callback(char* topic, byte* payload, unsigned int length) {

  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
  
  int data = payload[0] - '0';
  uint32_t color; 
  if (data <= 5){
    color = strip.Color(  0,   0, 255);
  }else{
    color = strip.Color(  255,   255, 0); // 黄色（255,255,0）
  }
  
  switch(data){
    case 0:
      strip.clear();
      break; 
    case 1:
      strip.clear();
      for(int i=0; i<1; i++) {
        strip.setPixelColor(i, color);
        strip.show();
      }
      break;
    case 2:
      strip.clear();
      for(int i=0; i<2; i++) {
        strip.setPixelColor(i, color);
        strip.show();
      }
      break;
    case 3:
      strip.clear();
      for(int i=0; i<3; i++) {
        strip.setPixelColor(i, color);
        strip.show();
      }
      break;
    case 4:
      strip.clear();
      for(int i=0; i<4; i++) {
        strip.setPixelColor(i, color);
        strip.show();
      }
      break;
   case 5:
      strip.clear();
      for(int i=0; i<5; i++) {
        strip.setPixelColor(i, color);
        strip.show();
      }
      break; 
    case 6:
      strip.clear();
      for(int i=0; i<1; i++) {
        strip.setPixelColor(i, color);
        strip.show();
      }
      break;
    default:
      strip.clear();
      break;
  }
}
