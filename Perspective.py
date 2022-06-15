from googleapiclient import discovery
import pandas as pd
import json
import time



def PerspectiveClient(text):



  #API_KEY = 'AIzaSyDcalBRDF8mvybVc9_-2bAh9BdNiWT-iBE'
  API_KEY = 'AIzaSyDeq5usFqUj8o_xS9X57XlH0ubliprumy4'

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
  #print(json.dumps(response, indent=2))
 
  for k,v in response['attributeScores'].items():
  
    toxicity_value=v['summaryScore']['value']
    # print(">>>>>>>>>")
    # print( toxicity_value )
    # print(">>>>>>>>>")

  return toxicity_value
  




posts_df=pd.read_csv('politics_hot_comments_praw.csv')
print(posts_df)

# posts_df['toxicity'] = 0
posts_df.insert(2,'toxicity',0.0)
print(posts_df)
for post, post_row in posts_df.iterrows():
  text= post_row['body']
  print("post: ",post)
  # print(text)
  
  try:
    toxicity_v=PerspectiveClient(text)
  except:
    toxicity_v=0.0
  
  time.sleep(1) # Sleep for 1 second
  print(toxicity_v)
  posts_df.at[post,'toxicity']=float(toxicity_v)
  # index = posts_df.index
  # posts_df['toxicity'][index] = toxicity_v
  # print(toxicity_v)


  # if(post==1000):
  #   break

  
 

print(posts_df)
# text="you're lovely"
posts_df.to_csv('politics_hot_comments_praw_toxic.csv', header=True, index=False)