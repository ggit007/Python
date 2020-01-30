class SalesforceConnector:

    import requests as req
    
    #print('req***** ',help(req.utils))
    client_id = '3MVG9ZL0ppGP5UrCZ3e21E0nM7U.w9A5ZlFXys6E9OUrUmby19Tihxw88G6R0AXhqeX6l3ZzX2g=='
    client_secret = '2152073599418201878'
    redirect_uri = 'https://boltmup-dev-ed.my.salesforce.com/services/oauth2/success'
    sfdc_username = 'kr.gaurav9999@ymail.com'
    password = 'Gaurav12@'
    
    auth_uri = 'https://login.salesforce.com/services/oauth2/token'
    try:
        response = req.post(auth_uri, data = {
                            'client_id' : client_id,
                            'client_secret' : client_secret,
                            'grant_type' : 'password',
                            'username' : sfdc_username,
                            'password' : password
        })
        
        #print('response*******',help(response))
        #print('status code******* ',response.status_code)
        if response.status_code == 200:
            json_response = response.json()
            print('json_response***** ',json_response)
            access_token = json_response['access_token']
            instance_url =  json_response['instance_url']
            token_type = json_response['token_type']    #Bearer
            auth = {'Authorization':token_type+' '+access_token}
            
            url = instance_url + '/services/data/v47.0/query/?q=SELECT+Name+FROM+Account LIMIT 10'
            data_response = req.get(url, headers=auth)
            data_reponse_json = data_response.json()
            #print('data_response_status@@@@@@@@@@@ ',data_response.json())
            #print('data_response@@@@@@@@@@@',data_response.json()['totalSize'])
            #print('data_response@@@@@@@@@@@',data_response.json()['records'])
            for each in data_reponse_json['records']:
                print('%%%%% ',each['Name'])
        else:
            print('Error code: ',response.status_code)
    except:
        raise Exception('Error code: ',response.status_code)
