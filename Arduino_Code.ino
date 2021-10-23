char c = ' ';
int length = 30;
char buffer [31];
char termChar = 10;  //new line/line feed/'\n'

byte index = 0;
boolean haveNewData = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.print("Microproccessor is ready!");
}

void loop() {
  // put your main code here, to run repeatedly:
  readSerial();
    if ( haveNewData )
    {
      haveNewData = false;
      //check for the magic message, return magic answer
      if (strcmp(buffer, "magic_message!") == 0)
      {
        Serial.print("message_received!\n");
      }
    }
}

void readSerial()
{
    if (Serial.available())
    {
       c = Serial.read();
       if (c != termChar)
       {
         buffer[index] = c;
         index = index + 1;
       }
       else
       {
         buffer[index] = '\0';
         index = 0;
         haveNewData = true;
       }
    }
}