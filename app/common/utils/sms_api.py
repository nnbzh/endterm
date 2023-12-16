import requests


def send_authorization_sms(recipient, code):
    body = {
        'recipient': recipient,
        'text': code
    }

    response = requests.post(
        'https://api.mobizon.kz/service/message/sendSmsMessage?'
        'output=json'
        '&api=v1'
        '&apiKey=kz1e2c66557aaedf6e1aee165e384787b8148980bd3e878775398852115318dfc0d0f4',
        body
    )
    # TODO: PARSE JSON RESPONSE
    return response
