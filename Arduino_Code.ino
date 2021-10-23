#define SERVO_1_PIN 9
#include <Servo.h>

#define laser_pin 2

// 0 degrees = 600
// 180 degrees = 2200 //differs per servo, can be 2400

class Motor {
  private:
    byte pin;
  public:
    int minimum = 600;
    int maximum = 2200;
    int currentPos = 1500; //current position of the servo, initialize middle (1500)
    int newPos; //new target position of the servo
    int distance; //distance between currentPos and newPos (on moment of calculation)
    int velocity; //speed
    int stepSize; //size of steps to take
    int nextStep; //newPos + stepSize

    void init(byte pin) {
      this->pin = pin;
      pinMode (pin, OUTPUT);
    }

    void coordinateGenerator() {
      int randNumber = random(0, 1);
      if (randNumber == 0 && currentPos * 1.1 < (maximum)) {
        int randMin = currentPos * (1.1);
        int randMax = maximum;
        newPos = random(randMin, randMax);
      }
      else {
        int randMin = minimum;
        int randMax = currentPos * (0.8);
        newPos = random(randMin, randMax);
      }
    }

    void speedGenerator() {
      int randMin = 10;
      int randMax = 100;
      velocity = random(randMin, randMax);
      int analog = analogRead(0);
      if (analog < 10) {
        analog = 10;
      }
      Serial.println((log(analog)));
    }

    void calculate() {
      distance = abs(currentPos - newPos);
      int integer = 1000 - analogRead(0);
      if (integer < 10) {
        integer = 10;
      }
      stepSize = distance / (integer * 0.95 / 10);
    }

    int motorMove() {
      if (currentPos > newPos) {
        currentPos = currentPos - stepSize;
      }
      if (currentPos < newPos) {
        currentPos = currentPos + stepSize;
      }
      //move servo to new position
      return currentPos;
    }

    void printStats() {
      Serial.println();
      Serial.print("servo pin: ");
      Serial.println(pin);
      Serial.print("currentPos: ");
      Serial.println(currentPos);
      Serial.print("newPos: ");
      Serial.println(newPos);
      Serial.print("velocity: ");
      Serial.println(velocity);
      Serial.print("stepSize: ");
      Serial.println(stepSize);
      Serial.print("nextStep: ");
      Serial.println(nextStep);
      Serial.println();
    }
};

Servo servo1;
Servo servo2;
Motor motor1;
Motor motor2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  motor1.init(9);
  motor1.minimum = 1200;
  motor1.maximum = 1800;
  motor1.coordinateGenerator();
  motor1.speedGenerator();
  motor1.printStats();

  motor2.init(10);
  motor2.minimum = 700;
  motor2.maximum = 1000;
  motor2.coordinateGenerator();
  motor2.speedGenerator();
  motor2.printStats();

  servo1.attach(9);
  servo2.attach(10);

  pinMode(laser_pin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  motor1.coordinateGenerator();
  motor2.coordinateGenerator();
  motor1.speedGenerator();
  motor2.speedGenerator();
  motor1.calculate();
  motor2.calculate();
  motor1.motorMove();
  motor2.motorMove();
  //  motor1.printStats();
  //  motor2.printStats();

  while ((motor1.newPos - motor1.stepSize) >= motor1.currentPos || motor1.currentPos >= (motor1.newPos + motor1.stepSize) | (motor2.newPos - motor2.stepSize) >= motor2.currentPos || motor2.currentPos >= (motor2.newPos + motor2.stepSize)) {
    servo1.writeMicroseconds(motor1.motorMove());
    //    Serial.println(motor1.currentPos);
    servo2.writeMicroseconds(motor2.motorMove());
    //    Serial.println(motor2.currentPos);
    digitalWrite(laser_pin, HIGH);
    delay(5);
      digitalWrite(laser_pin, LOW);
    delay(5);

  }
}