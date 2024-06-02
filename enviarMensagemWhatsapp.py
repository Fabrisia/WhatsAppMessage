import pandas as pd
from twilio.rest import Client

# Configuração do Twilio
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)
from_whatsapp_number='whatsapp:+1XXXXXXXXXX'  # Seu número do Twilio WhatsApp

# Lendo o arquivo Excel
df = pd.read_excel('caminho_para_seu_arquivo.xlsx', engine='openpyxl')

# Enviando mensagens de WhatsApp
for index, row in df.iterrows():
    contato = str(row['CONTATO'])
    if contato.startswith('+'):  # Verifica se o contato tem o formato internacional
        message = client.messages.create(
            body="Sua mensagem aqui",  # Texto da mensagem que você quer enviar
            from_=from_whatsapp_number,
            to=f'whatsapp:{contato}'
        )
        print(f'Mensagem enviada para {contato} com SID {message.sid}')
    else:
        print(f'Número de contato inválido: {contato}')

print("Todas as mensagens foram enviadas.")
