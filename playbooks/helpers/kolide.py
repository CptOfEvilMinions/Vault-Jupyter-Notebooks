from websocket import create_connection
import requests
import json
import ssl

def generateJSONAuthHeader(kolide_token):
  """
  Input: Takes in Kolide JWT token
  Output: Returns JSON payload for authenticating websocket to Kolide
  """
  websocket_auth_payload = {
    "type":"auth",
    "data":
      {
        "token": kolide_token
      }
  }
  return json.dumps(websocket_auth_payload)

def AuthenticateToKolide(base_url, username, passowrd):
  """
  Input: Take in Kolide base URL, username, and password
  Output: Return Kolide JWT
  https://github.com/CptOfEvilMinions/BlogProjects/blob/master/kolide-api-ansible/kolide_websocket_client.py#L127
  """
  data = {
    "Username": username,
    "Password": passowrd
  }
  url = f"{base_url}/api/v1/kolide/login"
  r = requests.post(url=url, data=json.dumps(data), verify=False)
  return r.json()['token']


def CreateLiveQuery(base_url, token, query, hosts = [], labels = []):
  """
  Input: Takes in Kolide base URL, Kolide JWT for auth, a query to run on endpoints,
  optional list of hosts, optional list of labels.
  Note: kolide_hosts or kolide_labels must be specified
  Output: Returns Kolide query campaign ID
  https://github.com/CptOfEvilMinions/BlogProjects/blob/master/kolide-api-ansible/kolide_websocket_client.py#L103
  """
  auth_header = {
    "Authorization": f"Bearer {token}"
  }
  data = {
    "query": query,
    "selected": {
      "Labels": labels, 
      "Hosts": hosts 
    }
  }
  url = f"{base_url}/api/v1/kolide/queries/run_by_names"
  r = requests.post(url=url, data=json.dumps(data), headers=auth_header, verify=False)
  return r.json()["campaign"]["id"]

def generateKoldieQueryCampaignIDJSONpayload(koldie_query_campaign_id):
  """
  Input: Takes in Kolide query campaign ID
  Output: Returns JSON payload for querying result(s) of query
  """
  koldie_query_campaign_id_payload = {
    "type":"select_campaign",
    "data":{
      "campaign_id": koldie_query_campaign_id
    }
  }
  return json.dumps(koldie_query_campaign_id_payload)
  
def GetKolideLiveQueryResults(base_url, token, query_campaign_id):
  """
  Input: Kolide base URL, Kolide JWT, query ID
  Output: Return results from websocket for query ID
  https://github.com/CptOfEvilMinions/BlogProjects/blob/master/kolide-api-ansible/kolide_websocket_client.py#L47
  """
  # Generate Kolide URL
  kolide_websocket_uri = f"wss://{':'.join( base_url.split(':')[1:])[2:]}/api/v1/kolide/results/websocket"
  
  # Disable SSL cert verification
  # Init client websocket connection
  ws = create_connection(kolide_websocket_uri, sslopt={"cert_reqs": ssl.CERT_NONE})

  # Send Kolide JWT token
  print("Sending JWT")
  ws.send(generateJSONAuthHeader(token))

  # Send campaign ID to websocket
  print("Sending campaign ID")
  ws.send(generateKoldieQueryCampaignIDJSONpayload(query_campaign_id))

  # Keep websocket until all data has been received
  print("Receiving...")
  result_list = list()
  counter = 0
  max_results = 0
  while True:
    recv_text = ws.recv()
    result = recv_text
    result = json.loads(result)
  

    # get results count
    if result.get("type") == "totals":
      max_results = result.get("data").get("count")

    # Add results to list
    if result.get("type") == "result":
      counter = counter + 1
      osq_hostname = result.get("data").get("host").get("hostname")
      osq_uuid = result.get("data").get("host").get("uuid")
      print (f"Host { osq_hostname }:{ osq_uuid } has submitted results")
      print (f"Received the following number of results: {counter}/{max_results}")
      result_list.append(result)

    # Break while
    if result.get("type") == "status" and result.get("data").get("status") == "finished":
      break

  ws.close()
  print("Close socket")
  return result_list