from ftplib import FTP_TLS
import os

""" Connect to an FTP server.
      by yourstrulyhb 

   References:
   https://docs.python.org/3/library/ftplib.html
   """


def get_ftp() -> FTP_TLS:

   # Get FTP details
   FTPHOST = os.environ.get("FTPHOST")
   FTPUSER = os.environ.get("FTPUSER")
   FTPPASS = os.environ.get("FTPPASS")
   FTPPORT = os.environ.get("FTPPORT")

   print("Starting FTP server...")

   ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)     # Creates instance of FTP class
   ftp.prot_p()                                 # Set up secure data connection.

   print("FTP server running...")
   return ftp
 

def read_csv(config: dict) -> pd.DataFrame:
   url = config["URL"]
   params = config["PARAMS"]

   return pd.read_csv(url, **params)

if __name__=="__main__":
   get_ftp()