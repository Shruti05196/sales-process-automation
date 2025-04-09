import pandas as pd

# Load the dummy LinkedIn data
df = pd.read_excel("linkedin_dummy_data.xlsx")

# Load the HTML email template
with open("email_template.html", "r", encoding="utf-8") as file:
    template = file.read()

# Generate personalized emails
for index, row in df.iterrows():
    email_body = template
    email_body = email_body.replace("[Recipient Name]", row["Contact Person"])
    email_body = email_body.replace("[Company Name]", row["Company Name"])
    email_body = email_body.replace("[Industry]", row["Industry"])
    email_body = email_body.replace("[Location]", row["Location"])

    # Save each personalized email as an HTML file
    with open(f"email_{index + 1}.html", "w", encoding="utf-8") as output:
        output.write(email_body)

print("✅ Personalized emails generated successfully!")
