#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int sensorPin = A0;
const int lightPin = A1;

void setup() {
  lcd.begin(16,2);
  Serial.begin(9600);
}

void loop(){
  int sensorVal = analogRead(sensorPin);

  float voltage = (sensorVal / 1024.0) * 5.0;
  float temperature = (voltage - .5) * 100;

  Serial.print("Temperature (C): ");
  Serial.println(temperature);
  
  int lightValue = analogRead(lightPin);

  Serial.print(" Light Value: ");
  Serial.println(lightValue);

  lcd.home();
  lcd.print(temperature);
  lcd.setCursor(0,1);
  lcd.print(lightValue);

  delay(1000);
}
