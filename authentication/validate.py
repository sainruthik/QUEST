from .models import Client
import smtplib

def alreadyLoggedIN(req):
    try:
        username = req.session['username']
        password = req.session['password']
        return validateLogIn(username,password)
    except:
        return False


def validateEmail(email):
    k = Client.objects.all().filter(email=email)
    if len(k)==1:
        return 0 
    return 1

def validatePassword():
    pass

def validateLogIn(username,password):
    obj = Client.objects.all().filter(username=username,password=password)
    return len(obj)


def checkLogIn():
    pass

def sendOTP(otp,receiver):
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    sender = "quest.app.india@gmail.com"
    s.login(sender , "QuestIndia@2020") 
    SUBJECT = "Quest India - OTP"
    TEXT = "Your OTP for sign up is {0}".format(otp)
    # message to be sent 
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (sender, receiver, SUBJECT, TEXT)
    
    # sending the mail 
    s.sendmail(sender, receiver, message)
    
    # terminating the session 
    s.quit() 