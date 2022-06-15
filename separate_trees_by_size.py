import pandas as pd



politics_top=pd.read_csv('politics_top_statistics_new.csv')
print(politics_top)

sports_cntr=pd.read_csv('sports_cntr_statistics_new.csv')
print(sports_cntr)

ukraine_hot=pd.read_csv('ukraine_hot_statistics_new.csv')
print(ukraine_hot)

ukraine_cntr=pd.read_csv('ukraine_cntr_statistics_new.csv')
print(ukraine_cntr)



small_df = pd.DataFrame(columns=ukraine_cntr.columns)
medium_df = pd.DataFrame(columns=ukraine_cntr.columns)
large_df = pd.DataFrame(columns=ukraine_cntr.columns)


for post, post_row in ukraine_cntr.iterrows():
    if post_row['num of comments']<100:
        small_df = small_df.append(post_row, ignore_index=True)
    if post_row['num of comments']>100 and post_row['num of comments']<200:
        medium_df = medium_df.append(post_row, ignore_index=True)
    if post_row['num of comments']>200:
        large_df = large_df.append(post_row, ignore_index=True)

for post, post_row in ukraine_hot.iterrows():
    if post_row['num of comments']<100:
        small_df = small_df.append(post_row, ignore_index=True)
    if post_row['num of comments']>100 and post_row['num of comments']<200:
        medium_df = medium_df.append(post_row, ignore_index=True)
    if post_row['num of comments']>200:
        large_df = large_df.append(post_row, ignore_index=True)

for post, post_row in sports_cntr.iterrows():
    if post_row['num of comments']<100:
        small_df = small_df.append(post_row, ignore_index=True)
    if post_row['num of comments']>100 and post_row['num of comments']<200:
        medium_df = medium_df.append(post_row, ignore_index=True)
    if post_row['num of comments']>200:
        large_df = large_df.append(post_row, ignore_index=True)

for post, post_row in politics_top.iterrows():
    if post_row['num of comments']<100:
        small_df = small_df.append(post_row, ignore_index=True)
    if post_row['num of comments']>100 and post_row['num of comments']<200:
        medium_df = medium_df.append(post_row, ignore_index=True)
    if post_row['num of comments']>200:
        large_df = large_df.append(post_row, ignore_index=True)



print(small_df)
print(medium_df)
print(large_df)

small_df.to_csv('small_ds.csv', header=True, index=False)
medium_df.to_csv('medium_ds.csv', header=True, index=False)
large_df.to_csv('large_ds.csv', header=True, index=False)
