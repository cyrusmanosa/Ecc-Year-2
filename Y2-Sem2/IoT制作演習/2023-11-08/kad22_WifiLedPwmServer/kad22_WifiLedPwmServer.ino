#include <WiFi.h>

// 接続先のSSIDとパスワード　学内CampusIOT
const char ssid[] = "CampusIoT-WiFi";
const char passwd[] = "0b8b413f2c0fa6aa90e085e9431abbf1fa1b2bd2db0ecf4ae9ce4b2e87da770c";
const int pwmPin = A10;
WiFiServer server(80);

void setup(){
  delay(1000);
  Serial.begin(115200);
  ledcSetup(0,12800,8);
  ledcAttachPin(pwmPin,0);

  // WIFI接続シーケンス
  Serial.print("Connecting....");
  WiFi.begin(ssid,passwd);
  while (WiFi.status() != WL_CONNECTED){
    delay(100);
    Serial.print(".");
  }
  Serial.println("connected");
  Serial.println(WiFi.localIP());

  server.begin();
}
void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("new client");
    String currentLine = "";
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        if (c == '\n') {
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();
            client.println("<!DOCTYPE html>");
            client.println("<html>");
            client.println("<head>");
            client.println("<meta name='viewport' content='initial-scale=1.5'>");
            client.println("</head>");
            client.println("<body>");
            client.println("<form method='get'>");
            client.println("<h1>ESP32</h1>");
            client.println("<h2>Wi-Fi LED Switch</h2>");
            client.print("<input type='radio' name=level value='0%'>");
            client.println("<label>0%</label>");
            client.println("<br>");
            client.println("<input type='radio' name=level value='25%'>");
            client.println("<label>25%</label>");
            client.println("<br>");
            client.println("<input type='radio' name=level value='50%'>");
            client.println("<label>50%</label>");
            client.println("<br>");
            client.println("<input type='radio' name=level value='75%'>");
            client.println("<label>75%</label>");
            client.println("<br>");
            client.println("<input type='radio' name=level value='100%'>");
            client.println("<label>100%</label>");
            client.println("<br>");
            client.println("<input type='submit' name=btn value='Send'>");
            client.println("</form>");
            client.println("</body>");
            client.println("</html>");
            client.println();
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
          if (currentLine.endsWith("GET /?level=0%25&btn=Send")){
            ledcWrite(0,0);
          } else if (currentLine.endsWith("GET /?level=25%25&btn=Send")){
            ledcWrite(0,63);
          } else if (currentLine.endsWith("GET /?level=50%25&btn=Send%")){
            ledcWrite(0,127);
          } else if (currentLine.endsWith("GET /?level=75%25&btn=Send")){
            ledcWrite(0,191);
          } else if (currentLine.endsWith("GET /?level=100%25&btn=Send")){
            ledcWrite(0,255);
          }
      }
    }

    client.stop();
    Serial.println("client disconnected");
  }
}
