//Código DigiSpark para movimentar o mouse

#include <DigiMouse.h>

void setup() {
  DigiMouse.begin();
} 

void loop() {
  
  //Movimenta o no eixo Y 
  //DigiMouse.moveY(10); //down 10
  //DigiMouse.delay(500);
  //Movimenta o mouse de um lado a outro
  DigiMouse.moveX(20); //right 20
  DigiMouse.delay(500);
  DigiMouse.moveX(-20);
  DigiMouse.delay(500);
  
  //Movimenta o scroll do mouse
  //DigiMouse.scroll(80);
  //DigiMouse.delay(1000);
  
  //Função para clicar e cancelar o clique
/*  DigiMouse.setButtons(1<<0); //left click
  DigiMouse.delay(500);
  DigiMouse.setButtons(0); //unclick all
  DigiMouse.delay(500); */

  //Função de clique dos botões
  //DigiMouse.rightClick();
  //DigiMouse.delay(500);
  DigiMouse.leftClick();
  DigiMouse.delay(1000);
  //DigiMouse.middleClick();
  //DigiMouse.delay(500);*/

}