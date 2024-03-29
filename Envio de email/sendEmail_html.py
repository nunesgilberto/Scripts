from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()

#Chave da API do Sendinblue 
configuration.api_key['api-key'] = 'CHAVE DA API DO SENDINBLUE'
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

#Titulo do email
subject = "Campanha de Phishing"

#Código HTML do corpo do email
html_content = "<html><body><h1>Essa mensagem é um phishing. </h1></body></html>"

#Falsificando a identidade do remetente
sender = {"name":"NOME REMETENTE","email":"remetente@email.com"}

#Destinatário da campanha de Phishing
to = [{"email":"destinatario@email.com","name":"NOME DESTINATÁRIO"}]

#Destinatário em cópia
#cc = [{"email":"destinatarioemcopia@email.com","name":"DESTINATARIO EM CÓPIA"}]

#Destinatário em cópia oculta
#bcc = [{"name":"DESTINATARIO EM COPIA OCULTA","email":"destinatarioemcopiaoculta@email.com"}]

#Responder para o mesmo remetente da mensagem
reply_to = {"email":"remetente@email.com","name":"NOME REMETENTE"}

#Cabeçalho da mensagem
headers = {"Some-Custom-Name":"unique-id-1234"}
params = {"parameter":"My param value","subject":"New Subject"}

#Incluir parâmetros cc e bcc se necessário
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)

#Envio do email
try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print("Erro ao chamar a API SMTPApi->send_transac_email: %s\n" % e)