int porta = 1; //Inicia uma variavel do tipo inteiro que receber o valor da porta, no caso, porta 1
 
void setup() {  
  pinMode(porta, OUTPUT); //Declara a porta 1 como saida
}
 
void loop() {
  digitalWrite(porta, HIGH); //Deixa a porta 1 em nivel logico alto
  delay(1000); //Aguarda 100 milissegundos
  digitalWrite(porta, LOW); //Deixa a porta em nivel logico baixo    
  delay(1000); //Aguarda 100 milissegundos
}
