import os
import datetime

def create_folders():
	os.mkdir("C:\\Users\\mail\\Desktop\\photosbyyear")
	for i in range(2015, 2021):
		os.mkdir(os.path.join("C:\\Users\\mail\\Desktop\\photosbyyear", str(i)))
		for j in range(1, 13):
			os.mkdir(os.path.join("C:\\Users\\mail\\Desktop\\photosbyyear", str(i), str(j)))
			for k in range(1, 32):
				os.mkdir(os.path.join("C:\\Users\\mail\\Desktop\\photosbyyear", str(i), str(j), str(k)))

create_folders()