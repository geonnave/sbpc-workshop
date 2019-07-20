/* 
 Controle de LED na porta digital
*/

char valorSerial = 0;
int pinoLED = 7;

void setup() {
  Serial.begin(9600);
  pinMode(pinoLED, OUTPUT);
}
 
void loop() {
  digitalWrite(pinoLED, HIGH);
  delay(1000);
  digitalWrite(pinoLED, LOW);
  delay(1000);
}
