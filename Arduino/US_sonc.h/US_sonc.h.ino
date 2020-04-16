#ifndef US_sonic
#define US_sonic

#include <Arduino.h>
typedef struct {
  double max_fft=0;
  int max_fft_id=0;
  int upper_band=0;
  int under_band=0;  
  int upper_band_2=0;
  int under_band_2=0;
}FFT_info;
 

#endif
