int pot = A0;

void setup() {
  // put your setup code here, to run once: 
  Serial.begin(9600);  
}

int aux;
void loop() {
  // put your main code here, to run repeatedly:

  aux = analogRead(pot);
  Serial.println(aux);
  
  delay(100);
  
  
}
