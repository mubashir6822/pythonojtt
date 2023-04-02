import smtplib 

try: 
    #Create your SMTP session 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 

    #Give ur Username and password
    smtp.login("sender_email_id","sender_email_id_password")
 
    message = "Message_you_need_to_send" 

    #Sending the Email with msg
    smtp.sendmail("sender_email_id", "receiver_email_id",message) 

    #Stop the session 
    smtp.quit() 
    print ("Email sent successfully!") 
except: 
    print("Something went wrong....may be your credentials are wrong.. please check")