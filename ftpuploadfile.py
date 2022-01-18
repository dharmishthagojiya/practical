import ftplib
session = ftplib.FTP('192.168.43.198', 'ftp-user', 'ahir1234')
file2 = open(r'D:\projectfiles\mumbai.txt', 'rb')                  # file to send
session.storbinary(r'STOR mumbai.txt', file2)     # send the file
file3 = open(r'D:\projectfiles\jamnagar.txt', 'rb')                  # file to send
session.storbinary(r'STOR jamnagar.txt', file3)
file = open(r'D:\projectfiles\Rajkot.txt', 'rb')                  # file to send
session.storbinary(r'STOR Rajkot.txt', file)
file1 = open(r'D:\projectfiles\ahmedabad.txt', 'rb')                  # file to send
session.storbinary(r'STOR ahmedabad.txt', file1)
# send the file

file.close()                                    # close file and FTP
session.quit()
