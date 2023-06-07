import openai

openai.api_key = 'Type your Open AI API key here'
from whatsapp import send_whatsapp_message


def ask_question(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
    )

    answer = response.choices[0].message.content
    return answer

a = "y"
while a not in ['no', 'n', 'No', 'Nope']:
    user_question = input("What is your question? ")
    question = user_question + "in under 1500 characters"
    answer = ask_question(question)
    answer = user_question + "\n\n" + answer
    send_whatsapp_message(answer)
    a = input('Do you want to ask another question?')
