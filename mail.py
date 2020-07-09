import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
def no_mask():
    msg = MIMEMultipart('related')
    msg['Subject'] = "Unsafe Guest"
    msg['From'] = 'mukundacharya2020@gmail.com'
    msg['To'] = 'mukuacharya30@gmail.com'
    #now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = """\
    <html>
    <body>
    <h1 style="background-color: red;text-align: Center;color: white;font-size:40px"> UNSAFE!</h1>
    <p style="text-align: center;font-size: 30px"> <b>This Person is not safe to Enter the house</b></p>
    <img src="cid:image1" style="display: block;margin-left: auto;margin-right: auto; width:50%"></img>
    <p>Regards,</p><p>Mask Detector</p>
    </body>
    </html>
    """
    # Record the MIME types of text/html.
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part2)

    # This example assumes the image is in the current directory
    fp = open('C:\\ML\\face_mask\\op\\image.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    # Send the message via local SMTP server.
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mukundacharya2020@gmail.com','cdxsfozsqkposogy')
    server.sendmail('mukundacharya2020@gmail.com', 'mukuacharya30@gmail.com', msg.as_string())
    server.quit()
    
def mask():
    msg = MIMEMultipart('related')
    msg['Subject'] = "Safe Guest"
    msg['From'] = 'mukundacharya2020@gmail.com'
    msg['To'] = 'mukuacharya30@gmail.com'
    #now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = """\
    <html>
    <body>
    <h1 style="background-color: green;text-align: Center;color: white;font-size:40px"> SAFE!</h1>
    <p style="text-align: center;font-size: 30px"> <b>The person is wearing a mask and is safe to enter.</b></p>
    <img src="cid:image1" style="display: block;margin-left: auto;margin-right: auto; width:50%"></img>
    <p>Regards</p><p>Mask Detector</p>
    </body>
    </html>
    """
    # Record the MIME types of text/html.
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part2)

    # This example assumes the image is in the current directory
    fp = open('C:\\ML\\face_mask\\op\\image.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    # Send the message via local SMTP server.
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mukundacharya2020@gmail.com','cdxsfozsqkposogy')
    server.sendmail('mukundacharya2020@gmail.com', 'mukuacharya30@gmail.com', msg.as_string())
    server.quit()
    