void ADC_IrqHandler(void)
{
    // Check the ADC conversion status
    if ((adc_get_status(ADC) & ADC_ISR_DRDY) == ADC_ISR_DRDY)
    {
    // Get latest digital data value from ADC and can be used by application
        uint32_t result = adc_get_latest_value(ADC);
    }
}
void adc_setup(void)
{
    adc_init(ADC, sysclk_get_main_hz(), ADC_CLOCK, 8);
    adc_configure_timing(ADC, 0, ADC_SETTLING_TIME_3, 1);
    adc_set_resolution(ADC, ADC_MR_LOWRES_BITS_12);
    adc_enable_channel(ADC, ADC_CHANNEL_5);
    adc_enable_interrupt(ADC, ADC_IER_DRDY);
    adc_configure_trigger(ADC, ADC_TRIG_SW, 0);
}


void setup() {
  // put your setup code here, to run once:
  adc_setup();

}

void loop() {
  // put your main code here, to run repeatedly:
  adc_start()

}
