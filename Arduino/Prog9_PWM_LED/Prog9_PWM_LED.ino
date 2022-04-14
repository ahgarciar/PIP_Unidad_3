int pot = A0;
int led = 11;

void setup() {
  // put your setup code here, to run once: 
  Serial.begin(9600);  
}

int aux;
void loop() {
  // put your main code here, to run repeatedly:

  aux = analogRead(pot);
  aux = aux / 4;
  Serial.println(aux);
  analogWrite(led, aux); //0 - 255 ---> PWM
  
  delay(100);
  
  
}
