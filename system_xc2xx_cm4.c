/***********************************************************************************************************************
 * File Name: system_xc2xx_cm4.c
 *
 * Description: Implementation of SYSTEM and Startup Code
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
 *   @brief      system_xc2xx_cm4 Source File with Startup Code
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
#include <stddef.h>

/***********************************************************************************************************************
 *  DEFINES & MACROS
 **********************************************************************************************************************/
#define VTOR_REG  (*(volatile uint32_t *)0xE000ED08UL)

/***********************************************************************************************************************
 *  EXTERN
 **********************************************************************************************************************/
/* External symbols defined by linker */
extern const uint32_t __VECTORTABLE_START;
extern uint32_t __DATA_START;
extern const uint8_t __INIT_DATA_START;
extern const uint8_t __INIT_DATA_END;
extern uint32_t __BSS_START;
extern uint32_t __BSS_END;
extern uint32_t __STACK_START;

/* Forward declarations */
extern int main(void);
extern void SystemInit(void);

/***********************************************************************************************************************
 *  LOCAL TYPEDEFS
 **********************************************************************************************************************/

/* Init table structure for data initialization */
typedef struct {
    const uint32_t *src;    /* Source address in ROM */
    uint32_t *dest;         /* Destination address in RAM */
    uint32_t wlen;          /* Length in words (unused - calculated from end) */
} init_table_t;

/* Zero table structure for BSS clearing */
typedef struct {
    uint32_t *start;        /* Start address of BSS section */
    uint32_t *end;          /* End address of BSS section */
} zero_table_t;

/***********************************************************************************************************************
 *  LOCAL CONSTANTS
 **********************************************************************************************************************/

/* Init table - placed in .init_table section by linker script */
#pragma section = ".init_table"
__attribute__((section(".init_table")))
const init_table_t __INIT_TABLE[] = {
    { &__VECTORTABLE_START, NULL, 0 },  /* Vector table (not copied to RAM) */
    { NULL, (uint32_t *)&__DATA_START, 0 }  /* Data section */
};

__attribute__((section(".init_table")))
const uint8_t *__INIT_DATA_START_PTR = &__INIT_DATA_START;
__attribute__((section(".init_table")))
const uint8_t *__INIT_DATA_END_PTR = &__INIT_DATA_END;

/* Zero table - placed in .zero_table section */
#pragma section = ".zero_table"
__attribute__((section(".zero_table")))
const zero_table_t __ZERO_TABLE[] = {
    { (uint32_t *)&__BSS_START, (uint32_t *)&__BSS_END }
};

/***********************************************************************************************************************
 *  LOCAL VARIABLES
 **********************************************************************************************************************/

/***********************************************************************************************************************
 *  GLOBAL VARIABLES
 **********************************************************************************************************************/

/***********************************************************************************************************************
 *  LOCAL FUNCTION PROTOTYPES
 **********************************************************************************************************************/
static void ClearGenericRegister(void);
static void SetUpVtorRegister(void);
static void SetStack(void);
static void InitData(void);
static void ClearBss(void);

/***********************************************************************************************************************
 *  LOCAL FUNCTION
 **********************************************************************************************************************/

/***********************************************************************************************************************
 * GLOBAL FUNCTION
 **********************************************************************************************************************/

/**
 * @brief Clear all general-purpose registers
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((noinline))
static void ClearGenericRegister(void)
{
    __asm__ volatile (
        "mov  r0, #0     \n\t"
        "mov  r1, #0     \n\t"
        "mov  r2, #0     \n\t"
        "mov  r3, #0     \n\t"
        "mov  r4, #0     \n\t"
        "mov  r5, #0     \n\t"
        "mov  r6, #0     \n\t"
        "mov  r7, #0     \n\t"
        "mov  r8, #0     \n\t"
        "mov  r9, #0     \n\t"
        "mov  r10, #0    \n\t"
        "mov  r11, #0    \n\t"
        "mov  r12, #0    \n\t"
        "bx   lr         \n\t"
    );
}

/**
 * @brief Set VTOR register to point to vector table
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((noinline))
static void SetUpVtorRegister(void)
{
    VTOR_REG = (uint32_t)&__VECTORTABLE_START;
}

/**
 * @brief Set Main Stack Pointer (MSP)
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((noinline))
static void SetStack(void)
{
    __asm__ volatile (
        "ldr  r0, =__STACK_START  \n\t"
        "msr  msp, r0             \n\t"
        "bx   lr                  \n\t"
    );
}

/**
 * @brief Copy initialized data from ROM to RAM
 * @param[in]  void
 *
 * @return     void
 */
static void InitData(void)
{
    uint8_t *dest = (uint8_t *)&__DATA_START;
    const uint8_t *src = &__INIT_DATA_START;
    const uint8_t *src_end = &__INIT_DATA_END;

    /* Copy data byte by byte from ROM to RAM */
    while (src < src_end) {
        *dest++ = *src++;
    }
}

/**
 * @brief Clear BSS section (zero-initialized data)
 * @param[in]  void
 *
 * @return     void
 */
static void ClearBss(void)
{
    uint32_t *start = (uint32_t *)&__BSS_START;
    uint32_t *end = (uint32_t *)&__BSS_END;

    /* Clear BSS section word by word */
    while (start < end) {
        *start++ = 0;
    }
}

/**
 * @brief Reset Handler - Entry point for the application
 *            This is the first code executed after reset
 * @param[in]  void
 *
 * @return     void (never returns)
 */
__attribute__((section(".startup")))
void Reset_Handler(void)
{
    /* Disable interrupts */
    __asm__ volatile ("cpsid i" ::: "memory");

    /* Clear all registers */
    ClearGenericRegister();

    /* Set VTOR register */
    SetUpVtorRegister();

    /* Set stack pointer */
    SetStack();

    /* Copy initialized data from ROM to RAM */
    InitData();

    /* Clear BSS section */
    ClearBss();

    /* System initialization */
    SystemInit();

    /* Enable interrupts and call main */
    __asm__ volatile (
        "cpsie i      \n\t"
        "bl   main     \n\t"
    );

    /* Infinite loop if main returns */
    while(1) {;}
}

/**
 * @brief Default exception handler for unused IRQs
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak))
void Default_Handler(void)
{
    while(1) {;}
}

/**
 * @brief NMI IRQ handler
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak, alias("Default_Handler")))
void NMI_Handler(void);

/**
 * @brief HardFault IRQ handler
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak, alias("Default_Handler")))
void HardFault_Handler(void);

/**
 * @brief MemManage IRQ handler
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak, alias("Default_Handler")))
void MemManage_Handler(void);

/**
 * @brief BusFault IRQ handler
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak, alias("Default_Handler")))
void BusFault_Handler(void);

/**
 * @brief UsageFault IRQ handler
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak, alias("Default_Handler")))
void UsageFault_Handler(void);

/**
 * @brief DebugMon IRQ handler
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak, alias("Default_Handler")))
void DebugMon_Handler(void);

/**
 * @brief PendSV IRQ handler
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak, alias("Default_Handler")))
void PendSV_Handler(void);

/**
 * @brief SysTick IRQ handler
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak, alias("Default_Handler")))
void SysTick_Handler(void);

/**
 * @brief SVC IRQ handler
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak, alias("Default_Handler")))
void SVC_Handler(void);

/**
 * @brief undefined IRQ handler
 * @param[in]  void
 *
 * @return     void
 */
__attribute__((weak, alias("Default_Handler")))
void UnKnown_Handler(void);

/**
 * @brief System Init - called by startup code
 * @param[in] void
 *
 * @return    void
 */
void SystemInit(void)
{
    /* Add system-specific initialization here */
}

#ifdef __cplusplus
}
#endif
