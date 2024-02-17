import requests
from fastapi import HTTPException

def send_reset_email(to_email: str, reset_link: str):
    api_key = "3dce6b8bae3341d1b380357c5340ab52-1900dca6-4f316e8b"  # Replace with your MailGun API key
    print(to_email)
    # MailGun API endpoint
    api_url = f"https://api.mailgun.net/v3/sandbox25a06c31840743d39fe28d0f030e4cc2.mailgun.org/messages"

    # MailGun API key and parameters
    auth = ("api", api_key)

    # HTML content for the email
    html_content = f"""
    <html>
    <body style="font-family:montserrat; text-align: center;">
        <img src="https://res.cloudinary.com/dtk8amipr/image/upload/v1704668946/logo-no-background_ekm7jh.png" alt="Hiro Logo" style="width: 150px; height: 100px;object-fit:contain;">
        <h2>Password Reset</h2>
        <p>Hello there!</p>
        <p>We hope this message finds you well. You've requested to reset your password for Hiro, your mental health bot.</p>
        <p>Click the following link to reset your password:</p>
        <p><a href="{reset_link}" style="text-decoration: none; color: #3498db;">Reset Password</a></p>
        <p>This magic link is valid for 10 minutes only.</p>
        <p>If you didn't request this, no worries! Your account is still safe and sound.</p>
        <p>Stay positive and take care of yourself!</p>
        <p>Best regards,<br>Team Hiro</p>
    </body>
    </html>
    """

    # MailGun API parameters with HTML content
    data = {
        "from": "rohkumar0126@gmail.com",  # Replace with your email
        "to": to_email,
        "subject": "Password Reset",
        "html": html_content,
    }

    # Send the email
    response = requests.post(api_url, auth=auth, data=data)

    # Check for errors
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to send reset email")

# Usage example:
# send_reset_email("recipient@example.com", "https://example.com/reset/123456")
