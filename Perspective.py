from googleapiclient import discovery
import json


class PerspectiveClient:
  pass

text=' fuck you'

API_KEY = 'AIzaSyDcalBRDF8mvybVc9_-2bAh9BdNiWT-iBE'

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

analyze_request = {
  'comment': {'text': text},
  'requestedAttributes': {'TOXICITY': {}}
}

response = client.comments().analyze(body=analyze_request).execute()
print(json.dumps(response, indent=2))