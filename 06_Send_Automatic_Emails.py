import smtplib
import getpass

def automatic_email():
    email = input("Enter Your Email: ")
    receiver_email = input("Enter Receiver Email: ")

    subject = input("Subject: ")
    message = input("Message: ")

    text = f"Subject: {subject}\n\n{message}"

    try:
        # Connecting to Gmail Server
        s = smtplib.SMTP("smtp.gmail.com", 587)

        # Starting TLS Encryption
        s.starttls()

        # Logging into Gmail (securely)
        password = getpass.getpass("Enter Your Password: ")
        s.login(email, password)

        # Sending Email
        s.sendmail(email, receiver_email, text)

        print(f"Email has been sent to {receiver_email}")

    except smtplib.SMTPAuthenticationError:
        print("Error: Invalid email or password.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    finally:
        # Closing the server
        s.quit()

if __name__ == "__main__":
    automatic_email()