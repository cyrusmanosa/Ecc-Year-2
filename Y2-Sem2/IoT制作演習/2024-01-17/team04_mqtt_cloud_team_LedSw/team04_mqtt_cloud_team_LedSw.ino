#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "CampusIoT-WiFi";
const char* password = "0b8b413f2c0fa6aa90e085e9431abbf1fa1b2bd2db0ecf4ae9ce4b2e87da770c";
const char* mqtt_server = "team-d.cloud.shiftr.io";

WiFiClient espClient;
PubSubClient client(espClient);
#define BUILTIN_LED 4
#define MSG_BUFFER_SIZE  (50)
unsigned long lastMsg = 0;
char msg[MSG_BUFFER_SIZE];
const int swPin = 17;
char teamLED = 0;


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
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    
    // Create a random client ID
    String clientId = "sk2a03";
    
    // Attempt to connect
    if(client.connect(clientId.c_str(),"team-d","xrg5nDrNKfut9rnA")){
      Serial.println("connected");
      
      // Once connected, publish an announcement...
      client.publish("SK2A/team-d","ブン");
      
      // ... and resubscribe
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
  pinMode(swPin, INPUT);
  pinMode(BUILTIN_LED, OUTPUT);
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
  if ((char)payload[0] == '1') {
    teamLED = 1;
    digitalWrite(BUILTIN_LED, HIGH);
  } else {
    teamLED = 0;
    digitalWrite(BUILTIN_LED, LOW);
  }
}
