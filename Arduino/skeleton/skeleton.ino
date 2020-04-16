#include <SerialTransfer.h>
#include <arduinoFFT.h>

arduinoFFT FFT = arduinoFFT(); 
SerialTransfer myTransfer;

const int num_meas = 4096;
uint16_t meas_val1[num_meas];

const uint16_t samples=1024;
float sys_vol =3.3;
uint16_t res = 4096;
float fft_y1[num_meas];
double fft_in_x[samples];
double fft_in_y[samples];
uint16_t sam_fre = 666666;

double stad=0.0;
double skew = 0.0;
double kurt = 0.0;
double mue = 0.0;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);
  myTransfer.begin(Serial);
  
  uint16_t t = analogRead(0);
  ADC->ADC_MR |= 0x80; // these lines set free running mode on adc 7 (pin A0)
  ADC->ADC_CR = 2;
  ADC->ADC_CHER = 0x80;

//   for (uint16_t j = 0; j < num_meas_k; j++) {
//  
//      for (uint16_t i = 0; i < num_meas; i++) {
//       fft_x[i+j*num_meas_k]= ((i+j*num_meas_k) * 1.0 * sam_fre / num_meas_k /num_meas);
//      }
//      
//      
//    }


    for (uint16_t j = 0; j < samples; j++){
      fft_in_x[j] = 0.0;
    }
    

}

void loop()
{
  
  //fast_analog_in(num_meas);
  //send_meas_data(num_meas, num_meas_k);
  //conv_fft(num_meas);

//  for(int i = 0; i<9999;i++){
//    Serial.print(fft_y[i]);
  }
  
  
}
