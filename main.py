import os
import yagmail
from dotenv import load_dotenv
import pandas as pd

# Load variables from .env file
load_dotenv()

# Fetch email and password from .env
EMAIL = os.getenv("USER_EMAIL")
PASSWORD = os.getenv("USER_PASS")

Emails = pd.read_excel("formData.xlsx", usecols=["emails"]);

# Initialize Yagmail client
yag = yagmail.SMTP(EMAIL, PASSWORD)

# Send email

for index, row in Emails.iterrows():
    try:
        yag.send(
        to=row["emails"],
        subject="Hello from Python #test01",
        contents="This email was sent using credentials stored in a .env file!"
        )
        print("Email sent successfully to: ",row["emails"]);
    except:
        print("Email Sent not successful for: ",row["emails"]);
