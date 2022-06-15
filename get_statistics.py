import pandas as pd



politics_top=pd.read_csv('politics_top_statistics_new.csv')
# print(politics_top)

sports_cntr=pd.read_csv('sports_cntr_statistics_new.csv')
# print(sports_cntr)

ukraine_cntr=pd.read_csv('ukraine_cntr_statistics_new.csv')
# print(ukraine_cntr)

ukraine_hot=pd.read_csv('ukraine_hot_statistics_new.csv')
# print(ukraine_hot)





print("\nSTATISTICS: /sports (controversial)\n")
avg_root_toxicity=sports_cntr['root_toxicity'].mean()
avg_num_comments=sports_cntr['num of comments'].mean()
avg_avg_toxicity=sports_cntr['avg toxicity of tree'].mean()
avg_levels=sports_cntr['levels of tree'].mean()
avg_toxic_ratio=sports_cntr['toxic_ratio'].mean()
avg_score_votes=sports_cntr['score_votes'].mean()
avg_upvotes_ratio=sports_cntr['upvote_ratio'].mean()
print("avg_root_toxicity: ",avg_root_toxicity," | avg_num_comments: ",avg_num_comments," | avg_avg_toxicity: ",avg_avg_toxicity," | avg_levels: ",avg_levels," | avg_toxic_ratio: ",avg_toxic_ratio," | avg_score_votes: ",avg_score_votes," | avg_upvotes_ratio: ",avg_upvotes_ratio)

print("\nSTATISTICS: /ukraine (controversial)\n")
avg_root_toxicity=ukraine_cntr['root_toxicity'].mean()
avg_num_comments=ukraine_cntr['num of comments'].mean()
avg_avg_toxicity=ukraine_cntr['avg toxicity of tree'].mean()
avg_levels=ukraine_cntr['levels of tree'].mean()
avg_toxic_ratio=ukraine_cntr['toxic_ratio'].mean()
avg_score_votes=ukraine_cntr['score_votes'].mean()
avg_upvotes_ratio=ukraine_cntr['upvote_ratio'].mean()
print("avg_root_toxicity: ",avg_root_toxicity," | avg_num_comments: ",avg_num_comments," | avg_avg_toxicity: ",avg_avg_toxicity," | avg_levels: ",avg_levels," | avg_toxic_ratio: ",avg_toxic_ratio," | avg_score_votes: ",avg_score_votes," | avg_upvotes_ratio: ",avg_upvotes_ratio)

print("\nSTATISTICS: /politics (top)\n")
avg_root_toxicity=politics_top['root_toxicity'].mean()
avg_num_comments=politics_top['num of comments'].mean()
avg_avg_toxicity=politics_top['avg toxicity of tree'].mean()
avg_levels=politics_top['levels of tree'].mean()
avg_toxic_ratio=politics_top['toxic_ratio'].mean()
avg_score_votes=politics_top['score_votes'].mean()
avg_upvotes_ratio=politics_top['upvote_ratio'].mean()
print("avg_root_toxicity: ",avg_root_toxicity," | avg_num_comments: ",avg_num_comments," | avg_avg_toxicity: ",avg_avg_toxicity," | avg_levels: ",avg_levels," | avg_toxic_ratio: ",avg_toxic_ratio," | avg_score_votes: ",avg_score_votes," | avg_upvotes_ratio: ",avg_upvotes_ratio)

print("\nSTATISTICS: /ukraine (hot)\n")
avg_root_toxicity=ukraine_hot['root_toxicity'].mean()
avg_num_comments=ukraine_hot['num of comments'].mean()
avg_avg_toxicity=ukraine_hot['avg toxicity of tree'].mean()
avg_levels=ukraine_hot['levels of tree'].mean()
avg_toxic_ratio=ukraine_hot['toxic_ratio'].mean()
avg_score_votes=ukraine_hot['score_votes'].mean()
avg_upvotes_ratio=ukraine_hot['upvote_ratio'].mean()
print("avg_root_toxicity: ",avg_root_toxicity," | avg_num_comments: ",avg_num_comments," | avg_avg_toxicity: ",avg_avg_toxicity," | avg_levels: ",avg_levels," | avg_toxic_ratio: ",avg_toxic_ratio," | avg_score_votes: ",avg_score_votes," | avg_upvotes_ratio: ",avg_upvotes_ratio)








# small_df.to_csv('small_ds.csv', header=True, index=False)
# medium_df.to_csv('medium_ds.csv', header=True, index=False)
# large_df.to_csv('large_ds.csv', header=True, index=False)
