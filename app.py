from flask import Flask, request
import base64
import json
import os
import tempfile

app = Flask(__name__)

# create a json object from text: '{ "v": "2", "ps": "JPE2", "add": "52.140.199.214", "port": "47330", "id": "b0f229a6-f383-40f0-b467-79ff45973320", "aid": "0", "scy": "auto", "net": "tcp", "type": "none", "host": "", "path": "", "tls": "", "sni": "", "alpn": "", "fp": "" }'


@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'this is a ledder to freedom'

@app.route("/get_config", methods=['GET'])  
def base64_encode():

    """     
    if request.method == 'POST':
        text = request.form['text']
        encoded_text = base64.b64encode(text.encode('utf-8'))
        return encoded_text.decode('utf-8')
    else:
        return '''
            <form method="POST">
                Text: <input name="text">
                <input type="submit">
            </form>
        ''' 
    """
    temp_file_path = os.path.join(tempfile.gettempdir(), 'v2ray_config.json')
    if os.path.exists(temp_file_path):
        with open(temp_file_path, 'rb') as f:
            b64_json = f.read()
        
        json_obj = json.loads(base64.b64decode(b64_json).decode())
        json_str = json.dumps(json_obj)

        #text = '{ "v": "2", "ps": "JPE2", "add": "52.140.199.214", "port": "47330", "id": "b0f229a6-f383-40f0-b467-79ff45973320", "aid": "0", "scy": "auto", "net": "tcp", "type": "none", "host": "", "path": "", "tls": "", "sni": "", "alpn": "", "fp": "" }'
        encoded_text =  base64.b64encode(json_str.encode('utf-8'))    
        return 'vmess://'+ encoded_text.decode('utf-8')
    else:
        return "it's fresh here"

@app.route("/ssr", methods=['GET'])  
def get_ssr():

    """     
    if request.method == 'POST':
        text = request.form['text']
        encoded_text = base64.b64encode(text.encode('utf-8'))
        return encoded_text.decode('utf-8')
    else:
        return '''
            <form method="POST">
                Text: <input name="text">
                <input type="submit">
            </form>
        ''' 
    """
    temp_file_path = os.path.join(tempfile.gettempdir(), 'v2ray_config.json')
    if os.path.exists(temp_file_path):
        with open(temp_file_path, 'rb') as f:
            b64_json = f.read()
        
        json_obj = json.loads(base64.b64decode(b64_json).decode())
        json_str = json.dumps(json_obj)

        #text = '{ "v": "2", "ps": "JPE2", "add": "52.140.199.214", "port": "47330", "id": "b0f229a6-f383-40f0-b467-79ff45973320", "aid": "0", "scy": "auto", "net": "tcp", "type": "none", "host": "", "path": "", "tls": "", "sni": "", "alpn": "", "fp": "" }'
        encoded_text =  base64.b64encode(json_str.encode('utf-8'))    
        return 'ssr://'+ encoded_text.decode('utf-8')
    else:
        return "it's fresh here"
    
@app.route("/updateip", methods=['GET'])
def updateip():
    if request.method == 'GET':
        text = request.args.get('text')
          

        json_str = '{ "v": "2", "ps": "JPE2", "add": "", "port": "47330", "id": "b0f229a6-f383-40f0-b467-79ff45973320", "aid": "0", "scy": "auto", "net": "tcp", "type": "none", "host": "", "path": "", "tls": "", "sni": "", "alpn": "", "fp": "" }'
        json_obj = json.loads(json_str)
        json_obj['add'] = text

        # Encode to base64    
        b64_json = base64.b64encode(json.dumps(json_obj).encode())

        # code to Write to file using fs module to a temp file
        temp_file_path = os.path.join(tempfile.gettempdir(), 'v2ray_config.json')
        with open(temp_file_path, 'wb') as f:
            f.write(b64_json)
        
        return 'ok'
    else:
        return '''
            <form method="POST">
                Text: <input name="text">
                <input type="submit">
            </form>
        '''


if __name__ == "__main__":
    app.run(debug = True)