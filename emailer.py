import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, email_address, email_password, smtp_server="smtp.gmail.com", smtp_port=587):
        self.email_address = email_address
        self.email_password = email_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
    
    def send_email(self, recipient_email, subject, body):
        try:
            # Create the email
            msg = MIMEMultipart()
            msg["From"] = self.email_address
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))
            
            # Connect to SMTP server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email_address, self.email_password)
                server.sendmail(self.email_address, recipient_email, msg.as_string())
            
            print("✅ Email sent successfully!")
        except Exception as e:
            print("❌ Error:", e)

# Usage Example:
if __name__ == "__main__":
    email_sender = EmailSender("your_email@gmail.com", "your_app_password")
    email_sender.send_email("recipient@example.com", "Test Email", "Hello, this is a test email sent from Python!")
