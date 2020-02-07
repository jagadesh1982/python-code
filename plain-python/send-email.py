from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

threshold = 1
partition = "/"


def report_via_email():
      # Python code to illustrate Sending mail from  
      # creates SMTP session 
      server = smtplib.SMTP('smtp.gmail.com', 587)
      
      msg = MIMEMultipart()      
      msg['From'] = "jagadesh.manchala@gmail.com"
      msg['To'] = "jagadesh.manchala@gmail.com"
      msg['Subject'] = "Disk alert Warning" 
      
      body = "Disk is alerting Too Much"
      msg.attach(MIMEText(body, 'plain'))

      server.starttls() 
      server.login("jagadesh.manchala@gmail.com", "*******") 
      server.sendmail("jagadesh.manchala@gmail.com", "jagadesh.manchala@gmail.com", msg.as_string())  
      server.quit() 
 

def check_once():
    df = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
    for line in df.stdout:
        splitline=line.decode().split()
        if splitline[5] == partition:
           if int(splitline[4][:-1]) > threshold:
              print line 
              report_via_email()
   
check_once()
