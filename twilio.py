from twilio.rest import Client

account_sid = 'ACd521f5e926b76a3cad16dcdde966386a'
auth_token = '422c0e665f1bd13a3f7b03530ea4d689'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+14252463728',
) 

print(message.sid)