/***********************************************************************************************************************
 * File Name: system_xc2xx_cm4.c
 *
 * Description: Implementation of SYSTEM
 *
 *
 * (c) Copyright 2024 XIAOHUA SEMICONDUCTOR CO., LTD. All rights reserved.
 *
 * This software is licensed by XHSC PLATFORM SOFTWARE LICENSE AGREEMENT (the "License"). By downloading, installing, or
 * using the Software, you indicate that you accept the terms of the License, and you acknowledge that you have the
 * authority, for yourself or on behalf of your company, to bind your company to these terms. If you do not agree to all
 * of the terms of this License, you should not download or install the Software.
 *
 **********************************************************************************************************************/


/**
 *   @file       system_xc2xx_cm4.c
 *   @version    1.0.0
 *   @brief      system_xc2xx_cm7 Source File
 *   @addtogroup system_driver
 *   @{
 */



#ifdef __cplusplus
extern "C" {
#endif

/***********************************************************************************************************************
 *  INCLUDES
 **********************************************************************************************************************/
#include "system_xc2xx_cm4.h"

/***********************************************************************************************************************
 *  DEFINES & MACROS
 **********************************************************************************************************************/

/***********************************************************************************************************************
 *  EXTERN
 **********************************************************************************************************************/

/***********************************************************************************************************************
 *  LOCAL TYPEDEFS
 **********************************************************************************************************************/

/***********************************************************************************************************************
 *  LOCAL CONSTANTS
 **********************************************************************************************************************/

/***********************************************************************************************************************
 *  LOCAL VARIABLES
 **********************************************************************************************************************/

/***********************************************************************************************************************
 *  GLOBAL VARIABLES
 **********************************************************************************************************************/

/***********************************************************************************************************************
 *  LOCAL FUNCTION PROTOTYPES
 **********************************************************************************************************************/

/***********************************************************************************************************************
 *  LOCAL FUNCTION
 **********************************************************************************************************************/

/***********************************************************************************************************************
 * GLOBAL FUNCTION
 **********************************************************************************************************************/
/**
 * @brief NMI IRQ handler
 * @param[in]  void
 *
 * @return     void
 */

void NMI_Handler(void)
{
    while(1){;};
}

/**
 * @brief HardFault IRQ handler
 * @param[in]  void
 *
 * @return     void
 */

void HardFault_Handler(void)
{
    while(1){;};
}

/**
 * @brief MemManage IRQ handler
 * @param[in]  void
 *
 * @return     void
 */

void MemManage_Handler(void)
{
    while(1){;};
}

/**
 * @brief BusFault IRQ handler
 * @param[in]  void
 *
 * @return     void
 */

void BusFault_Handler(void)
{
    while(1){;};
}

/**
 * @brief UsageFault IRQ handler
 * @param[in]  void
 *
 * @return     void
 */

void UsageFault_Handler(void)
{
    while(1){;};
}

/**
 * @brief DebugMon IRQ handler
 * @param[in]  void
 *
 * @return     void
 */

void DebugMon_Handler(void)
{
    while(1){;};
}

/**
 * @brief PendSV IRQ handler
 * @param[in]  void
 *
 * @return     void
 */

void PendSV_Handler(void)
{
    while(1){;};
}

/**
 * @brief SysTick IRQ handler
 * @param[in]  void
 *
 * @return     void
 */

void SysTick_Handler(void)
{
    while(1){;};
}

/**
 * @brief undefined IRQ handler
 * @param[in]  void
 *
 * @return     void
 */

void UnKnown_Handler(void)
{
   while(1){;};
}


/**
 * @brief SVC IRQ handler
 * @param[in]  void
 *
 * @return     void
 */

void SVC_Handler(void)
{
    while(1){;};
}


void SystemInit(void)
{

}
#ifdef __cplusplus
}
#endif
