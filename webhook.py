from flask import Flask, request, jsonify
import pandas as pd

hsn_data = pd.read_excel("HSN_SAC_Mstr.xlsx", engine='openpyxl')

app = Flask(__name__)

def validate_hsn_code(hsn_code):
    if hsn_code in hsn_data['\nHSNCode'].values:
        return hsn_data[hsn_data['\nHSNCode'] == hsn_code]['Description'].values[0]
    return None

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    tag = req.get('fulfillmentInfo', {}).get('tag')

    # Extract parameters from the session
    session_params = req.get('sessionInfo', {}).get('parameters', {})

    # Dialogflow CX will send based on fulfillment tag
    if tag == 'validate_hsn_code':
        hsn_code = session_params.get('hsncode')
        description = validate_hsn_code(hsn_code)

        if description:
            response_text = f"The HSN code {hsn_code} is valid. Description: {description}"
        else:
            response_text = f"The HSN code {hsn_code} is invalid."

        return jsonify({
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": [response_text]
                        }
                    }
                ]
            }
        })

    return jsonify({
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": ["Webhook tag not recognized."]
                    }
                }
            ]
        }
    })

if __name__ == '__main__':
    app.run(port=8000)
