/*************************************************** 
  This is an example for our Adafruit 16-channel PWM & Servo driver
  Servo test - this will drive 16 servos, one after the other

  Pick one up today in the adafruit shop!
  ------> http://www.adafruit.com/products/815

  These displays use I2C to communicate, 2 pins are required to  
  interface. For Arduino UNOs, thats SCL -> Analog 5, SDA -> Analog 4

  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
// you can also call it with a different address you want
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);

// Depending on your servo make, the pulse width min and max may vary, you 
// want these to be as small/large as possible without hitting the hard stop
// for max range. You'll have to tweak them as necessary to match the servos you
// have!
#define SERVOMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  590 // this is the 'maximum' pulse length count (out of 4096)

// our servo # counter
uint8_t servonum = 0;

int angle[6];

void setup() {
  for(int i = 0; i < 6; i++)
  {
    angle[i] = 300;
  }
  
  Serial.begin(38400);
  Serial.println("16 channel Servo test!");

#ifdef ESP8266
  Wire.pins(2, 14);   // ESP8266 can use any two pins, such as SDA to #2 and SCL to #14
#endif

  pwm.begin();
  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates
  
  Serial.println("hey guys im done initializing stuff\n");;

  setDegreeHard(500,500,500,690,550,1000);
}

void loop()
{
  
}


void setDegreeHard(int degree0, int degree1, int degree2, int degree3, int degree4, int degree5)
{

  Serial.print("ok i will");
  
  int wanted[6];
  wanted[0] = map(degree0,0,1000,150,590);
  wanted[1] = map(degree1,0,1000,150,520);
  wanted[2] = map(degree2,0,1000,570,160);
  wanted[3] = map(degree3,0,1000,150,600);
  wanted[4] = map(degree4,0,1000,100,550);
  wanted[5] = map(degree5,0,1000,300,600);

  int originalangle[6];
  int distance[6];
  
  for(int i = 0; i < 6; i++)
  {
    originalangle[i] = angle[i];
    distance[i] = wanted[i] - originalangle[i];
//    angle[i] = wanted[i];
  }

//  angle[x] = wanted[x];

  
      for(int x = 0; x < 6; x++)
      {
          angle[x] = originalangle[x] + distance[x];
//          Serial.print(angle[x]);
          pwm.setPWM(x+10,0,angle[x]);
      }
  Serial.print("ok i wil2l2");
}
