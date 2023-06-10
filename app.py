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
    #temp_file_path = os.path.join(tempfile.gettempdir(), 'v2ray_config.json')
    json_list = load_v2ray_config()
    if json_list is not None:
        # Convert each item to a string 
        items = [json.dumps(item) for item in json_list]

        result = []
        for json_str in items:   
            # Concatenate 'vmess://' as prefix        
            encoded_text =  base64.b64encode(json_str.encode('utf-8'))    
            encoded_text = 'vmess://' + encoded_text.decode('utf-8')

            # Concatenate newline as postfix
            encoded_text += '\n'
            
            result.append(encoded_text)

        ret = ''.join(result)
        return ret
        



        #json_str = json.dumps(json_list)
        #text = '{ "v": "2", "ps": "JPE2", "add": "52.140.199.214", "port": "47330", "id": "b0f229a6-f383-40f0-b467-79ff45973320", "aid": "0", "scy": "auto", "net": "tcp", "type": "none", "host": "", "path": "", "tls": "", "sni": "", "alpn": "", "fp": "" }'
        #encoded_text =  base64.b64encode(json_str.encode('utf-8'))    
        #return 'vmess://'+ encoded_text.decode('utf-8')
    else:
        return "it's fresh here"

    
@app.route("/updateip", methods=['GET'])            
def updateip():
    if request.method == 'GET':
        addr = request.args.get('addr')
        loc = request.args.get('loc').upper()
        match loc:
            case "USW2":
                json_item_template = '{ "v": "2", "ps": "USW2", "add": "", "port": "47330", "id": "1a6511b4-6bfa-4836-896f-51f66491250f", "aid": "0", "scy": "auto", "net": "tcp", "type": "none", "host": "", "path": "", "tls": "", "sni": "", "alpn": "", "fp": "" }'
            case "JPE2":
                json_item_template = '{ "v": "2", "ps": "JPE2", "add": "", "port": "47330", "id": "b0f229a6-f383-40f0-b467-79ff45973320", "aid": "0", "scy": "auto", "net": "tcp", "type": "none", "host": "", "path": "", "tls": "", "sni": "", "alpn": "", "fp": "" }'
        #swtch by loc to update the ip, if loc='usw2' then use usw2 json_usw2 string, if loc='jep' then use json_jep string
        new_obj  = json.loads(json_item_template)
        new_obj['add'] = addr

        json_list = load_v2ray_config()
        if json_list is not None:        
            exist_obj = get_item(json_list, loc)
            if exist_obj is not None:
                exist_obj.update(new_obj)
            else:
            # Append the new object
                json_list.append(new_obj)
        else:
            # Append the new object
            json_list=[new_obj]



            

        # Encode to base64    
        b64_json = base64.b64encode(json.dumps(json_list).encode())

        # code to Write to file using fs module to a temp file
        temp_file_path = os.path.join(tempfile.gettempdir(), 'v2ray_config4.json')
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

def load_v2ray_config():
    temp_file_path = os.path.join(tempfile.gettempdir(), 'v2ray_config4.json')
    if os.path.exists(temp_file_path):
        with open(temp_file_path, 'rb') as f:
            b64_json = f.read()

        json_list = json.loads(base64.b64decode(b64_json).decode())
        return json_list
    else:
        return None

def get_item(json_list: list, ps: str):
    try:
        for item in json_list:
            if item['ps'] == ps:
                return item
        return None
    except:            
        return None

if __name__ == "__main__":
    app.run(debug = True)