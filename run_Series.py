#!/usr/bin/python
import os
import time
input("Press enter")
trials=15
for i in range(1,trials+1):
	print(str(i)+":")
	os.system("sudo cp /home/davidsjt/Documents/ECE532/DRAMSim3_mods/dramsim3_wrapper_"+str(i)+".cc /home/davidsjt/Documents/ECE532/gem5/src/mem/dramsim3_wrapper.cc")
#	input("...")
	os.system("sudo ./compile_gem5_X86.sh")
	os.system("sudo ./run_gem5.sh")
#	input("...")
	os.system("sudo cp m5out/dramsim3.json results/dramsim3_"+str(i)+".json")
	os.system("sudo cp m5out/dramsim3.txt results/dramsim3_"+str(i)+".txt")
#	input("Done")
