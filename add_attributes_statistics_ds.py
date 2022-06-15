import pandas as pd

trees_df=pd.read_csv('ukraine_cntr_statistics.csv')
print(trees_df)

comments_df=pd.read_csv('ukraine_cntr_comments_praw_toxic.csv')
print(comments_df)

posts_df=pd.read_csv('ukraine_cntr_posts_praw_toxic.csv')
print(posts_df)


trees_df.insert(5,'low_ratio',0.0)
trees_df.insert(6,'high_ratio',0.0)
trees_df.insert(7,'toxic_ratio',0.0)
trees_df.insert(8,'score_votes',0)
trees_df.insert(9,'upvote_ratio',0.0)

for post, post_row in posts_df.iterrows():
    low_toxic_comments=0
    high_toxic_comments=0
    total_comments=0
    score_votes=post_row['score']
    upvote_ratio=post_row['upvote_ratio']
    for comment, row in comments_df.iterrows():
        if (post_row['post_id']==row['parent_id']):

            total_comments+=1
            if row['toxicity']>0.3 and row['toxicity']<=0.5:
                low_toxic_comments+=1
            if row['toxicity']>0.5:
                high_toxic_comments+=1
    low_ratio="{:.2f}".format(low_toxic_comments/total_comments)
    high_ratio="{:.2f}".format(high_toxic_comments/total_comments)
    toxic_ratio="{:.2f}".format((low_toxic_comments+high_toxic_comments)/total_comments)
  
    # print("post #",post, " low toxic: ",low_toxic_comments,"| high toxic: ",high_toxic_comments," all: ",total_comments)
    # print("post #",post, " low ratio: ",low_ratio," | high ratio: ",high_ratio," |toxic ratio: ",toxic_ratio," \n")
    trees_df.at[post,'low_ratio']=float(low_ratio)
    trees_df.at[post,'high_ratio']=float(high_ratio)
    trees_df.at[post,'toxic_ratio']=float(toxic_ratio)
    trees_df.at[post,'score_votes']=int(score_votes)
    trees_df.at[post,'upvote_ratio']=float(upvote_ratio)

print(trees_df)
trees_df.to_csv('ukraine_cntr_statistics_new.csv', header=True, index=False)