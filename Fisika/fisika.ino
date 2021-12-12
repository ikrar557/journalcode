#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);
 
int num_Measure = 128 ; // Set the number of measurements   
int pinSignal = A0; // pin connected to pin O module sound sensor  
int redLed = 5; 
long Sound_signal;    // Store the value read Sound Sensor   
long sum = 0 ; // Store the total value of n measurements   
long level = 0 ; // Store the average value   
//int soundlow = 100;
//int soundmedium = 200;
int data;

void setup ()  
{   
  pinMode (pinSignal, INPUT); // Set the signal pin as input   
  Serial.begin (9600); 
  lcd.clear();
  lcd.begin(16,2); 
}  
   
void loop ()  
{  
  // Performs 128 signal readings   
  for ( int i = 0 ; i <num_Measure; i ++)  
  {  
   Sound_signal = analogRead (pinSignal);  
    sum =sum + Sound_signal;  
  }  
 
  level = sum / num_Measure; // Calculate the average value   
  data = (level+83.2073) / 11;
  lcd.setCursor(6,0);
  lcd.print(data);
  lcd.print("dB");

  
  if(data > 50)
  {
    lcd.setCursor(2,2);
    lcd.print("Quiet Office");    
  }
  
  if(data > 60)
  {
    lcd.setCursor(2,2);
    lcd.print("Conversation");    
  }

   if(data > 70)
  {
    lcd.setCursor(2,2);
    lcd.print("Busy Traffic");    
  }

  sum = 0 ; // Reset the sum of the measurement values  
  delay(315 );
  lcd.clear();
}
