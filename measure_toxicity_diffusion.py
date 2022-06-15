import pandas as pd



statistics_df=pd.read_csv('politics_top_statistics_toxic_nodes.csv')
print(statistics_df)

no_replies_cntr=0
cntr=0
sum_ratio=0
for i, row in statistics_df.iterrows():
    if( row['first_reply_level'] == row['last_toxic_level'] and row['first_reply_level']==-1):
        no_replies_cntr+=1
    else:
        cntr+=1
        
        levels_propagated=row['last_toxic_level']-row['first_reply_level']
        total_levels=row['levels of tree']
        ratio=levels_propagated/total_levels
        # print(levels_propagated,"/",total_levels)
        # print("Ratio: ",ratio)
        ratio=ratio*100
        print("last: ",row['last_toxic_level'],"first: ",row['first_reply_level']," | ",levels_propagated,"/",total_levels, "| Ratio: ",int(ratio),"%")
        sum_ratio+=ratio

if(cntr>0):
    avg_ratio=sum_ratio/cntr
    print("Toxicity diffusion stops on average in ", avg_ratio,"% of the tree depth")

print("Total trees that toxicity did not spread in the rest of the tree: ",no_replies_cntr," (total trees: ",i,").")   

