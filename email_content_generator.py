import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from web_scrapper import Website
from prompts.system_prompts import link_system_prompt, email_generation_system_prompt, email_footer_editor
from prompts.user_prompts import get_links_user_prompt, generate_mail_user_prompt, email_footer_user_prompt

# Initialize and constants

class Email_Ad_Generator:
    def __init__(self, url):
        load_dotenv(override=True)
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.MODEL = 'gpt-4o-mini'
        self.openai = OpenAI()
        self.url = url

    def get_links(self):
        website = Website(self.url)
        response = self.openai.chat.completions.create(
            model=self.MODEL,
            messages=[
                {"role": "system", "content": link_system_prompt},
                {"role": "user", "content": get_links_user_prompt(website)}
            ],
            response_format={"type" : "json_object"}
        )

        result = response.choices[0].message.content

        return json.loads(result)

    def collect_data_from_urls(self):
        result = "Landing Page"
        result += Website(self.url).get_contents()
        extracted_links = self.get_links()
        # print(extracted_links)
        for link in extracted_links['links']:
            result += f"\n\n{link['type']}\n"
            result += Website(link['url']).get_contents()
        return result

    def create_mail(self):        
        response = self.openai.chat.completions.create(
            model=self.MODEL,
            messages=[
                {"role": "system", "content": email_generation_system_prompt},
                {"role": "user", "content": generate_mail_user_prompt(self.collect_data_from_urls(), self.url)}
            ]
        )
        result = response.choices[0].message.content
        return result
    
    def edit_final_mail(self, your_name, designation, contact_info):
        response = self.openai.chat.completions.create(
            model=self.MODEL,
            messages=[
                {"role": "system", "content": email_footer_editor},
                {"role": "user", "content": email_footer_user_prompt(self.create_mail(), your_name, designation, contact_info)}
            ],
            response_format={"type" : "json_object"}
        )
        result = response.choices[0].message.content
        return json.loads(result)