//*function_support_devices#lpc8

//*function_start*/ 
//*function_location#fsl_clock.c
//*function_depend#F:void CLOCK_InitExtClkin(uint32_t clkInFreq)
//*function_status#ignore
//*function_position#in
//*function_name#
void CLOCK_InitExtClkin
//*function_paramter#
(uint32_t clkInFreq)
//*function_body_old#
    /* bypass system oscillator */
    SYSCON->SYSOSCCTRL |= SYSCON_SYSOSCCTRL_BYPASS_MASK;
//*function_body_new#
//*function_end

//*function_start*/ 
//*function_location#fsl_clock.c
//*function_depend#F:void CLOCK_InitExtClkin(uint32_t clkInFreq)
//*function_status#ignore
//*function_position#in
//*function_name#
void CLOCK_InitXtalin(uint32_t oscFreq)
//*function_body_old#
    /* remove the pull up and pull down resistors in the IOCON */
    IOCON->PIO[IOCON_INDEX_PIO0_9] &= ~IOCON_PIO_MODE_MASK;
    IOCON->PIO[IOCON_INDEX_PIO0_8] &= ~IOCON_PIO_MODE_MASK;
    /* enable the 1 bit functions for XTALIN and XTALOUT */
    SWM0->PINENABLE0 &= ~(SWM_PINENABLE0_XTALIN_MASK | SWM_PINENABLE0_XTALOUT_MASK);
//*function_body_new#
    /* remove the pull up and pull down resistors in the IOCON */
    IOCON->PIO[IOCON_INDEX_PIO0_8] &= ~IOCON_PIO_MODE_MASK;
    /* enable the 1 bit functions for XTALIN and XTALOUT */
    SWM0->PINENABLE0 &= ~SWM_PINENABLE0_XTALIN_MASK;
//*function_end
    

//*function_end

//*function_start*/
//*function_location#fsl_clock.c
//*function_depend#F:void CLOCK_InitXtalin(uint32_t oscFreq)
//*function_status#replace
//*function_position#before
//*function_body_new#
void CLOCK_InitXtalin(uint32_t xtalInFreq)
{
    volatile uint32_t i = 0U;

    /* remove the pull up and pull down resistors in the IOCON */
    IOCON->PIO[IOCON_INDEX_PIO0_8] &= ~IOCON_PIO_MODE_MASK;
    /* enable the 1 bit functions for XTALIN and XTALOUT */
    SWM0->PINENABLE0 &= ~SWM_PINENABLE0_XTALIN_MASK;

    /* system osc configure */
    SYSCON->SYSOSCCTRL |= SYSCON_SYSOSCCTRL_BYPASS_MASK;
    /* external clock select */
    SYSCON->EXTCLKSEL &= ~SYSCON_EXTCLKSEL_SEL_MASK;
    /* enable system osc power first */
    SYSCON->PDRUNCFG &= ~SYSCON_PDRUNCFG_SYSOSC_PD_MASK;

    /* software delay 500USs */
    for (i = 0U; i < 1500U; i++)
    {
        __ASM("nop");
    }

    /* record the external clock rate */
    g_Ext_Clk_Freq = xtalInFreq;
}

//*function_end

//*function_start*/
//*function_location#fsl_clock.h
//*function_depend#F:void CLOCK_InitSysOsc(uint32_t oscFreq);
//*function_status#ignore
//*function_position#end
//*function_body_new#

/*! @brief  XTALIN init function
 *  system oscillator is bypassed, sys_osc_clk is fed driectly from the XTALIN.
 *  @param xtalInFreq XTALIN frequency value
 *  @return Frequency of PLL
 */
void CLOCK_InitXtalIn(uint32_t xtalInFreq);
//*function_end