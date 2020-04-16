void setup() {
  Serial.begin(115200); // opens serial port, sets data rate to 9600 bps
  int t=analogRead(0);

  ADC->ADC_MR |= 0x80; // these lines set free running mode on adc 7 (pin A0)
  ADC->ADC_CR=2;
  ADC->ADC_CHER=0x80;
}

void loop() {
  int t=micros();
  int q=0;
  int a0;
  char meas_num[5];
  int meas_long = 100;
  int meas_array[meas_long];

  
  char incomingByte[4]=""; // for incoming serial data
  if (Serial.available() > 0) {
    
    // read the incoming byte:
    incomingByte = Serial.readString();
    Serial.println(incomingByte);
    
    
    if (incomingByte = '1'){
      delay(1000);
      //Serial.println("meas");
      meas_num = Serial.readString();
      Serial.println(meas_num);
      
      //incomingByte = Serial.read();
      //meas_num = incomingByte.toInt();
      for(int i=0;i<int(meas_num);i++){
        
        for(int j=0;j<meas_long;j++){
          while((ADC->ADC_ISR & 0x80)==0); // wait for conversion
          meas_array[j]=ADC->ADC_CDR[7];              // read data
          q+=a0;
          Serial.write(meas_array[j]);
          Serial.print(",");
        }
        Serial.println();
        
      }
      
    }
  

  }
 
    }
