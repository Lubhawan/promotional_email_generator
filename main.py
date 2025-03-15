from email_content_generator import Email_Ad_Generator
from emailer import EmailSender
import os

def main():
    recipient_email = input("Enter the email address of the recipient: ")

    your_name = input("Enter your name: ")
    designation = input("Enter your designation: ")
    contact_info = input("Enter your contact information: ")

    url = input("Enter the URL of the company website: ")
    email_ad_generator = Email_Ad_Generator(url)
    email_container = email_ad_generator.edit_final_mail(your_name, designation, contact_info)

    email_sender = EmailSender(os.getenv('SENDER_MAIL'), os.getenv('SENDER_MAIL_PASSWORD'))
    email_sender.send_email(recipient_email, email_container['subject'], email_container['email_body'])

if __name__ == "__main__":
    main()