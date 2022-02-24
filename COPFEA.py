import numpy as np
import matplotlib.pyplot as plt
import re
import glob
import os

# Merge all PDB files in a single master_file.pdb; running correctly in Windows at present
#import glob
#file_list = glob.glob("*.pdb")
#with open('master_file.pdb', 'w') as file:
#    input_lines = fileinput.input(file_list)
#    file.writelines(input_lines)

# Merge all PDB files in a single master_file.pdb; suitable for Linux-based architecture
filenames = ['051.pdb', '052.pdb', '053.pdb', '054.pdb', '055.pdb', '056.pdb', '057.pdb', '058.pdb', '059.pdb', '060.pdb', '061.pdb', '062.pdb', '063.pdb', '064.pdb', '065.pdb', '066.pdb', '067.pdb', '068.pdb', '069.pdb', '070.pdb', '071.pdb', '072.pdb', '073.pdb', '074.pdb', '075.pdb', '076.pdb', '077.pdb', '078.pdb', '079.pdb', '080.pdb', '081.pdb', '082.pdb', '083.pdb', '084.pdb', '085.pdb', '086.pdb', '087.pdb', '088.pdb', '089.pdb', '090.pdb', '091.pdb', '092.pdb', '093.pdb', '094.pdb', '095.pdb', '096.pdb', '097.pdb', '098.pdb', '099.pdb', '100.pdb', '101.pdb']
with open('master_file.pdb', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

# Reading the pharmacophore features from pharmacophore.txt as a set
keywords = set()
with open('pharmacophore.txt') as list_file:
    for line in list_file:
        if line.strip():
            keywords.add(line.strip())

# Searching the pharmacophore feature set from the master_file.pdb and export into results.pdb
with open('master_file.pdb') as master_file:
	with open('results.pdb', 'w') as search_results:
		for line in master_file:
			if set(line.split()[:-1]) & keywords:
				search_results.write(line)

# Searching the pharmacophore feature set from the reference (001.pdb) and export into reference.txt
with open('001.pdb') as master_file:
    with open('reference.txt', 'w') as search_results:
        for line in master_file:
            if set(line.split()[:-1]) & keywords:
                search_results.write(line)

# Replacing all spaces and new line characters with a single space in the PDB files
fin = open("results.pdb", "rt")
fout = open("formatted_output.txt", "wt")
rfin = open("reference.txt", "rt")
rfout = open("formatted_reference.txt", "wt")

for line in fin:
    fout.write(re.sub('\s+',' ',line)+"\n")

for line in rfin:
    rfout.write(re.sub('\s+',' ',line)+"\n")

fin.close()
fout.close()
rfin.close()
rfout.close()

# Reading the formatted_output.txt file, converting into CSV and extracting the x,y,z columns using the column index to flatten the 3D coordinates to 1D. Depth and width are kept constant (m = 3)
ax = ay = az = None
m = 3
flat = open("flattened_values.txt", "w")
with open('formatted_output.txt', 'r') as f, open('final_formatted_output.csv', 'w') as x:
    for line in f:
        x.write(", ".join(line.strip().split(" "))+'\n')
with open('final_formatted_output.csv') as infile:
    for line in infile:
            ax = float(line.split()[6].strip(","))
            ay = float(line.split()[7].strip(","))
            az = float(line.split()[8].strip(","))

            y = ax + (m*ay) + (m*m*az)
            format_y = "{:.2f}".format(y)
            print(format_y, file=flat)
            
flat.close()

# Reading the formatted_reference.txt file, converting into CSV and extracting the x,y,z columns using the column index to flatten the 3D coordinates to 1D. Depth and width are kept constant (m = 3)
ax = ay = az = None
m = 3

flat = open("reference_flattened_values.txt", "w")
with open('formatted_reference.txt', 'r') as f, open('final_reference_formatted_output.csv', 'w') as x:
    for line in f:
        x.write(", ".join(line.strip().split(" "))+'\n')
with open('final_reference_formatted_output.csv') as infile:
    for line in infile:
            ax = float(line.split()[6].strip(","))
            ay = float(line.split()[7].strip(","))
            az = float(line.split()[8].strip(","))

            y = ax + (m*ay) + (m*m*az)
            format_y = "{:.2f}".format(y)
            print(format_y, file=flat)
            
flat.close()

#Counting the total number of input pharmacophore features given for calculations
Phar = open("pharmacophore.txt","r")
Counter = 0
Content = Phar.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
    	Counter += 1
          
print("The total number of input pharmacophore features are:", Counter)
print("The pharmacophore features are (not in given order as in pharmacophore.txt):\n", keywords)

#Creating dictionary for fast and efficient searching of pharmacophore features
a_file = open("pharmacophore.txt", "r")
list_of_lists_1 = [(line.strip()).strip() for line in a_file]

b_file = open("reference_flattened_values.txt", "r")
list_of_lists_2 = [(line.strip()).strip() for line in b_file]
b_file.close()
dct = {}
for k, v in zip(list_of_lists_1, list_of_lists_2):
	dct[k] = v

print("The reference feature set used for calculations\n", str(dct))

#Extracting the flattened values of respective pharmacophore feature given in the pharmacophore.txt and exporting the file as separate Feature_<feature_name>.txt in the folder
keys_list = list(dct)
i = x = 0
with open("flattened_values.txt") as f:
	lines = f.readlines()
	while (x < Counter):
		desired_lines = lines[i::Counter]
		a_keys = keys_list[i]
		c = dct.get(a_keys)
		C = float(c)
		desired_lines = list(map(lambda x:x.strip(), desired_lines))
		arr = np.array(desired_lines, dtype=float)
		arr = arr - C
		with open("Feature_" + str(a_keys) + ".txt", "w") as namesake:
			np.savetxt(namesake, np.array(arr))
		x = x + 1
		i = i + 1

#Requesting the user to give pharmacophore feature that needs to be cross-correlated with other features given in the pharmacophore.txt 
fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.xlabel("Lag")
plt.ylabel("Correlation coefficient")
ax1.grid(True)
ax1.axhline(0, color='red', lw=2)

first_variable = input("Enter the pharmacophore feature you want to calculate cross-correlation with other features enumerated in the calculations:")
file_opened = "Feature_" + str(first_variable) + ".txt"
with open(file_opened, "r") as f:
		g = f.readlines()
		for i in range(len(g)):
			g[i]=float(g[i].strip("\n"))

# Computing the cross-correlation with other non-input features and exporting the cross-correlated plot in the current folder
file_list = glob.glob("Feature_*.txt")
for file in file_list:
	with open(file, "r") as h:
		if file != file_opened:
			j = h.readlines()
			for i in range(len(j)):
				j[i]=float(j[i].strip("\n"))
			reader = len(open(file).readlines(  ))
			labeller = file_opened+file
			labeller = labeller.replace('.txt', '')
			labeller = labeller.replace('Feature_', ' ')
			ax1.xcorr(g, j, usevlines=False, maxlags=reader-1, normed=True, lw=1, label=labeller)
			ax1.legend(loc='best')
			plt.savefig("Computed Correlated Features", dpi = 300)	
			
#Deleting transient files generated during the calculations. Uncomment to verify the steps made in the calculations
os.remove("final_formatted_output.csv")
os.remove("final_reference_formatted_output.csv")
os.remove("flattened_values.txt")
os.remove("formatted_output.txt")
os.remove("formatted_reference.txt")
os.remove("reference.txt")
os.remove("reference_flattened_values.txt")
