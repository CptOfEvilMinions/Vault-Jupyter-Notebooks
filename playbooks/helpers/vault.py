import requests

def GetVaultSecrets(VAULT_ADDR, VAULT_SECRET_PATH, VAULT_TOKEN):
  """
  Input: Take in Vault URL address, path to secrets, and user's token
  Output: Return dictoanry of secrets for the path provided
  """
  auth_header = {
      "X-Vault-Token": VAULT_TOKEN
  }
  url = f"{VAULT_ADDR}/v1{VAULT_SECRET_PATH}"
  print (url)
  r = requests.get(url=url, headers=auth_header)
  return r.json()['data']['data']