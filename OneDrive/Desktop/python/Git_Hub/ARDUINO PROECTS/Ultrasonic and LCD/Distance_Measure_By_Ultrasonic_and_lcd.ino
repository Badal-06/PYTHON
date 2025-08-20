#include <LiquidCrystal.h>
LiquidCrystal lcd (1,2,4,5,6,7);
const int trig = 9;
const int echo = 10;
long duration;
int distanceCm ,distanceInch;

void setup()
{
  lcd.begin(16,2);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
}

void loop()
{
  digitalWrite(trig ,0);
  delayMicroseconds(2); 
  digitalWrite(trig ,1);
  delayMicroseconds(10);
  digitalWrite(trig ,0);
  
  duration = pulseIn(echo ,1);
  distanceCm = (duration*0.034)/2;
  distanceInch =(duration*0.0133)/2;
  
  lcd.setCursor(0,0);
  lcd.print("Distance:");
  lcd.print(distanceCm);
  lcd.print(" cm");
  delay(10);
  lcd.setCursor(0,1);
  lcd.print("Distance:");
  lcd.print(distanceInch);
  lcd.print(" inch");
  delay(500);
}
