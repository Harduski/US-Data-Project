
#include <SerialTransfer.h>
#include <arduinoFFT.h>

arduinoFFT FFT = arduinoFFT(); 
SerialTransfer myTransfer;

const int num_meas = 100;
const int num_meas_k = 100;
int meas_val1[num_meas][num_meas_k];
const int samples=1024;
double sys_vol =3.3;
int res = 4096;
float fft_x[num_meas*num_meas_k];
float fft_y[num_meas*num_meas_k];
int sam_fre = 666666;
double vReal[samples];
double vImag[samples];


void setup()
{
  for (uint16_t i = 0; i < samples; i++)
  {
    vReal[i] = 0.0;
    vImag[i] = 0.0; //Imaginary part must be zeroed in case of looping to avoid wrong calculations and overflows
  }
  Serial.begin(115200);
  myTransfer.begin(Serial);
  
  int t = analogRead(0);
  ADC->ADC_MR |= 0x80; // these lines set free running mode on adc 7 (pin A0)
  ADC->ADC_CR = 2;
  ADC->ADC_CHER = 0x80;

   for (int j = 0; j < num_meas_k; j++) {
  
      for (int i = 0; i < num_meas; i++) {
      // fft_x[i+j*num_meas_k]= ((i+j*num_meas_k) * 1.0 * sam_fre / num_meas_k /num_meas);
      }
      
    }
}

void loop()
{
  fast_analog_in(num_meas, num_meas_k);
  send_meas_data(num_meas, num_meas_k);
  
  
}

void fast_analog_in(int arr_x, int arr_y){
    int a0;
  for (int j = 0; j < arr_y; j++) {

    for (int i = 0; i < arr_x; i++) {


      while ((ADC->ADC_ISR & 0x80) == 0); // wait for conversion
        a0 = ADC->ADC_CDR[7];             // read data
        meas_val1[i][j] = a0;
    }
  } 
}

void send_meas_data(int arr_x, int arr_y){
  char meas_val_str[num_meas * 5];
  String str;
  char b[5];


  for (int i = 0; i < arr_x; i++) {


    str = String(meas_val1[i][0]);

    str.toCharArray(b, 5);
    for (int j = 0; j <= 4; j++) {
      meas_val_str[i * 5 + j] = b[j];

    }




  }
  for (int k = 0; k < arr_y; k++) {
    for (int j = 0; j < 500; j = j + 5) {
      for (int h = 0; h < 4; h++) {
        myTransfer.txBuff[j + h] = meas_val_str[j + h];
      }

    }
    

    myTransfer.sendData(500);
    delay(101);
  }  
}


void feat_extr(int sam){
 
  // variable for feature extraction
  uint16_t samples = 4096;
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


  //calculate averrage value of the FFT
   for(int i =0; i<sam; i++){
    mue = mue + abs(vReal[i]); 
    
   }
   mue = mue/sam;

   //calculate stad
   for(int i =0; i<sam; i++){
    stad = (abs(vReal[i])-mue)*(abs(vReal[i])-mue)+stad;   
   }
   stad = sqrt(stad/sam);
   

   
    //calculate skew
   for(int i =0; i<sam; i++){
    skew = (abs(vReal[i])-mue)*(abs(vReal[i])-mue)*(abs(vReal[i])-mue)/stad+skew;   
   }
   skew = skew/sam;

   //calculate kurtolios
   for(int i =0; i<sam; i++){
    kurt = (abs(vReal[i])-mue)*(abs(vReal[i])-mue)*(abs(vReal[i])-mue)*(abs(vReal[i])-mue)/stad+skew;              
   }
   kurt = kurt/sam;
   
    //centerfrequency
  //  x = FFT.MajorPeak(vReal, sam, samplingFrequency);

    Serial.println(mue, 6);Serial.println(stad,6); Serial.println(skew,6);  Serial.println(kurt,6);

   //calculate bandwith and center frequency
   for(int i =0; i<sam; i++){
    if(vReal[i]>max_fft){
      max_fft=vReal[i];
      max_fft_id=i;
     
    }
    
   }
   for(int j =max_fft_id; j<sam; j++){
    
     if(vReal[j] <max_fft/2)
      upper_band = j;
      if(vReal[j] <max_fft/3){
        upper_band_2 = j;
        break;
     }
   }
     for(int h =max_fft_id; h>1; h--){
     
      if(vReal[h] <max_fft/2)
      under_band =h;
      if(vReal[h] <max_fft/3){
        under_band_2 = h;
        break;
     
    }
   }
}


   void fft_all(int arr_x, int arr_y){
    uint16_t samples = 4096;
    uint8_t y = 0;
    uint8_t x = 0;
    uint8_t fft_run = 4;
    uint16_t fft_count=0;

    for (uint16_t i = 0; i < samples; i++)
  {
    vReal[i] = 0.0;
    vImag[i] = 0.0; //Imaginary part must be zeroed in case of looping to avoid wrong calculations and overflows
  }
  for ( int con = 0; con < fft_run; con++){
    for (int j = y; j < arr_y; j++) {
  
      for ( int i = x; i < arr_x; i++) {
        if (fft_count == 4096){
          y=j;
          x=i;
          fft_count = 0;
          goto jump;
          
        }
        vReal[fft_count]=  meas_val1[i][j]*sys_vol/res;
        vImag[fft_count] =0;
        fft_count++;
        
              
        
      }
    }
    jump:
    FFT.Compute(vReal, vImag,  samples, FFT_FORWARD); 
    FFT.ComplexToMagnitude(vReal, vImag, samples); 
    for (int j = con*y-y; j < arr_y; j++) {
      for (int i = con*x-x; i < arr_x; i++){
         if (fft_count == 4096){
          fft_count = 0;
          goto jump1;
          
        }
        fft_y[i+j*arr_y]=vReal[fft_count];
       
      }
    
    }
    jump1:
    fft_count = 0;
  }
 }
 
