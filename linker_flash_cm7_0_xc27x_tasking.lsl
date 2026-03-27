////////////////////////////////////////////////////////////////////////////
//
//  File        :  linker_flash_cm7_0_xc27x_tasking.lsl
//
//  Description :  LSL file for the Infineon XC27x device (Core 0)
//                 Converted from IAR ICF to TASKING LSL
//
//  This version works with custom startup_cm7.s
//
//  Memory Layout:
//  -------------
//  ITCM          : 0x00000000 - 0x00007FFF   32 KB  (Instruction TCM)
//  DTCM          : 0x20000000 - 0x2000EFFF   60 KB  (Data TCM)
//  DTCM_STACK    : 0x2000F000 - 0x2000FFFF    4 KB  (Stack in DTCM)
//  FLASH_C0      : 0x10000000 - 0x101FF7FF 2046 KB  (Core 0 Flash)
//  FLS_RSV_FLASH : 0x101FF800 - 0x101FFFFF    2 KB  (Flash reserved for AC FLS)
//  SRAM_C0       : 0x30000000 - 0x3003F7FF  254 KB  (Core 0 SRAM)
//  FLS_RSV_RAM   : 0x3003F800 - 0x3003FFFF    2 KB  (RAM reserved for AC FLS)
//  SRAM_NO_CACHE : 0x30040000 - 0x30047FFF   32 KB  (Non-cacheable SRAM)
//  SRAM_SHAREABLE: 0x30048000 - 0x3004BFFF   16 KB  (Shareable SRAM)
//
////////////////////////////////////////////////////////////////////////////

//
// Memory region sizes
//
#define __ITCM_SIZE              32k
#define __DTCM_SIZE              60k
#define __DTCM_STACK_SIZE        4k
#define __FLASH_C0_SIZE          2046k
#define __FLS_RSV_FLASH_SIZE     2k
#define __SRAM_C0_SIZE           254k
#define __FLS_RSV_RAM_SIZE       2k
#define __SRAM_NO_CACHEABLE_SIZE 32k
#define __SRAM_SHAREABLE_SIZE    16k

//
// Memory region addresses
//
#define __ITCM_START             0x00000000
#define __ITCM_END               0x00007FFF

#define __DTCM_START             0x20000000
#define __DTCM_END               0x2000EFFF
#define __DTCM_STACK_START       0x2000F000
#define __DTCM_STACK_END         0x2000FFFF

#define __FLASH_C0_START         0x10000000
#define __FLASH_C0_END           0x101FF7FF
#define __FLS_RSV_FLASH_START    0x101FF800
#define __FLS_RSV_FLASH_END      0x101FFFFF

#define __SRAM_C0_START          0x30000000
#define __SRAM_C0_END            0x3003F7FF
#define __FLS_RSV_RAM_START      0x3003F800
#define __FLS_RSV_RAM_END        0x3003FFFF

#define __SRAM_NO_CACHEABLE_START 0x30040000
#define __SRAM_NO_CACHEABLE_END   0x30047FFF

#define __SRAM_SHAREABLE_START   0x30048000
#define __SRAM_SHAREABLE_END     0x3004BFFF

//
// Stack and heap configuration
//
#ifndef __CM7_0_STACK
#  define __CM7_0_STACK 4k
#endif

#ifndef __CM7_0_HEAP
#  define __CM7_0_HEAP 4k
#endif

#include "arm_mc_arch.lsl"

////////////////////////////////////////////////////////////////////////////
// Derivative Definition for Infineon XC27x
////////////////////////////////////////////////////////////////////////////

derivative xc27x
{
    core cm7_0
    {
        architecture = ARM;
    }

    bus local_bus
    {
        mau = 8;
        width = 32;
        map (size = 4G, src_offset = 0, dest_offset = 0, dest = bus:cm7_0:local_bus);
    }
}

////////////////////////////////////////////////////////////////////////////
// Section Setup - Core 0
////////////////////////////////////////////////////////////////////////////

section_setup :cm7_0:linear
{
    // Stack definition in DTCM
    stack "stack"
    (
#ifdef __CM7_0_STACK_FIXED
        fixed,
#endif
        align = 8,
        min_size = __CM7_0_STACK,
        grows = high_to_low
    );

    // Heap definition
    heap "heap"
    (
#ifdef __CM7_0_HEAP_FIXED
        fixed,
#endif
        align = 8,
        min_size = __CM7_0_HEAP
    );

    // Copy table for data initialization
    copytable
    (
        align = 8,
        dest = linear
    );
}

////////////////////////////////////////////////////////////////////////////
// Section Layout - Core 0
////////////////////////////////////////////////////////////////////////////

section_layout :cm7_0:linear
{
    // Stack placement in DTCM
    group ( ordered, run_addr = __DTCM_STACK_START )
    {
        select "stack";
    }

    // Exported symbols for stack (used by startup_cm7.s)
    "__STACK_DTCM_END"   = __DTCM_STACK_START;
    "__STACK_DTCM_START" = __DTCM_STACK_END;

    // Exported symbols for RAM initialization (used by startup_cm7.s)
    "__RAM_INIT"         = 1;
    "__INIT_SRAM_START"  = __SRAM_C0_START;
    "__INIT_SRAM_END"    = __SRAM_SHAREABLE_END;
    "__ITCM_INIT"        = 1;
    "__INIT_ITCM_START"  = __ITCM_START;
    "__INIT_ITCM_END"    = __ITCM_END;
    "__DTCM_INIT"        = 1;
    "__INIT_DTCM_START"  = __DTCM_START;
    "__INIT_DTCM_END"    = __DTCM_STACK_END;

    // Flash Access Code (AC FLS) symbols
    "__FLS_AC_ERASE_START_ADDR_IN_ROM"     = __FLS_RSV_FLASH_START;
    "__FLS_AC_WRITE_START_ADDR_IN_ROM"     = __FLS_RSV_FLASH_START;
    "__FLS_AC_BLANKREAD_START_ADDR_IN_ROM" = __FLS_RSV_FLASH_START;

    "__FLS_AC_ERASE_FUNC_PTR_IN_RAM"       = __FLS_RSV_RAM_START;
    "__FLS_AC_WRITE_FUNC_PTR_IN_RAM"       = __FLS_RSV_RAM_START;
    "__FLS_AC_BLANKREAD_FUNC_PTR_IN_RAM"   = __FLS_RSV_RAM_START;

    // Exported symbols for application use
    "__ROM_CODE_START"         = __FLASH_C0_START;
    "__RAM_SHAREABLE_START"    = __SRAM_SHAREABLE_START;
    "__RAM_STACK_START"        = __DTCM_STACK_START;
    "__RAM_NO_CACHEABLE_START" = __SRAM_NO_CACHEABLE_START;
    "LINKER_ID"                = 0;

    // ==================== ITCM Region ====================
    // Vector table (must be first in ITCM, used by startup_cm7.s)
    group ( ordered, run_addr = __ITCM_START )
    {
        select ".intvec";
        select ".intvec_init";
    }

    // Startup and initialization code
    group ( ordered )
    {
        select ".startup";
        select ".systeminit";
    }

    // Init table and zero table (used by startup_cm7.s for data initialization)
    group ( ordered )
    {
        select ".init_table";
        select ".zero_table";
    }

    // Main code sections
    group ( ordered )
    {
        select ".mcal_text.fast.*_init";
        select ".mcal_data.fast.*_init";
        select ".text";
        select ".mcal_text.*";
        select ".rodata";
        select ".mcal_const_cfg.*";
        select ".mcal_const.*";
    }

    // Data initialization images (in ROM, copied to RAM at startup)
    group ( ordered )
    {
        select ".data_init";
        select ".mcal_data.*_init";
        select ".ramcode*_init";
        select ".data_no_cacheable_init";
        select ".const_no_cacheable_init";
        select ".mcal_data_no_cacheable*_init";
        select ".mcal_const_no_cacheable*_init";
        select ".mcal_shared_data*_init";
    }

    // Flash Access Code (reserved for AC FLS module)
    group ( ordered, run_addr = __FLS_RSV_FLASH_START )
    {
        select ".acfls_code_rom";
    }

    // ==================== SRAM Region ====================
    // Initialized data in SRAM
    group ( ordered, run_addr = __SRAM_C0_START )
    {
        select ".data";
        select ".mcal_data.*";
        select ".ramcode*";
    }

    // Zero-initialized data (BSS) in SRAM
    group ( ordered )
    {
        select ".bss";
        select ".mcal_bss.*";
    }

    // ==================== SRAM Reserved for AC FLS ====================
    group ( ordered, run_addr = __FLS_RSV_RAM_START )
    {
        // This region is reserved for AC FLS RAM code
    }

    // ==================== SRAM Non-Cacheable ====================
    group ( ordered, run_addr = __SRAM_NO_CACHEABLE_START )
    {
        select ".bss_no_cacheable";
        select ".mcal_bss_no_cacheable*";
        select ".data_no_cacheable";
        select ".const_no_cacheable";
        select ".mcal_data_no_cacheable*";
        select ".mcal_const_no_cacheable*";
    }

    // ==================== SRAM Shareable ====================
    group ( ordered, run_addr = __SRAM_SHAREABLE_START )
    {
        select ".mcal_shared_data*";
        select ".mcal_shared_bss*";
    }

    // ==================== ITCM Region ====================
    // Fast code in ITCM
    group ( ordered )
    {
        select ".mcal_text.fast.*";
    }

    // ==================== DTCM Region ====================
    // Fast data in DTCM
    group ( ordered, run_addr = __DTCM_START )
    {
        select ".mcal_data.fast.*";
    }

    // Fast BSS in DTCM
    group ( ordered )
    {
        select ".mcal_bss.fast.*";
    }
}

////////////////////////////////////////////////////////////////////////////
// Processor Definition
////////////////////////////////////////////////////////////////////////////

processor ARM
{
    derivative = xc27x;
}

////////////////////////////////////////////////////////////////////////////
// Memory Definitions (only if __MEMORY is not defined)
////////////////////////////////////////////////////////////////////////////

#ifndef __MEMORY

memory XC27X_ITCM
{
    mau = 8;
    type = reserved ram;
    size = __ITCM_SIZE;
    map ( size = __ITCM_SIZE, dest_offset = __ITCM_START, dest = bus:ARM:local_bus, exec_priority = 2 );
}

memory XC27X_DTCM
{
    mau = 8;
    type = reserved ram;
    size = __DTCM_SIZE;
    map ( size = __DTCM_SIZE, dest_offset = __DTCM_START, dest = bus:ARM:local_bus, priority = 2, exec_priority = 0 );
}

memory XC27X_DTCM_STACK
{
    mau = 8;
    type = reserved ram;
    size = __DTCM_STACK_SIZE;
    map ( size = __DTCM_STACK_SIZE, dest_offset = __DTCM_STACK_START, dest = bus:ARM:local_bus, priority = 2, exec_priority = 0 );
}

memory XC27X_FLASH_C0
{
    mau = 8;
    type = rom;
    size = __FLASH_C0_SIZE;
    map ( size = __FLASH_C0_SIZE, dest_offset = __FLASH_C0_START, dest = bus:ARM:local_bus );
}

memory XC27X_FLS_RSV_FLASH
{
    mau = 8;
    type = rom;
    size = __FLS_RSV_FLASH_SIZE;
    map ( size = __FLS_RSV_FLASH_SIZE, dest_offset = __FLS_RSV_FLASH_START, dest = bus:ARM:local_bus );
}

memory XC27X_SRAM_C0
{
    mau = 8;
    type = ram;
    size = __SRAM_C0_SIZE;
    map ( size = __SRAM_C0_SIZE, dest_offset = __SRAM_C0_START, dest = bus:ARM:local_bus );
}

memory XC27X_FLS_RSV_RAM
{
    mau = 8;
    type = ram;
    size = __FLS_RSV_RAM_SIZE;
    map ( size = __FLS_RSV_RAM_SIZE, dest_offset = __FLS_RSV_RAM_START, dest = bus:ARM:local_bus );
}

memory XC27X_SRAM_NO_CACHEABLE
{
    mau = 8;
    type = ram;
    size = __SRAM_NO_CACHEABLE_SIZE;
    map ( size = __SRAM_NO_CACHEABLE_SIZE, dest_offset = __SRAM_NO_CACHEABLE_START, dest = bus:ARM:local_bus );
}

memory XC27X_SRAM_SHAREABLE
{
    mau = 8;
    type = ram;
    size = __SRAM_SHAREABLE_SIZE;
    map ( size = __SRAM_SHAREABLE_SIZE, dest_offset = __SRAM_SHAREABLE_START, dest = bus:ARM:local_bus );
}

#endif /* __MEMORY */
