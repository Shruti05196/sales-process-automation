# 📌 Sales Process Automation using Python

This project automates the sales outreach process — from scraping business leads to sending personalized emails and tracking responses — all using Python.

---

## 🎯 Objective

To demonstrate an automated pipeline that:
- Collects business leads from the web (LinkedIn/Google/Justdial)
- Exports lead data to Excel
- Generates personalized HTML email templates
- Sends emails using Gmail SMTP
- Simulates email analytics and lead scoring

---

## 🛠️ Tech Stack

- **Python**  
- **Selenium + BeautifulSoup** (Web scraping)  
- **Pandas** (Excel and data handling)  
- **smtplib + email** (Automated email sending)  
- **HTML** (Dynamic email templates)  

---

## 📂 Project Structure

| File / Folder              | Description                                      |
|----------------------------|--------------------------------------------------|
| `linkedin_scraper.py`      | Scrapes profile links from Google (LinkedIn)     |
| `linkedin_dummy_data.xlsx` | Dummy business leads for email testing           |
| `email_template.html`      | Custom HTML email template with placeholders     |
| `generate_emails.py`       | Replaces placeholders and creates HTML emails    |
| `send_emails.py`           | Sends personalized emails using Gmail SMTP       |
| `email_analytics.csv`      | Simulated analytics: opened, replied, lead stage |

---

## 🔥 Features

- Business data scraping from multiple sources  
- Data cleaning and Excel export  
- Personalized email generation using dynamic fields  
- One-click email campaign execution using Gmail  
- Lead categorization (Hot/Warm/Cold) using simulated analytics

---

## 📽️ Demo

▶️ [Click here to watch the demo video](https://drive.google.com/file/d/1mwen73xLHHBI7aCdLZnV0osjUsuiMy58/view?usp=drive_link)

---

## 📊 Email Campaign Analytics Summary

- **Total Emails Sent:** 6  
- **Emails Opened:** 4  
- **CTA Clicked:** 2  
- **Open Rate:** 66.6%  
- **Click-Through Rate (CTR):** 33.3%  
- **Hot Leads:** 2  
- **Warm Leads:** 2  
- **Cold Leads:** 2  

> These metrics were simulated using dummy analytics data to showcase lead engagement tracking.

---

## 🔮 Future Scope (AI/ML Integration)

While this version focuses on Python-based automation, it is fully adaptable for AI/ML enhancements. Future versions can include:

- **Lead Scoring using ML:** Train a classification model to score leads as Hot/Warm/Cold based on behavior, industry, and engagement.
- **Email Sentiment Analysis (NLP):** Use AI to analyze email replies and classify intent (positive, negative, neutral).
- **Smart Response Suggestion:** Integrate with GPT APIs to generate AI-based reply suggestions for inbound messages.
- **Reply Prediction Model:** Predict the probability of a lead replying based on past campaign data.
- **Opt-in Behavior Analysis:** Cluster similar leads using unsupervised ML based on ICP features and response trends.

> These upgrades can help turn the project into a full AI-driven sales assistant platform.

---

## 🧠 Skills Demonstrated

- Python scripting and modular coding
- Web scraping using BeautifulSoup and requests
- Email automation using smtplib and email.message
- Secure credential management via .env
- Personalized email generation using HTML templates
- Data analytics with pandas
- Categorizing leads based on engagement (Hot/Warm/Cold)
- GitHub documentation and video demo submission

---

## 👩‍💻 Author

**Shruti Undhad**  
Python Developer | Final Year CSE Student  
[GitHub Profile](https://github.com/Shruti05196)
