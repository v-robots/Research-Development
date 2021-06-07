/*
This code is for controlling servo robot arm using inverse kinematics
A pathfinder project for Hibot-3
*/ 

#include <VarSpeedServo.h>//Library for slow motion servo controls

//initializing objects
VarSpeedServo srs;//shoulder rotation servo
VarSpeedServo sys;//shoulder yaw servo
VarSpeedServo es;//elbow servo

int speeds = 15;
float arm = 17.2;
float fore_arm = 9;


void setup()
{
    Serial.begin(9600);
    //servo.attach(pin,min_value,max_value)
    srs.attach(9,0,180);
    sys.attach(8,0,180);
    es.attach(10,0,180);
    pos();
}

void loop()
{
    
   if (Serial.available() > 0){
    Serial.println("reading");
    String values = Serial.readString();
    String x = getValue(values,',',0);
    String y = getValue(values,',',1);
    String width = getValue(values,',',2);
    String height = getValue(values,',',3);
    int shoulder = map(x.toInt(),0,200,0,180);
    Serial.println(shoulder);
    srs.slowmove(shoulder,speeds);
}

}

void pos(){
    srs.slowmove(60,speeds);
    sys.slowmove(50,speeds);
    es.slowmove(180,speeds);
}

float inverse_kinematics(int y,int x){
    float num = sq(x) + sq(y) - sq(arm) - sq(fore_arm);
    float den = 2*arm*fore_arm;
    float q2 = (-1*(acos(num/den)) * 4068) / 71;
    float deg2 = -180 - q2;
    float q1_f = atan(y/x);
    float q1_s_num =fore_arm*sin(q2);
    float q1_s_den = (arm + fore_arm*cos(q2));
    float q1_s = atan(q1_s_num/q1_s_den);
    float q1 = q1_f + q1_s;
    q1 = (q1* 4068) / 71;
    float deg1 = q1 + 50;
    deg2 = -deg2;
    sys.slowmove(deg1,speeds);
    es.slowmove(deg2,speeds);
    Serial.println(deg1);
    Serial.println(deg2);
    return 0;
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
