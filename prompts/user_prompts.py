def get_links_user_prompt(website):
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += "please decide which of these are relevant web links for generating a personalized mail for product recommendation to customers, respond with the full https URL in JSON format. \
        Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt

def generate_mail_user_prompt(details, url):
    user_prompt = f"Based on the information provided on the website {url}, please generate a personalized sales email for the company's product. \
        The email should be engaging, informative, and encourage the recipient to take action. \
        Respond with the email content in plain text format.\n"
    user_prompt += details
    user_prompt += user_prompt[:20000]
    return user_prompt

def email_footer_user_prompt(mail_content, your_name, designation, contact_info):
    user_prompt = "If receipent information not availabe keep the greetings as it is.\n"
    user_prompt += f"Modify the mail footer/header or in-between missing variables present in the mail based on the given info for your name:{your_name}, designation:{designation}, contact_info:{contact_info}:\n"
    user_prompt += "**Do not modify the mail other than above mentioned changes**.\n"
    user_prompt += mail_content
    return user_prompt