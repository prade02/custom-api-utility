import json
import base64

def base64_encode(input):
    try:
        print(f'New base64 encode request for: {input}')
        base64_encoded = base64.b64encode(input.encode('utf-8'))
        print('base64 conversion successfull')
        return {'result': base64_encoded.decode('utf-8')}
    except Exception as e:
        print(f'error while base64 encoding: {e}')
     
        
def respond(message, error=False):
    response_code = 200 if not error else 503
    return {
        'statusCode': response_code,
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
    if 'action' not in raw_body:
        return respond(result)
    action = raw_body['action']
    if action == 'base64-encode':
        if 'message' not in raw_body:
            return respond('missing message in request', True)
        result = base64_encode(raw_body['message'])
        return respond(result)
    
    return respond(result)
