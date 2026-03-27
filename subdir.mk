################################################################################
# Automatically-generated file. Do not edit!
################################################################################

C_FILES += "..\startup\system_xc2xx_cm4.c"
OBJ_FILES += "startup\system_xc2xx_cm4.obj"
"startup\system_xc2xx_cm4.obj" : "..\startup\system_xc2xx_cm4.c" "startup\.system_xc2xx_cm4.obj.opt"
	@echo Compiling ${<F}
	@"${PRODDIR}\bin\ccarm" -f "startup\.system_xc2xx_cm4.obj.opt"

"startup\.system_xc2xx_cm4.obj.opt" : .refresh
	@argfile "startup\.system_xc2xx_cm4.obj.opt" -o "startup\system_xc2xx_cm4.obj" "..\startup\system_xc2xx_cm4.c" -Ccortex_m7 -t -Wa-gAHLs -Wa--error-limit=42 -DARMCM7 -D__FPU_PRESENT=0 -I"C:\mywork\UM\HITECK_TASKING\hightec\XC2xx_Template_V1.0.2\TASKING\XC2xx_Template_Cm4\include" --iso=17 --language=-gcc,-volatile,+strings,-kanji --fp-model=cFzr -O2 --tradeoff=4 --compact-max-size=200 -g --error-limit=42 --source --global-type-checking -c --dep-file="startup\.system_xc2xx_cm4.obj.d" -Wc--make-target="startup\system_xc2xx_cm4.obj"
DEPENDENCY_FILES += "startup\.system_xc2xx_cm4.obj.d"


# Assembly file
ASM_FILES += "..\startup\startup_cm4.s"
OBJ_FILES += "startup\startup_cm4.obj"
"startup\startup_cm4.obj" : "..\startup\startup_cm4.s" "startup\.startup_cm4.obj.opt"
	@echo Assembling ${<F}
	@"${PRODDIR}\bin\asarm" -f "startup\.startup_cm4.obj.opt"

"startup\.startup_cm4.obj.opt" : .refresh
	@argfile "startup\.startup_cm4.obj.opt" -o "startup\startup_cm4.obj" "..\startup\startup_cm4.s" -Ccortex_m7 -t -Wa-gAHLs -Wa--error-limit=42 -I"C:\mywork\UM\HITECK_TASKING\hightec\XC2xx_Template_V1.0.2\TASKING\XC2xx_Template_Cm4\include" -g --error-limit=42 --source -c --dep-file="startup\.startup_cm4.obj.d" -Wa--make-target="startup\startup_cm4.obj"
DEPENDENCY_FILES += "startup\.startup_cm4.obj.d"


GENERATED_FILES += "startup\system_xc2xx_cm4.obj" "startup\.system_xc2xx_cm4.obj.opt" "startup\.system_xc2xx_cm4.obj.d" "startup\system_xc2xx_cm4.src" "startup\system_xc2xx_cm4.lst"
GENERATED_FILES += "startup\startup_cm4.obj" "startup\.startup_cm4.obj.opt" "startup\.startup_cm4.obj.d" "startup\startup_cm4.src" "startup\startup_cm4.lst"
