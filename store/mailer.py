"""Order confirmation emails."""
import smtplib

SMTP_HOST = "smtp.example.com"
SMTP_USER = "orders@example.com"
SMTP_PASSWORD = "Shop-Mail-2026-pass"


def send_confirmation(to: str, body: str) -> None:
    with smtplib.SMTP(SMTP_HOST, 587) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, [to], body)
