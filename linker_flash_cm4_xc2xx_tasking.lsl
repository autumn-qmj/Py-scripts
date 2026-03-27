////////////////////////////////////////////////////////////////////////////
//
//  File        :  linker_flash_cm4_xc2xx_tasking.lsl
//
//  Description :  LSL file for the Infineon XC2xx device (Cortex-M4)
//                 Converted from IAR ICF to TASKING LSL
//
//  Memory Layout:
//  -------------
//  INT           : 0x20000000 - 0x200001FF    512 B  (Interrupt Vector Table)
//  FLASH         : 0x00000000 - 0x0007FAFF  511 KB  (Flash)
//  FLS_RSV_FLASH : 0x0007FB00 - 0x0007FFFF    1 KB  (Flash reserved for AC FLS)
//  SRAM          : 0x20000200 - 0x2001DAFF  118.5 KB (SRAM)
//  SRAM_STACK    : 0x2001DB00 - 0x2001FB00    8 KB  (Stack)
//  FLS_RSV_RAM   : 0x2001FB00 - 0x2001FFFF    1 KB  (RAM reserved for AC FLS)
//
////////////////////////////////////////////////////////////////////////////

//
// Memory region sizes
//
#define __INT_SIZE               512
#define __FLASH_SIZE             0x7FB00           /* 512KB - 1KB = 511KB usable */
#define __FLS_RSV_FLASH_SIZE     0x400             /* 1KB */
#define __SRAM_SIZE              0x1D900           /* 118.5KB */
#define __SRAM_STACK_SIZE        0x2000            /* 8KB */
#define __FLS_RSV_RAM_SIZE       0x400             /* 1KB */

//
// Memory region addresses
//
#define __INT_START              0x20000000
#define __INT_END                0x200001FF

#define __FLASH_START            0x00000000
#define __FLASH_END              0x0007FAFF
#define __FLS_RSV_FLASH_START    0x0007FB00
#define __FLS_RSV_FLASH_END      0x0007FFFF

#define __SRAM_START             0x20000200
#define __SRAM_END               0x2001DAFF
#define __SRAM_STACK_START       0x2001DB00
#define __SRAM_STACK_END         0x2001FB00

#define __FLS_RSV_RAM_START      0x2001FB00
#define __FLS_RSV_RAM_END        0x2001FFFF

#define __SRAM_REGION_START      0x20000000
#define __SRAM_REGION_END        0x20020000

//
// Stack and heap configuration
//
#ifndef __CM4_STACK
#  define __CM4_STACK 8k
#endif

#ifndef __CM4_HEAP
#  define __CM4_HEAP 4k
#endif

//
// Vector table configuration
//
#define __NR_OF_VECTORS          256
#define __CM4_NR_OF_VECTORS      __NR_OF_VECTORS

#ifndef __CM4_VECTOR_TABLE_ROM_ADDR
#  define __CM4_VECTOR_TABLE_ROM_ADDR  __FLASH_START
#endif

#ifndef __CM4_VECTOR_TABLE_RAM_ADDR
#  define __CM4_VECTOR_TABLE_RAM_ADDR  __INT_START
#endif

// Copy vector table to INT RAM at startup
#ifdef __CM4_VECTOR_TABLE_RAM_COPY
# define __CM4_VECTOR_TABLE_COPY_ATTRIBUTE copy,
# define __CM4_VECTOR_TABLE_RUN_ADDR __CM4_VECTOR_TABLE_RAM_ADDR
#else
# define __CM4_VECTOR_TABLE_COPY_ATTRIBUTE
# define __CM4_VECTOR_TABLE_RUN_ADDR __CM4_VECTOR_TABLE_ROM_ADDR
#endif

#define __CM4_VECTOR_TABLE_SIZE (__CM4_NR_OF_VECTORS * 4)
#define __THUMB_OFFSET 1

#include "arm_mc_arch.lsl"

////////////////////////////////////////////////////////////////////////////
// Derivative Definition for Infineon XC2xx
////////////////////////////////////////////////////////////////////////////

derivative xc2xx
{
    core cm4
    {
        architecture = ARM;
    }

    bus local_bus
    {
        mau = 8;
        width = 32;
        map (size = 4G, src_offset = 0, dest_offset = 0, dest = bus:cm4:local_bus);
    }
}

////////////////////////////////////////////////////////////////////////////
// Section Setup - Cortex-M4
////////////////////////////////////////////////////////////////////////////

section_setup :cm4:linear
{
    // Stack definition
    stack "stack"
    (
#ifdef __CM4_STACK_FIXED
        fixed,
#endif
        align = 8,
        min_size = __CM4_STACK,
        grows = high_to_low
    );

    // Heap definition
    heap "heap"
    (
#ifdef __CM4_HEAP_FIXED
        fixed,
#endif
        align = 8,
        min_size = __CM4_HEAP
    );

    // Start address
    start_address
    (
#ifdef __CM4_START
        run_addr = __CM4_START | __THUMB_OFFSET,
#endif
        symbol = "Reset_Handler"
    );

    // Copy table for data initialization
    copytable
    (
        align = 8,
        dest = linear
    );

#if !defined(__CM4_NO_AUTO_VECTORS) && !defined(__CM4_NO_DEFAULT_AUTO_VECTORS)
    // Vector table with handler addresses
    vector_table "vector_table"
    (
        vector_size = 4,
        size = __CM4_NR_OF_VECTORS,
        run_addr = __CM4_VECTOR_TABLE_RUN_ADDR,
        template = ".text.handler_address",
        template_symbol = "_lc_vector_handler",
        vector_prefix = "_vector_",
        __CM4_VECTOR_TABLE_COPY_ATTRIBUTE
        fill = loop,
        no_inline
    )
    {
        vector ( id =   0, fill = "_lc_ub_stack" );
        vector ( id =   1, fill = "Reset_Handler" );
        vector ( id =   2, optional, fill = "NMI_Handler" );
        vector ( id =   3, optional, fill = "HardFault_Handler" );
        vector ( id =   4, optional, fill = "MemManage_Handler" );
        vector ( id =   5, optional, fill = "BusFault_Handler" );
        vector ( id =   6, optional, fill = "UsageFault_Handler" );
        vector ( id =  11, optional, fill = "SVC_Handler" );
        vector ( id =  12, optional, fill = "DebugMon_Handler" );
        vector ( id =  14, optional, fill = "PendSV_Handler" );
        vector ( id =  15, optional, fill = "SysTick_Handler" );
        // Add device-specific interrupt vectors here
    }
#endif
}

////////////////////////////////////////////////////////////////////////////
// Section Layout - Cortex-M4
////////////////////////////////////////////////////////////////////////////

section_layout :cm4:linear
{
    // Stack placement
    group ( ordered, run_addr = __SRAM_STACK_START )
    {
        select "stack";
    }

    // Exported symbols for stack
    "__STACK_END"   = __SRAM_STACK_START;
    "__STACK_START" = __SRAM_STACK_END;

    // Exported symbols for RAM initialization
    "__INIT_SRAM_START" = __SRAM_REGION_START;
    "__INIT_SRAM_END"   = __SRAM_REGION_END;

    // Flash Access Code (AC FLS) symbols
    "__FLS_AC_ERASE_START_ADDR_IN_ROM"     = __FLS_RSV_FLASH_START;
    "__FLS_AC_WRITE_START_ADDR_IN_ROM"     = __FLS_RSV_FLASH_START;
    "__FLS_AC_BLANKREAD_START_ADDR_IN_ROM" = __FLS_RSV_FLASH_START;

    "__FLS_AC_ERASE_FUNC_PTR_IN_RAM"       = __FLS_RSV_RAM_START;
    "__FLS_AC_WRITE_FUNC_PTR_IN_RAM"       = __FLS_RSV_RAM_START;
    "__FLS_AC_BLANKREAD_FUNC_PTR_IN_RAM"   = __FLS_RSV_RAM_START;

    // VTOR initialization value
    "_lc_vtor_value" = __CM4_VECTOR_TABLE_RUN_ADDR;

    // Exported symbols for application use
    "__ROM_CODE_START" = __FLASH_START;
    "__RAM_STACK_START" = __SRAM_STACK_START;
    "LINKER_ID"        = 0;

    // Vector table in ROM or INT RAM
#ifdef __CM4_VECTOR_TABLE_RAM_COPY
    group ( contiguous, ordered, load_addr = __CM4_VECTOR_TABLE_ROM_ADDR )
    {
        select "_vector_0";
        select "_vector_1";
    }
#endif

    // ==================== FLASH Region ====================
    // Vector table initialization code (first in flash, aligned to 512)
    group ( ordered, run_addr = __FLASH_START )
    {
        select ".intvec_init";
    }

    // Startup and initialization code
    group ( ordered )
    {
        select ".startup";
        select ".systeminit";
    }

    // Main code sections
    group ( ordered )
    {
        select ".text";
        select ".mcal_text.*";
        select ".rodata";
        select ".mcal_const_cfg.*";
        select ".mcal_const.*";
        select ".init_table";
        select ".zero_table";
    }

    // Data initialization images (in ROM, copied to RAM at startup)
    group ( ordered )
    {
        select ".data_init";
        select ".mcal_data.*_init";
    }

    // Flash Access Code (reserved for AC FLS module)
    group ( ordered, run_addr = __FLS_RSV_FLASH_START )
    {
        select ".acfls_code_rom";
    }

    // ==================== SRAM Region ====================
    // Initialized data in SRAM
    group ( ordered, run_addr = __SRAM_START )
    {
        select ".data";
        select ".mcal_data.*";
    }

    // Zero-initialized data (BSS) in SRAM
    group ( ordered )
    {
        select ".bss";
        select ".mcal_bss.*";
    }

    // ==================== INT RAM Region ====================
    // Vector table in INT RAM
    group ( ordered, run_addr = __INT_START )
    {
        select ".intvec";
    }
}

////////////////////////////////////////////////////////////////////////////
// Processor Definition
////////////////////////////////////////////////////////////////////////////

processor ARM
{
    derivative = xc2xx;
}

////////////////////////////////////////////////////////////////////////////
// Memory Definitions (only if __MEMORY is not defined)
////////////////////////////////////////////////////////////////////////////

#ifndef __MEMORY

memory XC2XX_INT
{
    mau = 8;
    type = reserved ram;
    size = __INT_SIZE;
    map ( size = __INT_SIZE, dest_offset = __INT_START, dest = bus:ARM:local_bus, exec_priority = 2 );
}

memory XC2XX_FLASH
{
    mau = 8;
    type = rom;
    size = __FLASH_SIZE;
    map ( size = __FLASH_SIZE, dest_offset = __FLASH_START, dest = bus:ARM:local_bus );
}

memory XC2XX_FLS_RSV_FLASH
{
    mau = 8;
    type = rom;
    size = __FLS_RSV_FLASH_SIZE;
    map ( size = __FLS_RSV_FLASH_SIZE, dest_offset = __FLS_RSV_FLASH_START, dest = bus:ARM:local_bus );
}

memory XC2XX_SRAM
{
    mau = 8;
    type = ram;
    size = __SRAM_SIZE;
    map ( size = __SRAM_SIZE, dest_offset = __SRAM_START, dest = bus:ARM:local_bus );
}

memory XC2XX_SRAM_STACK
{
    mau = 8;
    type = ram;
    size = __SRAM_STACK_SIZE;
    map ( size = __SRAM_STACK_SIZE, dest_offset = __SRAM_STACK_START, dest = bus:ARM:local_bus );
}

memory XC2XX_FLS_RSV_RAM
{
    mau = 8;
    type = ram;
    size = __FLS_RSV_RAM_SIZE;
    map ( size = __FLS_RSV_RAM_SIZE, dest_offset = __FLS_RSV_RAM_START, dest = bus:ARM:local_bus );
}

#endif /* __MEMORY */
