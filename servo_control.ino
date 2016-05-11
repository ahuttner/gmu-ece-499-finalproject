#define XWheel 1
#define YWheel 2
#define ZWheel 3

char i = 's';
int XSpeed = 0;
int YSpeed = 0;

Dynamixel Dxl(1);

void setup(){
  Dxl.begin(3);
  Dxl.wheelMode(XWheel);
  Dxl.wheelMode(YWheel);
  Dxl.jointMode(ZWheel);
  SerialUSB.attachInterrupt(usbInterrupt);
}

void usbInterrupt(byte* buffer, byte nCount){
  
  i =(char)buffer[0];  
    SerialUSB.println(i);
    
  switch (i) {
    //Stop
    case 's':
      XSpeed = 0;
      YSpeed = 0;
      SerialUSB.print("XSpeed:");
      SerialUSB.println(XSpeed);
      SerialUSB.print("YSpeed:");
      SerialUSB.println(YSpeed);
      break;
      
    //South
    case 'x':
      XSpeed = 0;
      YSpeed = 400;
      SerialUSB.print("XSpeed:");
      SerialUSB.println(XSpeed);
      SerialUSB.print("YSpeed:");
      SerialUSB.println(YSpeed);
      break;
      
      //North
    case 'w':
      XSpeed = 0;
      YSpeed = 400 | 0x400;
      SerialUSB.print("XSpeed:");
      SerialUSB.println(XSpeed);
      SerialUSB.print("YSpeed:");
      SerialUSB.println(YSpeed);
      break;
      
      //East
    case 'd':
      XSpeed = 400;
      YSpeed = 0;
      SerialUSB.print("XSpeed:");
      SerialUSB.println(XSpeed);
      SerialUSB.print("YSpeed:");
      SerialUSB.println(YSpeed);
      break;
      
      //West
    case 'a':
      LeftSpeed = 400 | 0x400;
      RightSpeed = 0;
      SerialUSB.print("XSpeed:");
      SerialUSB.println(XSpeed);
      SerialUSB.print("YSpeed:");
      SerialUSB.println(YSpeed);
      break;

      //North East
    case 'e':
      XSpeed = 400;
      YSpeed = 400 | 0x400;
      SerialUSB.print("XSpeed:");
      SerialUSB.println(XSpeed);
      SerialUSB.print("YSpeed:");
      SerialUSB.println(YSpeed);
      break;
      
      //South East
    case 'c':
      XSpeed = 400;
      YSpeed = 400;
      SerialUSB.print("XSpeed:");
      SerialUSB.println(XSpeed);
      SerialUSB.print("YSpeed:");
      SerialUSB.println(YSpeed);
      break;
      
      //North West
    case 'q':
      XSpeed = 400 | 0x400;
      YSpeed = 400 | 0x400;
      SerialUSB.print("XSpeed:");
      SerialUSB.println(XSpeed);
      SerialUSB.print("YSpeed:");
      SerialUSB.println(YSpeed);
      break;
      
      //South West
    case 'z':
      XSpeed = 400 | 0x400;
      YSpeed = 400;
      SerialUSB.print("XSpeed:");
      SerialUSB.println(XSpeed);
      SerialUSB.print("YSpeed:");
      SerialUSB.println(YSpeed);
      break;
      
      //Raise
    case 'r':
      Dxl.goalPosition(ZWheel, 150);
      break;
    
      //Lower
    case 'v':
      Dxl.goalPosition(ZWheel, 0);
      break;
      
    //Default to stop
    default:
      XSpeed = 0;
      YSpeed = 0;
      Dxl.goalPosition(ZWheel, 150);
      SerialUSB.print("XSpeed:");
      SerialUSB.println(XSpeed);
      SerialUSB.print("YSpeed:");
      SerialUSB.println(YSpeed);
      break;
  }
}

void loop(){
  delay(100);
  Dxl.goalSpeed(XWheel,XSpeed);
  Dxl.goalSpeed(YWheel,YSpeed);  
}

