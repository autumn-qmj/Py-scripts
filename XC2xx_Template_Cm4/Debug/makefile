################################################################################
# Automatically-generated file. Do not edit!
################################################################################

PROJ 	= XC2xx_Template_Cm4
PRODDIR = C:\Program Files\TASKING\Arm v7.1r1\carm

-include "..\makefile.init"

all :

-include "subdir.mk"
-include "src\subdir.mk"
-include "startup\subdir.mk"
-include "..\makefile.defs"

EXT_LIBRARIES =

all : "XC2xx_Template_Cm4.abs"

"XC2xx_Template_Cm4.abs" : $(OBJ_FILES) $(EXT_LIBRARIES) ".XC2xx_Template_Cm4.abs.opt"
	@echo Linking to ${@F}
	@"${PRODDIR}\bin\ccarm" -f ".XC2xx_Template_Cm4.abs.opt"

".XC2xx_Template_Cm4.abs.opt" : .refresh
	@argfile ".XC2xx_Template_Cm4.abs.opt" -o "XC2xx_Template_Cm4.abs" $(OBJ_FILES) $(EXT_LIBRARIES) -Ccortex_m7 -t -Wl-D__DEVICE_LSL_FILE=cm7.lsl "../linker/flash/XC2xx_Template_Cm4.lsl" -Wl-OtZxycL --no-map-file -Wl--map-file="${PROJ}.mapxml":XML -Wl-mcrfiklSmNOduQ -Wl--error-limit=42 --fpu=none -g --fp-model=cFzr --global-type-checking --c++=14 -Wl--dep-file=".XC2xx_Template_Cm4.abs.d" -Wl--make-target="XC2xx_Template_Cm4.abs"
DEPENDENCY_FILES += ".XC2xx_Template_Cm4.abs.d"
-include $(DEPENDENCY_FILES)

$(EXT_LIBRARIES) : .dummy

GENERATED_FILES += "XC2xx_Template_Cm4.abs" "XC2xx_Template_Cm4*.sre" "XC2xx_Template_Cm4*.hex" "XC2xx_Template_Cm4.map*" "XC2xx_Template_Cm4.mdf" ".XC2xx_Template_Cm4.abs.opt" ".XC2xx_Template_Cm4.abs.d"
-include "..\makefile.targets"

clean : ".clean.opt"
	@echo Cleaning
	@rm -f -m ".clean.opt"

".clean.opt" : .refresh
	@argfile ".clean.opt" $(GENERATED_FILES) $(OPTIONAL_FILES)

GENERATED_FILES += ".clean.opt"
OPTIONAL_FILES +=  "*.pre" "*.lst"


.PHONY : .dummy .refresh
