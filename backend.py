from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

EMAIL_ADDRESS = os.getenv('info@integrapvtltd.com')
EMAIL_PASSWORD = os.getenv('@Purchased1@integra')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.hostinger.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 465))

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    project = data.get("project")
    message = data.get("message")

    try:
        msg = EmailMessage()
        msg['Subject'] = 'New Contact Form Submission'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg.set_content(f"""New contact form message:

Full Name: {name}
Email: {email}
Mobile: {phone}
Project Type: {project}
Message: {message}
""")

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
