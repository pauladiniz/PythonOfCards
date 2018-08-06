from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

def find_contact(email, contact_list):
    for item in contact_list:
        if item['email'] == email:
            return item

    return {}

@app.route('/contact/')
def contact_list():
    """
    Example endpoint to return a list of contacts specified by email address.
    ---
    parameters:
      - name: email
        in: query
        type: string
        required: false
      - name: key
        in: query
        type: string
        default: teste
        required: true
    responses:
      200:
        description: A list of contacts (can be filtered by email)
        schema:
          $ref: '$/def'
    """
    email = request.args.get('email')
    api_key = request.args.get('key')
    if api_key != "teste":
        return jsonify({"error":"Bad request"}), 400
    contacts = {"contacts": [
        {'nome':'Paula', 'email': 'contato@paula.com'},
        {'nome':'Nick', 'email': 'contato@nick.com'}
    ]}
    if email == None:
        return jsonify(contacts), 200

    return jsonify({"contacts": find_contact(email, contacts["contacts"])}), 200


if __name__ == '__main__':
    app.run(debug=True)
