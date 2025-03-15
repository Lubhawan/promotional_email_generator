from email_content_generator import Email_Ad_Generator
from emailer import EmailSender
from prompts.system_prompts import email_generation_system_prompt

def main():
    your_name = input("Enter your name: ")
    designation = input("Enter your designation: ")
    contact_info = input("Enter your contact information: ")

    url = input("Enter the URL of the company website: ")
    email_ad_generator = Email_Ad_Generator(url)
    email_container = email_ad_generator.edit_final_mail(your_name, designation, contact_info)

    email_sender = EmailSender("lubhawan.meena@gmail.com", "mthmkbteelghksqx")
    email_sender.send_email("lubhawanp@gmail.com", email_container['subject'], email_container['email_body'])

if __name__ == "__main__":
    main()