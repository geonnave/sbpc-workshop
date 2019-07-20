/* 
 Controle de LED por comunicação serial
*/

char valorSerial = 0;
int pinoLED = 7;

void setup() {
  Serial.begin(9600);
  pinMode(pinoLED, OUTPUT);
}
 
void loop() {
  if (Serial.available() > 0) {
        valorSerial = Serial.read();
        if (valorSerial == 'l') {
            digitalWrite(pinoLED, HIGH);
            Serial.println("LED da Arduino ligado!");
        }
        else if (valorSerial == 'd') {
            digitalWrite(pinoLED, LOW);
            Serial.println("LED da Arduino desligado!");
        }
  }
  delay(1000);
}
