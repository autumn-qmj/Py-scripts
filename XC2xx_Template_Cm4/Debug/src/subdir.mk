################################################################################
# Automatically-generated file. Do not edit!
################################################################################

C_FILES += "..\src\main.c"
OBJ_FILES += "src\main.obj"
"src\main.obj" : "..\src\main.c" "src\.main.obj.opt"
	@echo Compiling ${<F}
	@"${PRODDIR}\bin\ccarm" -f "src\.main.obj.opt"

"src\.main.obj.opt" : .refresh
	@argfile "src\.main.obj.opt" -o "src\main.obj" "..\src\main.c" -Ccortex_m7 -t -Wa-gAHLs -Wa--error-limit=42 -DARMCM7 -D__FPU_PRESENT=0 -I"C:\mywork\UM\HITECK_TASKING\hightec\XC2xx_Template_V1.0.2\TASKING\XC2xx_Template_Cm4\include" --iso=17 --language=-gcc,-volatile,+strings,-kanji --fp-model=cFzr -O2 --tradeoff=4 --compact-max-size=200 -g --error-limit=42 --source --global-type-checking -c --dep-file="src\.main.obj.d" -Wc--make-target="src\main.obj"
DEPENDENCY_FILES += "src\.main.obj.d"


GENERATED_FILES += "src\main.obj" "src\.main.obj.opt" "src\.main.obj.d" "src\main.src" "src\main.lst"
