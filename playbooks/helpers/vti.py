import requests

def GetVTIresults(VTI_API_KEY, sha256_file_hash):
  """
  Input: Take in API key and SHA256 file hash
  Output: Return VTI report for the SHA256 file hash provided
  """
  auth_header = {
      "x-apikey": VTI_API_KEY
  }
  url = f"https://www.virustotal.com/api/v3/files/{sha256_file_hash}"
  r = requests.get(url=url, headers=auth_header)
  return r.json()