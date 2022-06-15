import praw
import pandas as pd 

reddit = praw.Reddit(client_id='8hTHhvTkxnldCeLFgYsbaQ',client_secret='UgxYKUsiefFICk9xKNScOIWoFdMbAw',username='lady_bou',password='gingrapefruitbaby',user_agent='d6')
subreddit= reddit.subreddit('politics')
hot_politics = subreddit.hot(limit=500) #time_filter="all"

submissions_dict={}
comments_list=[]
comments_dict={}
comment_info=[]
posts_list=[]
post_info=[]
import csv


# f = open('praw_data.csv',"w")
    # # for key in dict_post_comments.keys():
    #     f.write("%s, %s\n" % (key, dict_post_comments[key]))


i=0
for submission in hot_politics:
    
    if (submission.num_comments>20 and submission.num_comments<1500): #and submission.num_comments<3000
        i+=1
        print("#"+str(i)+" post id: "+ str(submission.id))
        # f.write("post_id: %s, self_text: %s\n" % (str(submission.id),submission.selftext))
        post_info.append(str(submission.id))
        post_info.append(submission.title)
        post_info.append(submission.score)
        post_info.append(submission.created)
        post_info.append(submission.created_utc)
        post_info.append(submission.num_comments)
        post_info.append(submission.upvote_ratio)
        post_info.append(submission.selftext)
        
        
        posts_list.append(post_info)
        post_info=[]
        submissions_dict[str(submission.id)]=submission.title
        # print("author: ",submission.author)
        print("num of comments: ",submission.num_comments)
        # print("score: ",submission.score)

        # print("have visited: ",submission.visited)
        # print("title: ",submission.title)
        # print("selftext: ", submission.selftext)
        # print("created: ", submission.created)
        # print("created_utc: ", submission.created_utc)
        # print("------------------------------------\n")



        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            # print("---------------------------------------")
            # print("post id: "+ str(submission.id))

            comment_info.append(str(comment.id))


            # print("parent id: ",comment.parent())
            parent_id=str(comment.parent())
            comment_info.append(parent_id)

            # print("comment id: ",comment.id)
            body_comment=[]
            body_comment.append(comment.body)
            # print(">>>>>>>>>>>",body_comment)
            comment_info.append(body_comment)
            comment_info.append(comment.score)
            comment_info.append(submission.created)
            comment_info.append(submission.created_utc)



            comments_dict[str(comment.id)]=comments_list
            comments_list.append(comment_info)
            comment_info=[]

            #f.write("parent_id: %s, comment_id %s, comment_body: %s\n" % (str(comment.parent()), comment.id,comment.body))
            # print(comment.body)
            # if len(comment.replies)>0:
            #     for reply in comment.replies:
            #         print(">>>>>>>> REPLY: ", reply.id)
            #         f.write("reply_id: %s\n" % (reply.id))
            

# for submission, selftext in submissions_dict.items():
#     print("post_id: "+submission+" selftext: "+selftext)

# for comment, v in comments_dict.items():
#     print("comment_id: "+comment)
#     print(v) #parent_id -> v[0] , body -> v[1][0]
#     print("------------\n")

df_comments=pd.DataFrame(comments_list)
print(df_comments)
df_comments.columns = ['comment_id','parent_id','body','score','created','created_utc']
df_comments.to_csv('politics_hot_comments_praw.csv', header=True, index=False)

df_posts=pd.DataFrame(posts_list)
print(df_posts)
df_posts.columns = ['post_id','title','score','created','created_utc','num_comments','upvote_ratio','selftext']
df_posts.to_csv('politics_hot_posts_praw.csv', header=True, index=False)

#see the attributes
# attributes_list=['STR_FIELD', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_chunk', '_comments_by_id', '_fetch', '_fetch_data', '_fetch_info', '_fetched', '_kind', '_reddit', '_reset_attributes', '_safely_add_arguments', '_url_parts', '_vote', 'all_awardings', 'allow_live_comments', 'approved_at_utc', 'approved_by', 'archived', 'author', 'author_flair_background_color', 'author_flair_css_class', 'author_flair_richtext', 'author_flair_template_id', 'author_flair_text', 'author_flair_text_color', 'author_flair_type', 'author_fullname', 'author_is_blocked', 'author_patreon_flair', 'author_premium', 'award', 'awarders', 'banned_at_utc', 'banned_by', 'can_gild', 'can_mod_post', 'category', 'clear_vote', 'clicked', 'comment_limit', 'comment_sort', 'comments', 'content_categories', 'contest_mode', 'created', 'created_utc', 'crosspost', 'delete', 'disable_inbox_replies', 'discussion_type', 'distinguished', 'domain', 'downs', 'downvote', 'duplicates', 'edit', 'edited', 'enable_inbox_replies', 'flair', 'fullname', 'gild', 'gilded', 'gildings', 'hidden', 'hide', 'hide_score', 'id', 'id_from_url', 'is_created_from_ads_ui', 'is_crosspostable', 'is_meta', 'is_original_content', 'is_reddit_media_domain', 'is_robot_indexable', 'is_self', 'is_video', 'likes', 'link_flair_background_color', 'link_flair_css_class', 'link_flair_richtext', 'link_flair_template_id', 'link_flair_text', 'link_flair_text_color', 'link_flair_type', 'locked', 'mark_visited', 'media', 'media_embed', 'media_only', 'mod', 'mod_note', 'mod_reason_by', 'mod_reason_title', 'mod_reports', 'name', 'no_follow', 'num_comments', 'num_crossposts', 'num_reports', 'over_18', 'parent_whitelist_status', 'parse', 'permalink', 'pinned', 'post_hint', 'preview', 'pwls', 'quarantine', 'removal_reason', 'removed_by', 'removed_by_category', 'reply', 'report', 'report_reasons', 'save', 'saved', 'score', 'secure_media', 'secure_media_embed', 'selftext', 'selftext_html', 'send_replies', 'shortlink', 'spoiler', 'stickied', 'subreddit', 'subreddit_id', 'subreddit_name_prefixed', 'subreddit_subscribers', 'subreddit_type', 'suggested_sort', 'thumbnail', 'thumbnail_height', 'thumbnail_width', 'title', 'top_awarded_type', 'total_awards_received', 'treatment_tags', 'unhide', 'unsave', 'ups', 'upvote', 'upvote_ratio', 'url', 'user_reports', 'view_count', 'visited', 'whitelist_status', 'wls']
# for attribute in attributes_list:
#     print(attribute)