import ftplib

ftp= ftplib.FTP('192.168.43.198')
ftp.login('ftp-user', 'ahir1234')
# Enter File Name with Extension
filename = "Rajkot.txt"
# Write file in binary mode
with open(filename, "wb") as file:
	# Command for Downloading the file "RETR filename"
	ftp.retrbinary(f"RETR {filename}", file.write)
file = open(filename, "r")
print('File Content:', file.read())

filename1 = "ahmedabad.txt"
# Write file in binary mode
with open(filename1, "wb") as file:
	# Command for Downloading the file "RETR filename"
	ftp.retrbinary(f"RETR {filename1}", file.write)
file1 = open(filename1, "r")
print('File Content:', file1.read())

filename2 = "jamnagar.txt"
# Write file in binary mode
with open(filename2, "wb") as file:
	# Command for Downloading the file "RETR filename"
	ftp.retrbinary(f"RETR {filename2}", file.write)
file2 = open(filename2, "r")
print('File Content:', file2.read())
print()
filename3 = "mumbai.txt"
# Write file in binary mode
with open(filename3, "wb") as file:
	# Command for Downloading the file "RETR filename"
	ftp.retrbinary(f"RETR {filename3}", file.write)
file3 = open(filename3, "r")
print('File Content:', file3.read())


ftp.retrlines('LIST')
ftp.quit()
