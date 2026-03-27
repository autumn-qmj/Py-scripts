;/***********************************************************************************************************************
; * Project Name: XC2XX ADL
; * File Name: startup.s
; *
; * Description: Implementation of the Start-up
; *              Compiler:                HighTec
; *
; *
; * Copyright (c) 2023 - 2025 Xiaohua Semiconductor Co., Ltd.
; *
; * All rights reserved.
; *
; * This software is licensed by XHSC PLATFORM SOFTWARE LICENSE AGREEMENT (the "License"). By downloading, installing, or
; * using the Software, you indicate that you accept the terms of the License, and you acknowledge that you have the
; * authority, for yourself or on behalf of your company, to bind your company to these terms. If you do not agree to all
; * of the terms of this License, you should not download or install the Software.
; *
; **********************************************************************************************************************/

    .syntax unified
    .arch armv7-m

.section .init_table : CONST : ROOT (2)
  .long __VECTORTABLE_START
  .long 0  /* __INIT_VECTORTABLE_START - vector table in ITCM ROM */
  .long 0  /* __INIT_VECTORTABLE_END - vector table in ITCM ROM */
  .long __MCALTEXTFAST_START
  .long __INIT_MCALTEXTFAST_START
  .long __INIT_MCALTEXTFAST_END
  .long __MCALDATAFAST_START
  .long __INIT_MCALDATAFAST_START
  .long __INIT_MCALDATAFAST_END
  .long __DATA_START
  .long __INIT_DATA_START
  .long __INIT_DATA_END
  .long __DATA_NOCACHE_START
  .long __INIT_DATA_NOCACHE_START
  .long __INIT_DATA_NOCACHE_END
  .long __DATA_SHAREABLE_START
  .long __INIT_DATA_SHAREABLE_START
  .long __INIT_DATA_SHAREABLE_END
.section .zero_table : CONST : ROOT (2)
  .long __BSS_START
  .long __BSS_END
  .long __BSS_NOCACHE_START
  .long __BSS_NOCACHE_END
  .long __BSS_SHAREABLE_START
  .long __BSS_SHAREABLE_END
  .long __BSS_MCALBSSFAST_START
  .long __BSS_MCALBSSFAST_END

;/* Section vector table */
.section .intvec : CODE : ROOT (2)
.align 2
.thumb
.globl __STACK_DTCM_START
.type Reset_Handler, %function
.globl Reset_Handler
.globl VTABLE
.globl NMI_Handler
.globl HardFault_Handler
.globl MemManage_Handler
.globl BusFault_Handler
.globl UsageFault_Handler
.globl UnKnown_IRQhandler
.globl SVC_Handler
.globl DebugMon_Handler
.globl PendSV_Handler
.globl SysTick_Handler

VTABLE:
    .long  __STACK_DTCM_START
    .long Reset_Handler
    .long NMI_Handler
    .long HardFault_Handler
    .long MemManage_Handler
    .long BusFault_Handler
    .long UsageFault_Handler
    .long 0
    .long 0
    .long 0
    .long 0
    .long SVC_Handler
    .long DebugMon_Handler
    .long 0
    .long PendSV_Handler
    .long SysTick_Handler
    ;/* Interrupts */
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .long UnKnown_IRQhandler
    .size VTABLE, . - VTABLE
/***********************************************************************************************************************
/* Before the MCU driver can be initialized, a basic initialization of the MCU has to be executed. This MCU specific 
/* initialization is typically executed in a start-up code.The start-up code of the MCU shall be executed after power up 
/* and any kind of microcontroller reset. It shall perform very basic and microcontroller specific start-up initialization
/* and shall be kept short because the MCU clock and PLL are not yet initialized. The start-up code shall cover MCU specific
/* initialization which is not part of other MCU services or other MCAL drivers. The following description summarizes the  
/* basic functionality to be included in the start-up code. It is listed for guidance because some functionality might not 
/* be supported in all MCU.
/***********************************************************************************************************************/

.section .startup : CODE : ROOT (2)
.thumb
.set VTOR_REG, 0xE000ED08
.set COREID_REG, 0x4001FC00
.set RAMINITEN_REG, 0x40028000
.set RAMINITCTRL_REG, 0x40028004
.set RAMINITSTATUS_REG, 0x40028008
.set SRAMINIT_EN,  0x07
.set DTCMINIT_EN,  0xA0
.set ITCMINIT_EN,  0x50
.set SRAMINIT_START,  0x07
.set DTCMINIT_START,  0xA0
.set ITCMINIT_START,  0x50
.set SRAMINIT_STATUS,  0x07
.set DTCMINIT_STATUS,  0xA0
.set ITCMINIT_STATUS,  0x50

.thumb 
.thumb_func
.globl Reset_Handler
.globl _start
_start:
Reset_Handler:
                CPSID   I

/***********************************************************************************************************************
/* Reset core register
/***********************************************************************************************************************/
                BL ClearGenericRegister

/***********************************************************************************************************************
/* Set vtor register
/***********************************************************************************************************************/
                BL SetUpVtorRegister

/***********************************************************************************************************************
/* Set stack register
/***********************************************************************************************************************/
                BL SetStack

/***********************************************************************************************************************
/* Clear Ram
/***********************************************************************************************************************/
                BL ClearRAM

/***********************************************************************************************************************
/* Clear DTCM
/***********************************************************************************************************************/
                BL ClearDTCM

/***********************************************************************************************************************
/* Clear ITCM
/***********************************************************************************************************************/
                BL ClearITCM

/***********************************************************************************************************************
/* Copy initialized data from Rom to Ram
/***********************************************************************************************************************/
                BL InitData

/***********************************************************************************************************************
/* System Init
/***********************************************************************************************************************/
                BL SystemInit

/***********************************************************************************************************************
/* Call Main Routine
/***********************************************************************************************************************/
_MAIN:
  CPSIE i
  BL main

/***********************************************************************************************************************
/* End Of Main
/***********************************************************************************************************************/
.globl _end_of_main
_end_of_main:
    b .

/***********************************************************************************************************************
/* Function defination
/***********************************************************************************************************************/
/* Clear Generic Register */
ClearGenericRegister:
    MOV     R0,  #0
    MOV     R1,  #0
    MOV     R2,  #0
    MOV     R3,  #0
    MOV     R4,  #0
    MOV     R5,  #0
    MOV     R6,  #0
    MOV     R7,  #0
    MOV     R8,  #0
    MOV     R9,  #0
    MOV     R10, #0
    MOV     R11, #0
    MOV     R12, #0
    MOV     PC,  LR

/* Set Up Vtor Register */
SetUpVtorRegister:
    LDR     R0, =VTOR_REG
    LDR     R1, =__VECTORTABLE_START
    STR     R1, [R0]
    MOV     PC, LR

/* Set Up Set Stack */
SetStack:
    LDR     r0, =__STACK_DTCM_START
    MSR     MSP, r0
EndSetStack:
    MOV     PC, LR

/* Clear RAM */
ClearRAM:
    LDR     R0, =COREID_REG
    LDR     R1, [R0]
    MOV     R0, #0
    CMP     R1, R0
    BNE     ClearRAM_End
    LDR     R0, =__RAM_INIT
    CMP     R0, #0
    /* Skip if __RAM_INIT is not set */
    BEQ     ClearRAM_End
SetRAMInit:   
    LDR     R0, =RAMINITEN_REG
    LDR     R1, =SRAMINIT_EN
    STR     R1, [R0]
    LDR     R0, =RAMINITCTRL_REG
    LDR     R1, =SRAMINIT_START
    STR     R1, [R0]
GetRAMInitStatus:    
    LDR     R0, =RAMINITSTATUS_REG
    LDR     R1, [R0]
    LDR     R0, =SRAMINIT_STATUS
    CMP     R1, R0
    BNE     GetRAMInitStatus
    LDR     R0, =RAMINITEN_REG
    MOV     R1, #0
    STR     R1, [R0]
ClearRAM_End:
    MOV     PC, LR

/* Clear DTCM */
ClearDTCM:
    LDR     R0, =COREID_REG
    LDR     R1, [R0]
    MOV     R0, #0
    CMP     R1, R0
    BNE     ClearDTCM_End
    LDR     R0, =__RAM_INIT
    CMP     R0, #0
    /* Skip if __RAM_INIT is not set */
    BEQ     ClearDTCM_End
SetDTCMInit:   
    LDR     R0, =RAMINITEN_REG
    LDR     R1, =DTCMINIT_EN
    STR     R1, [R0]
    LDR     R0, =RAMINITCTRL_REG
    LDR     R1, =DTCMINIT_START    
    STR     R1, [R0]
GetDCTMInitStatus:    
    LDR     R0, =RAMINITSTATUS_REG
    LDR     R1, [R0]
    LDR     R0, =DTCMINIT_STATUS
    CMP     R1, R0
    BNE     GetDCTMInitStatus
    LDR     R0, =RAMINITEN_REG
    MOV     R1, #0
    STR     R1, [R0]    
ClearDTCM_End:
    MOV     PC, LR

/* Clear ITCM */
ClearITCM:
    LDR     R0, =COREID_REG
    LDR     R1, [R0]
    MOV     R0, #0
    CMP     R1, R0
    BNE     ClearITCM_End
    LDR     R0, =__RAM_INIT
    CMP     R0, #0
    /* Skip if __RAM_INIT is not set */
    BEQ     ClearITCM_End
SetITCMInit:   
    LDR     R0, =RAMINITEN_REG
    LDR     R1, =ITCMINIT_EN
    STR     R1, [R0]
    LDR     R0, =RAMINITCTRL_REG
    LDR     R1, =ITCMINIT_START
    STR     R1, [R0]
GetITCMInitStatus:   
    LDR     R0, =RAMINITSTATUS_REG
    LDR     R1, [R0]
    LDR     R0, =ITCMINIT_STATUS
    CMP     R1, R0
    BNE     GetITCMInitStatus
    LDR     R0, =RAMINITEN_REG
    MOV     R1, #0
    STR     R1, [R0]    
ClearITCM_End:
    MOV     PC, LR

/* Init Data */
InitData:
    LDR     R0, =__INIT_TABLE
    LDR     R6, =__INIT_TABLE_END
    SUBS    R5, R6, R0
    ADDS    R5, R5, #12
SetaddRegionData:
    SUBS    R5, R5, #12
    CMP     R5, #0
    BEQ     InitData_Loop_End
    LDR     R1, [R0]
    LDR     R2, [R0, #4]
    LDR     R3, [R0, #8]
    ADDS    R0, R0, #12
    SUBS    R4, R3, R2
    CMP     R4, #0
    BEQ     SetaddRegionData
    LDR     R7, =COREID_REG
    LDR     R8, [R7]
    LDR     R7, =LINKER_ID
    CMP     R8, R7
    BEQ     CopyDataRomtoRamTcm
/* Copy data from rom to Dtcm/Itcm in core1 
   for one image project including 2 cores */
CopyDataRomtoCore1Itcm:
    LDR     R7, =__INIT_ITCM_START
    LDR     R8, =__INIT_ITCM_END
    CMP     R1, R7
    BLO     CopyDataRomtoCore1Dtcm
    CMP     R1, R8
    BHI     CopyDataRomtoCore1Dtcm
    B       CopyDataRomtoRamTcm
CopyDataRomtoCore1Dtcm:
    LDR     R7, =__INIT_DTCM_START
    LDR     R8, =__INIT_DTCM_END
    CMP     R1, R7
    BLO     InitData_Loop_End
    CMP     R1, R8
    BHI     InitData_Loop_End
CopyDataRomtoRamTcm:
    LDRB    R4, [R2]
    STRB    R4, [R1]
    ADDS    R1, R1, #1
    ADDS    R2, R2, #1
    CMP     R2, R3
    BEQ     SetaddRegionData
    B       CopyDataRomtoRamTcm
InitData_Loop_End:
    MOV  PC, LR

/* Clear Bss */
/* BSS has been cleard in ClearRAM, so this can be cancelled to reduce time consumption */
/*
ClearBss:
    LDR     R0, =COREID_REG
    LDR     R1, [R0]
    LDR     R0, =LINKER_ID
    CMP     R1, R0
    BEQ     SetRegionBss
    B       ClearBss_Loop_End
SetRegionBss:
    LDR     R0, =__ZERO_TABLE
    LDR     R6, =__ZERO_TABLE_END
    SUBS    R5, R6, R0
    ADDS    R5, R5, #8
SetaddRegionBss:
    SUBS    R5, R5, #8
    CMP     R5, #0
    BEQ     ClearBss_Loop_End
    LDR     R1, [R0]
    LDR     R2, [R0, #4]
    ADDS    R0, R0, #8
    SUBS    R4, R2, R1
    CMP     R4, #0
    BEQ     SetaddRegionBss
    LDR     R7, =COREID_REG
    LDR     R8, [R7]
    LDR     R7, =LINKER_ID
    CMP     R8, R7
    BEQ     EraseBss
*/
/* Clear Bss for Dtcm/Itcm in core1
   for one image project including 2 cores */
/* 
EraseBssCore1Itcm:
    LDR     R7, =__INIT_ITCM_START
    LDR     R8, =__INIT_ITCM_END
    CMP     R1, R7
    BLO     EraseBssCore1Dtcm
    CMP     R1, R8
    BHI     EraseBssCore1Dtcm
    B       EraseBss
EraseBssCore1Dtcm:
    LDR     R7, =__INIT_DTCM_START
    LDR     R8, =__INIT_DTCM_END
    CMP     R1, R7
    BLO     ClearBss_Loop_End
    CMP     R1, R8
    BHI     ClearBss_Loop_End
EraseBss:
    MOVS    R4, #0
    STRB    R4, [R1]
    ADDS    R1, R1, #1
    CMP     R2, R1
    BEQ     SetaddRegionBss
    B       EraseBss
ClearBss_Loop_End:
    MOV     PC, LR 
*/

.align 4
.ltorg
