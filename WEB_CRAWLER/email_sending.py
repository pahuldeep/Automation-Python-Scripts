import argparse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender_email, recipient_email, password, file_path, subject):
    # Create the MIMEMultipart object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the file
    with open(file_path, 'rb') as f:
        attachment = MIMEApplication(f.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
    msg.attach(attachment)

    # Connect to the server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Puts the connection into TLS mode

    # Login to the server
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

    print("Email sent successfully!")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Send an email with an attachment via Gmail.")
    parser.add_argument('sender_email', type=str, help='Sender email address')
    parser.add_argument('recipient_email', type=str, help='Recipient email address')
    parser.add_argument('password', type=str, help='Password for the sender email address')
    parser.add_argument('file_path', type=str, help='Path to the file to attach')
    parser.add_argument('subject', type=str, help='Subject of the email')

    args = parser.parse_args()

    # Call the send_email function with the parsed arguments
    send_email(args.sender_email, args.recipient_email, args.password, args.file_path, args.subject)
