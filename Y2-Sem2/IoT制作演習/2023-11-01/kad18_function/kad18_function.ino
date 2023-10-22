#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h> 
#endif
#define LED_PIN    5
#define LED_COUNT 60
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);


void setup() {
  #if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
    clock_prescale_set(clock_div_1);
  #endif
  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();            // Turn OFF all pixels ASAP
  strip.setBrightness(50); // Set BRIGHTNESS to about 1/5 (max = 255)
}


void loop() {
    colorDotOn(0, strip.Color(255,0,0)); //0番目(一番下）が赤色に光る   
    delay(1000);    
    colorDotOff(0); //Red 0番目(一番下）が消える   
    delay(1000);      

    colorDotOn(4, strip.Color(0, 255, 0)); //4番目(一番上）が緑色に光る   
    delay(1000);   
    colorDotOff(4); //Red 4番目(一番上）が消える   
    delay(1000); 
}


void colorDotOn(int i, uint32_t color){
  strip.clear();
  colorDotOff(i);
  strip.setPixelColor(i, color); // Set pixel 'c' to value 'color'
  strip.show(); // Update strip with new contents
} 

 
void colorDotOff(int i){ 
  strip.setPixelColor(i, 0);
  strip.show();
} 
