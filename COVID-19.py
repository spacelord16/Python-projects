import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message


app = Flask(__name__)
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


# Take the text message sent by the user and return a string with the results.
def get_stats_message(message):
    if message in states:
        resp = requests.get('https://covidtracking.com/api/states').json()

        # Get the data for the given State.
        for state_data in resp:
            # Figure out which State we're looking at.
            if message == state_data['state']:
                data = state_data
        return ('In {state} so far, {total} tests have been given with ' +
                '{positive} confirmed positive cases.\n\n{hospitalized}' +
                ' have been hospitalized so far with {death} deaths.') \
                .format(**data)

    # Return nation-wide data if no valid State was given.
    resp = requests.get('https://covidtracking.com/api/us').json()
    data = resp[0]
    return ('In the US so far, {total} tests have been given with ' +
           '{positive} confirmed positive cases.\n\n{hospitalized}' +
           ' have been hospitalized so far with {death} deaths.') \
           .format(**data)


@app.route('/sms', methods=['POST'])
def inbound_sms():
    # Grab the text from the received message.
    message_body = request.form['Body']

    # Generate a TwiML Response object with the message we want to send.
    twiml_resp = MessagingResponse()
    twiml_resp.message(get_stats_message(message_body))
    return str(twiml_resp)