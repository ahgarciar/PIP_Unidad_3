//Módulo UART --
String nombre;
bool bandera;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //baudios
  nombre = "Aquino";
  bandera = true;
}


void loop() {
  // put your main code here, to run repeatedly:
  if (bandera == true) {
    Serial.println("Hola " + nombre + ", gusto en conocerte!");
    delay(1000); //ms
    Serial.println("Contador de Amigos: " + String(10) + "\n\n");
    delay(1000); //ms
    bandera  = false;
  }
  //Serial.println("El programa se repetira...");
}
