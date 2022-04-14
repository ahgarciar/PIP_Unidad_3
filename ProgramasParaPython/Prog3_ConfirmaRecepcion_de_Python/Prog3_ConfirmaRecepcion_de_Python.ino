int led = 13;

void setup() {
  // put your setup code here, to run once: 
  Serial.begin(9600);  
  Serial.setTimeout(100);
  pinMode(led, OUTPUT);
}

int v; 
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
      v = Serial.readString().toInt();
      digitalWrite(led, v);
      Serial.println("Se recibio: " + String(v));
    }
  delay(100);
}
