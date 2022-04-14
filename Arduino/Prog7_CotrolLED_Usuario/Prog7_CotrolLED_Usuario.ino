int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);  
  Serial.begin(9600);
  Serial.setTimeout(200);
}

String v; 
int aux;
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
     v = Serial.readString();     
     aux = v.toInt();
     digitalWrite(led, aux);
   }
delay(100);
  
  
}
