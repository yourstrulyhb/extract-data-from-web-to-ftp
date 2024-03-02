from ftplib import FTP_TLS
import os
import pandas as pd
import json 

""" Connect to an FTP server.
      by yourstrulyhb 

   References:
   https://docs.python.org/3/library/ftplib.html
   """


def get_ftp() -> FTP_TLS:
   """ Start an FTP server.
   Return an FTP server [object].
   """

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
 
# def upload_to_ftp(ftp: FTP_TLS, file_source: Path):

#    # Open file source
#    with open(file_source, "rb") as fp:
#       ftp.storbinary("STOR {file_source.name}")

def read_csv(config: dict) -> pd.DataFrame:
   url = config["URL"]
   params = config["PARAMS"]

   return pd.read_csv(url, **params)


if __name__=="__main__":
   get_ftp()


   # Load source configuration
   with open("config.json", "rb") as fp:
      config = json.load(fp)

   # Download files
   for source_name, source_config in config.items():
      file_name =  source_name + ".csv"
      df = read_csv(source_config)
      df.to_csv(file_name, index=False)