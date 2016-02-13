#include <Wire.h>
#include <ServoShield2.h>

ServoShield2 servos = ServoShield2(127);//Address of 127, using 50Hz mode

void setup() {
  Serial.begin(9600); 
  Serial.println("Initializing...");
  servos.start();

  for (int servo = 0; servo < 6; servo++)//Initialize all 16 servos
  {
    servos.setbounds(servo,0,3000);
    servos.setposition(servo, 1500);      //Set the initial position of the servo
  }

//  servos.setbounds(0, 0, 5000);
//  servos.setposition(0, 1500);
  Serial.println("Init Done");
}

void loop() {
  if(Serial.available())
  {
    String first  = Serial.readStringUntil(',');
    Serial.read(); //next character is comma, so skip it using this
    String second = Serial.readStringUntil(',');
    Serial.print(first);
    Serial.println();
    Serial.print(second);
    setDegree(first.toInt(),second.toInt());
  }
}


void setDegree(int servo, int degree)
{
  if(servo == 0)
    servos.setposition(0,map(degree,0,1000,2600,700));
  if(servo == 1)
    servos.setposition(1,map(degree,0,1000,1500,700));
  if(servo == 2)
    servos.setposition(2,map(degree,0,1000,700,1500));
  if(servo == 3)
    servos.setposition(3,map(degree,0,1000,1500,600));
  if(servo == 4)
    servos.setposition(4,map(degree,0,1000,700,1600));
  if(servo == 5)
    servos.setposition(5,map(degree,0,1000,1400,3000));
    
}

