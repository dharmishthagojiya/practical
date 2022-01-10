import ftplib
from ftplib import FTP
#ftp = ftplib.FTP('ftp.sunet.se', 'anonymous', 'anonymous@sunet.se')
'''ftp=ftplib.FTP('ftp.us.debian.org')
ftp.login()
print ("File List: ")
files = ftp.dir()
print(files)
print(ftp.cwd('debian'))
print(ftp.retrlines('LIST'))'''

#ftp = ftplib.FTP("ftp.us.debian.org")
#ftp.login("anonymous", "anonymous@sunet.se")
#ftp.encoding = "utf-8"
session = ftplib.FTP('ftp.us.debian.org','anonymous','anonymous@sunet.se')
file = open('E001_v2.py','wb')                  # file to send
session.storbinary('STOR E001_v2.py', file)     # send the file
file.close()                                    # close file and FTP
session.quit()
