import ftplib
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
'''
session = ftplib.FTP('ftp.us.debian.org','anonymous','anonymous@sunet.se')
file = open('E001_v2.py','wb')                  # file to send
session.storbinary('STOR E001_v2.py', file)     # send the file
file.close()                                    # close file and FTP
session.quit()'''
'''
def downloadFile():
   filename = 'README.MIRRORS'
   localfile = open(filename, 'wb')
   ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
   ftp.quit()
   localfile.close()
#permission denied error get
def uploadFile():
   filename = 'D:\1into2project\E001_V3.py'
   ftp.storbinary('STOR '+filename, open(filename, 'rb'))
   ftp.quit()
with FTP("ftp1.at.proftpd.org") as ftp:
   ftp.login()
   ftp.getwelcome()
   ftp.dir()
   downloadFile()
   uploadFile()
downloadFile()
'''''

