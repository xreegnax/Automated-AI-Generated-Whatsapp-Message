from twilio.rest import Client

account_sid = 'Type your twilio account_sid here'
auth_token = 'Type your twilio account auth_token here'
twilio_number = 'Type your twilio_number here'

def send_whatsapp_message(message):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='whatsapp:' + twilio_number,
        to='whatsapp:' + to_number
    )

    print(f"Message sent to {to_number} with SID: {message.sid}")

# Example usage
to_number = '+123456789'  # Replace with your WhatsApp number
