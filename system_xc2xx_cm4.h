/***********************************************************************************************************************
 * File Name: system_xc2xx_cm7.h
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
 *   @file       system_xc2xx_cm7.h
 *   @version    1.0.0
 *   @brief      system_xc2xx_cm7 Header File
 *   @addtogroup system_driver
 *   @{
 */

#ifndef SYSTEM_H
#define SYSTEM_H

#include <stdint.h>

#ifdef __cplusplus
extern "C"
{
#endif

/**
 * @brief Early platform initialization for interrupts, cache and core MPU
 * @param[in] void
 *
 * @return    void
 */

void SystemInit(void);

/**
 * @brief Reset Handler - Entry point for the application
 * @param[in] void
 *
 * @return    void (never returns)
 */
void Reset_Handler(void);

/**
 * @brief Default exception handler
 * @param[in] void
 *
 * @return    void
 */
void Default_Handler(void);


/** 
 * @brief NMI IRQ handler
 * @param[in]  void
 * 
 * @return     void
 */

void NMI_Handler(void)                  __attribute__ ((weak));

/** 
 * @brief HardFault IRQ handler
 * @param[in]  void
 * 
 * @return     void
 */

void HardFault_Handler(void)            __attribute__ ((weak));

/** 
 * @brief MemManage IRQ handler
 * @param[in]  void
 * 
 * @return     void
 */

void MemManage_Handler(void)            __attribute__ ((weak));

/** 
 * @brief BusFault IRQ handler
 * @param[in]  void
 * 
 * @return     void
 */

void BusFault_Handler(void)             __attribute__ ((weak));

/** 
 * @brief UsageFault IRQ handler
 * @param[in]  void
 * 
 * @return     void
 */

void UsageFault_Handler(void)           __attribute__ ((weak));

/** 
 * @brief DebugMon IRQ handler
 * @param[in]  void
 * 
 * @return     void
 */

void DebugMon_Handler(void)             __attribute__ ((weak));

/** 
 * @brief PendSV IRQ handler
 * @param[in]  void
 * 
 * @return     void
 */

void PendSV_Handler(void)               __attribute__ ((weak));

/** 
 * @brief SysTick IRQ handler
 * @param[in]  void
 * 
 * @return     void
 */

void SysTick_Handler(void)              __attribute__ ((weak));

/** 
 * @brief undefined IRQ handler
 * @param[in]  void
 * 
 * @return     void
 */

void UnKnown_Handler(void);


/** 
 * @brief Handle SVC handler
 * @param[in]  void
 * 
 * @return     void
 */
void SVC_Handler(void)              __attribute__ ((weak));


#ifdef __cplusplus
}
#endif

#endif /*!< SYSTEM_H */
