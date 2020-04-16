//#include <SerialTransfer.h>
#include <arduinoFFT.h>
//#include "dt_iris.h" // classi data
# include "svm_iris.h"

arduinoFFT FFT = arduinoFFT(); 
//SerialTransfer myTransfer;




    






const int32_t length = 4;
const double values[length] = { 0.0,0.0,0.0,0.0 };

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
//  myTransfer.begin(Serial);
  
  uint16_t t = analogRead(0);
  ADC->ADC_MR |= 0x80; // these lines set free running mode on adc 7 (pin A0)
  ADC->ADC_CR = 2;
  ADC->ADC_CHER = 0x80;



    for (uint16_t j = 0; j < samples; j++){
      fft_in_x[j] = 0.0;
    }
    

}

void loop()
{
  
  fast_analog_in(num_meas);
  send_meas_data(num_meas);
  conv_fft(num_meas);
  feat_extr();
  pred();

//  for(int i = 0; i<9999;i++){
//    Serial.print(fft_y[i]);
//  }
  
  
}

void fast_analog_in(uint16_t arr_y){
    uint16_t a0;
  for (uint16_t j = 0; j < arr_y; j++) {
      while ((ADC->ADC_ISR & 0x80) == 0); // wait for conversion
        a0 = ADC->ADC_CDR[7];             // read data
        meas_val1[j] = a0;
    
  } 

}

void send_meas_data(uint16_t arr_y){
  for(int i =0; i<arr_y;i++){
    Serial.print(meas_val1[i]);
    Serial.print("\t");
  }
   Serial.print(";");
}


void conv_fft(uint16_t arr_y){
  int x = num_meas/samples;
  Serial.println(x);

 
  Serial.println("init yeah");  
 for (uint16_t k = 0; k < x; k++){
 for (uint16_t j = k*samples; j < samples*(k+1); j++) {
        fft_in_y[j] = meas_val1[j+k*samples]/res*sys_vol;
   
 }
 
    Serial.print("happy fft");
    FFT.Compute(fft_in_y, fft_in_x,  samples, FFT_FORWARD); /* Compute FFT */
    FFT.ComplexToMagnitude(fft_in_y, fft_in_x, samples);
  
    for (int i = 0; i<samples; i++){
      
    
     
      Serial.print("double in float");
      fft_y1[i+k*samples]=float(fft_in_y[i]);
      
      }
      Serial.println("end of loop");
    }
}

//}



void feat_extr(){
  Serial.print("welcome to Feature");
 
  // variable for feature extraction
uint16_t sam = 4096;
double stad=0.0;
double skew = 0.0;
double kurt = 0.0;
double mue = 0.0;
double x;
double max_fft=0;
int max_fft_id=0;
int upper_band=0;
int under_band=0;  
int upper_band_2=0;
int under_band_2=0; 
int bandwith =0;


  //calculate averrage value of the FFT
   for(int i =0; i<sam; i++){
    mue = mue + abs(fft_y1[i]); 
    
   }
   mue = mue/sam;

   //calculate stad
   for(int i =0; i<sam; i++){
    stad = (abs(fft_y1[i])-mue)*(abs(fft_y1[i])-mue)+stad;   
   }
   stad = sqrt(stad/sam);
   

   
    //calculate skew
   for(int i =0; i<sam; i++){
    skew = (abs(fft_y1[i])-mue)*(abs(fft_y1[i])-mue)*(abs(fft_y1[i])-mue)/stad+skew;   
   }
   skew = skew/sam;

   //calculate kurtolios
   for(int i =0; i<sam; i++){
    kurt = (abs(fft_y1[i])-mue)*(abs(fft_y1[i])-mue)*(abs(fft_y1[i])-mue)*(abs(fft_y1[i])-mue)/stad+skew;              
   }
   kurt = kurt/sam;
   
    //centerfrequency
  //  x = FFT.MajorPeak(vReal, sam, samplingFrequency);
  

    Serial.println(mue, 6);Serial.println(stad,6); Serial.println(skew,6);  Serial.println(kurt,6);

   //calculate bandwith and center frequency
   for(int i =0; i<sam; i++){
    if(fft_y1[i]>max_fft){
    max_fft=fft_y1[i];
      max_fft_id=i;
     
    }
    
   }
   for(int j =max_fft_id; j<sam; j++){
    
     if(fft_y1[j] <max_fft/2)
      upper_band = j;
      if(fft_y1[j] <max_fft/3){
        upper_band_2 = j;
        break;
     }
   }
     for(int h =max_fft_id; h>1; h--){
     
      if(fft_y1[h] <max_fft/2)
      under_band =h;
      if(fft_y1[h] <max_fft/3){
        under_band_2 = h;
        break;
     
    }
   }
   bandwith = upperband-under_band;
   values[0] = max_fft_id;
   values[1]= bandwith;
   values[2]= skew;
   values[3]= kurt;
}

void pred(){
  
  
 }

  //const int32_t predicted_class = dt_iris_predict(values, length);
  //  const int32_t predicted_class = eml_net_predict(nn_iris,values, length);
  int predicted_class = predict(values);
  Serial.println(predicted_class);
}

}
