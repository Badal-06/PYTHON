void setup()
{
  pinMode(3, OUTPUT);
}

void loop()
{
  digitalWrite(3, 1);
  delay(1000); 
  digitalWrite(3, 0);
  delay(1000); 
}