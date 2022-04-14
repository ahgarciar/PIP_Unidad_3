//Módulo UART --
String nombre;
int index;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //baudios
  nombre = "Aquino";
  index = 0;
}


void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hola " + nombre + ", gusto en conocerte!");
  delay(1000); //ms
  Serial.println("Contador: " + String(index++) + "\n\n");  
  delay(1000); //ms
}
