; /***********************************************************************************************************************
; * Project Name: #M4_PROJECT_NAME#
; * File Name: startup_cm4.s
; *
; * Description: Implementation of the Start-up
; *              Compiler:                HighTec
; *
; *
; * Copyright #M4_COPYRIGHT#
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
  .long 0  /* __INIT_VECTORTABLE_START - not used for ROM vector table */
  .long 0  /* __INIT_VECTORTABLE_END - not used for ROM vector table */
  .long __DATA_START
  .long __INIT_DATA_START
  .long __INIT_DATA_END

.section .zero_table : CONST : ROOT (2)
  .long __BSS_START
  .long __BSS_END

;/* Vector table is now defined in LSL file */

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

.thumb

.thumb_func
.globl Reset_Handler
Reset_Handler:
.globl _start
_start:
                CPSID   I

; /***********************************************************************************************************************
; /* Reset core register
; /**********************************************************************************************************************/
                BL ClearGenericRegister

; /***********************************************************************************************************************
; /* Set vtor register
; /**********************************************************************************************************************/
                BL SetUpVtorRegister

; /***********************************************************************************************************************
; /* Set stack register
; /**********************************************************************************************************************/
                BL SetStack

; /***********************************************************************************************************************
; /* Copy initialized data from Rom to Ram
; /**********************************************************************************************************************/
                BL InitData

; /***********************************************************************************************************************
; /* Clear Bss
; /**********************************************************************************************************************/
                BL ClearBss

; /***********************************************************************************************************************
; /* System Init
; /**********************************************************************************************************************/
                BL SystemInit

; /***********************************************************************************************************************
; /* Call Main Routine
; /**********************************************************************************************************************/
_MAIN:
  CPSIE i
  BL main

; /***********************************************************************************************************************
; /* End Of Main
; /**********************************************************************************************************************/
.globl _end_of_main
_end_of_main:
    b .

; /***********************************************************************************************************************
; /* Function defination
; /**********************************************************************************************************************/
; /***********************************************************************************************************************
; /* Clear Generic Register
; /**********************************************************************************************************************/
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

; /***********************************************************************************************************************
; /* Set Up Vtor Register
; /**********************************************************************************************************************/
SetUpVtorRegister:
    LDR     R0, =VTOR_REG
    LDR     R1, =__VECTORTABLE_START
    STR     R1, [R0]
    MOV     PC, LR

; /***********************************************************************************************************************
; /* Set Up Set Stack
; /**********************************************************************************************************************/
SetStack:
    LDR     r0,  =__STACK_START
    MSR     MSP, r0
    MOV     PC, LR

; /***********************************************************************************************************************
; /* Init Data
; /**********************************************************************************************************************/
InitData:
    LDR     R0, =__INIT_TABLE
    LDR     R6, =__INIT_TABLE_END
    SUBS    R5, R6, R0
    ADDS    R5, R5, #12
SetRegionData:
    SUBS    R5, R5, #12
    CMP     R5, #0
    BEQ     InitData_Loop_End
    LDR     R1, [R0]
    LDR     R2, [R0, #4]
    LDR     R3, [R0, #8]
    ADDS    R0, R0, #12
    SUBS    R4, R3, R2
    CMP     R4, #0
    BEQ     SetRegionData
; /***********************************************************************************************************************
; /* Copy data from rom to Dtcm/Itcm in core1
; /* for one image project including 2 cores
; /**********************************************************************************************************************/
CopyDataRomtoRam:
    LDRB    R4, [R2]
    STRB    R4, [R1]
    ADDS    R1, R1, #1
    ADDS    R2, R2, #1
    CMP     R2, R3
    BEQ     SetRegionData
    B       CopyDataRomtoRam
InitData_Loop_End:
    MOV  PC, LR

; /***********************************************************************************************************************
; /* Clear Bss
; /**********************************************************************************************************************/
ClearBss:
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
EraseBss:
    MOVS    R4, #0
    STRB    R4, [R1]
    ADDS    R1, R1, #1
    CMP     R2, R1
    BEQ     SetaddRegionBss
    B       EraseBss
ClearBss_Loop_End:
    MOV     PC, LR

.align 4
.ltorg
