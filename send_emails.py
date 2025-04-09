import smtplib
import ssl
import pandas as pd
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Secure credentials from .env
sender_email = os.getenv("EMAIL_ID")
app_password = os.getenv("APP_PASSWORD")

# Load data
df = pd.read_excel("linkedin_dummy_data.xlsx")

# Load email template
with open("email_template.html", "r", encoding="utf-8") as f:
    html_template = f.read()

# SMTP setup
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
server.login(sender_email, app_password)

# Send emails
for index, row in df.iterrows():
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = "undhadshruti9060@gmail.com"  # ✅ Testing email is okay
    msg['Subject'] = f"Hi {row['Contact Person']}, Let's talk about {row['Company Name']}"

    html_content = html_template
    html_content = html_content.replace("[Recipient Name]", row["Contact Person"])
    html_content = html_content.replace("[Company Name]", row["Company Name"])
    html_content = html_content.replace("[Industry]", row["Industry"])
    html_content = html_content.replace("[Location]", row["Location"])

    msg.set_content("This email requires HTML support.")
    msg.add_alternative(html_content, subtype='html')

    server.send_message(msg)
    print(f"✅ Email sent to: {row['Contact Person']}")

server.quit()
print("📬 All emails sent successfully!")
