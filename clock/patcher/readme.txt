This scripts is used to create template for clock driver, but it support update patch only now.
If you want to use it to update clock driver, please follow:
1.specificy target sdk path to path.txt
2.create you patch file, please reference lp8 directory
3.run python clock_patcher.py -d target
	eg: python clock_patcher.py -d lpc8
		python clock_patcher.py -d lpc54