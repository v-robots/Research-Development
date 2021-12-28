/*
This code is for controlling servo robot arm using inverse kinematics
A pathfinder project for Hibot-3
*/ 

#include <VarSpeedServo.h>//Library for slow motion servo controls

//initializing objects
VarSpeedServo srs;//shoulder rotation servo
VarSpeedServo sys;//shoulder yaw servo


int speeds = 15;
float arm = 17.2;
float fore_arm = 9;


void setup()
{
    Serial.begin(9600);
    //servo.attach(pin,min_value,max_value)
    srs.attach(9,0,180);
    sys.attach(8,0,180);
    pos();
}

void loop()
{
    
   if (Serial.available() > 0){
    Serial.println("reading");
    String values = Serial.readString();
    String x = getValue(values,',',0);
    String y = getValue(values,',',1);
    int shoulder = x.toInt();
    int shoulder_2 = y.toInt();
    Serial.println(shoulder,shoulder_2);
    srs.slowmove(shoulder,speeds);
    sys.slowmove(shoulder_2,speeds);
}

}

void pos(){
    srs.slowmove(60,speeds);
    sys.slowmove(50,speeds);
}


String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
