# settyl_assignment
This is a simple Flask application that acts as a webhook endpoint for validating HSN codes using an Excel master data file. It is designed to integrate with Dialogflow CX via webhooks or can be tested standalone using Postman.

Features
Validates user-provided HSN codes

Reads data from HSN_SAC_Mstr.xlsx using pandas

Provides description for valid HSN codes

Returns a friendly error for invalid codes

Easily deployable as a webhook for conversational agents

📁 Project Structure
.
├── webhook.py              # Main Flask app
├── HSN_SAC_Mstr.xlsx       # Master data file with HSN codes and descriptions
├── requirements.txt        # Python package dependencies
└── README.md               # This file

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/hsn-validator.git
cd hsn-validator

3. Install dependencies
Ensure you have Python 3.8 or above installed.
pip install -r requirements.txt

3. Add your Excel file
Place the HSN_SAC_Mstr.xlsx file (with columns like HSNCode and Description) in the root directory.

4. Run the Flask app
python webhook.py
The server will start on http://localhost:8000.

📬 API Endpoint
POST /webhook
Expected JSON request:
{
  "fulfillmentInfo": {
    "tag": "validate_hsn_code"
  },
  "sessionInfo": {
    "parameters": {
      "hsn_code": "01"
    }
  }
}

Example Response:
{
  "fulfillment_response": {
    "messages": [
      {
        "text": {
          "text": ["The HSN code 01 is valid. Description: LIVE ANIMALS"]
        }
      }
    ]
  }
}


📖 License
MIT License. Feel free to use, modify, and distribute.

