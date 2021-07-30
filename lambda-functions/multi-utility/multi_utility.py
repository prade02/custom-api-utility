import json
import base64

def base64_process(action, message):
    try:
        if action == 'encode':
            print(f'New base64 encode request for: {message}')
            base64_encoded = base64.b64encode(message.encode('utf-8'))
            print('base64 conversion successfull')
            return {'result': base64_encoded.decode('utf-8')}
        elif action == 'decode':
            print(f'New base64 decode request for: {message}')
            base64_decoded = base64.b64decode(message.encode('utf-8'))
            print('base64 decode successfull')
            return {'result': base64_decoded.decode('utf-8')}
        else:
            return {'result': 'no change in message. action not valid'}
    except Exception as e:
        print(f'error while base64 encoding: {e}')
     
        
def respond(message, error=False):
    response_code = 200 if not error else 503
    return {
        'statusCode': response_code,
        'headers': {
            'Access-Control-Allow-Headers' : 'Content-Type',
            'Access-Control-Allow-Origin': '*', 
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps(message)
    }
        
        
def handler(event, context):
    print(event)
    # set a dummy result - this will be the response if action in request does not match with lambda
    result = 'test response'
    action = 'default'
    # try to get action from body - this should be set by the client body:{'action':'some-action'}. if not action is set then return error message
    raw_body = json.loads(event['body'])
    if raw_body is not None and type(raw_body) is not dict:
        return respond('invalid data in request', True)
    # check action and call respective module
    if 'resource' not in raw_body or 'action' not in raw_body:
        return respond(result)
    resource = raw_body['resource']
    action = raw_body['action']
    if resource == 'base64':
        if 'message' not in raw_body:
            return respond('missing message in request', True)
        result = base64_process(action, raw_body['message'])
        return respond(result)
    
    return respond(result)
