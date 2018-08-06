
import sys
fin = open("input_tab.txt", "r")
fout = open("output_comma.txt", "w")
vCnt = 0

# from excel

for line in fin:
	if (sys.argv[1] == "time"):
		fout.write(str(float(line)/1000)+",")
	else:
		fout.write(line.rstrip()+",")
fout.write("\n")

# from "appro_stream.txt"
'''
v = 0
for line in fin:
	lines = line.split('\t')
	if((len(lines)>12)):
		if(v != 0):
			#fout.write(str(int(lines[0]))+",")
			fout.write(str(float(lines[8])/v/1000000)+",")
		v+=1
fout.write("\n")
'''