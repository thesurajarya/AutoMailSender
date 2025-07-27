# AutoMailSender

# 📧 Python Bulk Email Sender using Excel + .env + Yagmail

Send personalized emails to multiple recipients stored in an Excel sheet using Python — **securely and efficiently**.


## 🚀 Features

- 🔐 Uses a `.env` file to keep your email and password secure.
- 📊 Reads email addresses from an Excel file (`fileName.xlsx`).
- 💌 Sends emails using Gmail via `yagmail`.
- ✅ Logs the success or failure of each sent email.

How To Use:

Step 1: Make `.env` file, containing sender's gmail and App Password.

        (you can make one app password for your account from https://myaccount.google.com/apppasswords)

`.env` file structure:

        USER_EMAIL = SENDER_GMAIL_ADDRESS
        USER_PASS = SENDER_APP_PASSKEY (16 digits)

Step 2: Create excel file with receiver's email addresses.

Step 3: Name the column as `emails` which contains `all the receiver's email`

Step 4: Keep all the files in same folder.

Step 5: Run `main.py`

NOTE: make sure you have installed all the libraries beforehand.
      If not, then paste this command in terminal.

      pip install pandas openpyxl yagmail python-dotenv

There you go... Have Fun!

Author: Suraj Arya (https://github.com/thesurajarya)
        

