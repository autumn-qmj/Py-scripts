//*function_start*/
//*function_location#fsl_clock.c
//*function_depend#uint32_t CLOCK_GetFroFreq(void)
//*function_status#ignore
//*function_name#
uint32_t CLOCK_GetFroFreq(void)
//*function_name_new#
uint32_t CLOCK_GetFROFreq(void)
//*function_body_old#
    return s_Fro_Osc_Freq/2;
//*function_body_new#
    return s_Fro_Osc_Freq / 2U;
//*function_end

//*function_start*/
//*function_location#fsl_clock.c
//*function_depend#uint32_t CLOCK_GetFroFreq(void)
//*function_status#new
//*function_body_new#
uint32_t test(void)
{
    /* test function */
}
//*function_end