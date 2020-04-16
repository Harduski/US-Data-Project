#include <SerialTransfer.h>
#include <arduinoFFT.h>

arduinoFFT FFT = arduinoFFT(); 
SerialTransfer myTransfer;

const int num_meas = 100;
const int num_meas_k = 200;
int meas_val1[num_meas][num_meas_k];
int sampels;
double sys_vol =3.3;
int res = 4096;
float fft_x[num_meas*num_meas_k];
float fft_y[num_meas*num_meas_k];
int sam_fre = 666666;

void setup() {
  // put your setup code here, to run once:
 Serial.begin(115200);
  myTransfer.begin(Serial);
  
  int t = analogRead(0);
  ADC->ADC_MR |= 0x80; // these lines set free running mode on adc 7 (pin A0)
  ADC->ADC_CR = 2;
  ADC->ADC_CHER = 0x80;

   for (int j = 0; j < num_meas_k; j++) {
  
     
       fft_x[j]= ((j) * 1.0 );
      
      
}
}

void loop() {
  // put your main code here, to run repeatedly:

}
