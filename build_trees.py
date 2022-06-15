import statistics
import pandas as pd
import collections

def levelOrder(root):
        if not root: return []
        q = collections.deque([root])
        res = []
        while q:
            ids = []
           
            size = len(q)
            for i in range(size):
                node = q.popleft()
                ids.append(node)
               
                for child in node.children:
                    q.append(child)
            res.append(ids)

        return res

class TreeNode(object):
    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent
        self.tscore = 0
        self.votes = 0
        self.time = 0 

    def add_child(self, data, score, votes, time):
        new_child = TreeNode(data, parent=self.data)
        new_child.add_score(score)
        new_child.add_votes(votes)
        new_child.add_time(time)
        self.children.append(new_child)
        return new_child

    def add_time(self, time):
        self.time = time

    def add_votes(self, votes):
        self.votes = votes

    def add_score(self, score):
        self.tscore = score

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children

    def __str__(self):
        if self.is_leaf():
            return str(self.data)
        return '{data} [{children}]'.format(data=self.data, children=', '.join(map(str, self.children)))

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level()
        prefix = spaces + '|__' if self.parent else ""

        print(prefix + str(self.data))
        if self.children:
            for child in self.children:
                child.print_tree()



posts_df=pd.read_csv('sports_cntr_posts_praw_toxic.csv')
#print(posts_df)

comments_df=pd.read_csv('sports_cntr_comments_praw_toxic.csv')
#print(comments_df)

tree_list=[]

def add_children(children, tree, children_scores, children_votes, children_times):
    i=0

    for c in children:
        ll= tree.add_child(c, children_scores[i], children_votes[i], children_times[i])

        gc=[]
        new_c_scores = []
        new_votes = []
        new_times = []
        for comment, row in comments_df.iterrows():
            if (c==row['parent_id']):
                gc.append(row['comment_id'])
                new_c_scores.append(row['toxicity'])
                new_votes.append(row['score'])
                new_times.append(row['created_utc'])

        if(len(gc)!=0):
            add_children(gc,ll, new_c_scores, new_votes, new_times)
        i+=1


for post, post_row in posts_df.iterrows():
    print("Creating tree of post #",post," ...")
    children=[]
    children_scores = []
    children_votes = []
    children_times = []
    for comment, row in comments_df.iterrows():

        if (post_row['post_id']==row['parent_id']):
            t= TreeNode(post_row['post_id'])
            t.add_score(post_row['toxicity'])
            children.append(row['comment_id'])
            children_scores.append(row['toxicity'])
            children_votes.append(row['score'])
            children_times.append(row['created_utc'])

    if(len(children)!=0):
        add_children(children,t, children_scores, children_votes, children_times)

    tree_list.append(t)

j=0
toxic_nodes=[]
tree_info=[]
trees_info=[]
sum_toxicity=0
total_nodes_of_tree=0
for tree in tree_list:
    print("========= TREE: ", j,"=========\n")
    
    levels = levelOrder(tree)
    i=0
    sum_score_level=0

    nodes_per_level = 0
    for level in levels:
        
        print("level", i)
       
        n=0
        for node in level:
            sum_toxicity+=node.tscore
            total_nodes_of_tree+=1
            if(n==0 and i==0):
                root_id=node.data
                root_toxicity=node.tscore
                tree_info.append(root_id)
                tree_info.append(root_toxicity)
                #print("root id: ",root_id)
                #print("root toxicity: ",root_toxicity)
            print("id ", node.data," parent id", node.parent,  "  Toxicity score = ", node.tscore, "   Vote score = ", node.votes)
            if node.tscore>0.35:
                toxic_nodes.append(node)   
                #print("id ", node.data," parent id", node.parent,  "  score = ", node.tscore)



            sum_score_level += node.tscore
            nodes_per_level +=1
            n+=1
      
        nodes_per_level=0
        i+=1
        #avg_level_score=sum_score_level/nodes_per_level
        #print("average score of level ",i,": ",avg_level_score,"\n")
    avg_toxicity_of_tree=sum_toxicity/total_nodes_of_tree
    tree_info.append(total_nodes_of_tree)
    tree_info.append(avg_toxicity_of_tree)
    # print("avg_toxicity_of_tree: ",avg_toxicity_of_tree)
    total_levels_of_tree=i
    # print("total_levels_of_tree: ",total_levels_of_tree)
    tree_info.append(total_levels_of_tree)
    trees_info.append(tree_info)
    # print(tree_info)
    tree_info=[]
    

    sum_toxicity=0
    total_nodes_of_tree=0
   
    j+=1
for t in range(len(trees_info)):
    print(trees_info[t])
   # df = df.append(pd.DataFrame([trees_info[t]], columns =['root_id', 'root_toxicity','avg toxicity of tree','levels of tree']), ignore_index=True)
trees_df = pd.DataFrame(trees_info, columns =['root_id', 'root_toxicity','num of comments','avg toxicity of tree','levels of tree'])
print (trees_df)
trees_df.to_csv('sports_cntr_statistics_duplicate.csv', header=True, index=False)


j=0
toxic_tree_info=[]
toxic_trees_info=[]
sum_toxicity=0
total_nodes_of_toxic_tree=0
for root in toxic_nodes:
    print("\n========= TREE with toxic node as ROOT: ", j,"=========\n")
    levels= levelOrder(root)
    time_checked=0
    time_interval=-1
    first_reply_level=-1
    last_toxic_level=-1
    first_reply_time=-1
    time_taken_first_toxic_reply=-1
    time_taken_last_toxic_reply=-1
    last_reply_time=-1
    i=0
    for level in levels:
        print("level\n", i)
        n=0
        for node in level:
            print("time node: ", node.time)
            if(n==0 and i==0):
                print("root")
                toxic_root_id=node.data
                toxic_root_toxicity=node.tscore
                toxic_root_time=node.time
                toxic_root_score=node.votes
                toxic_tree_info.append(toxic_root_id)
                toxic_tree_info.append(toxic_root_toxicity)
                toxic_tree_info.append(toxic_root_score)
                toxic_tree_info.append(toxic_root_time)
            # print("id ", node.data," parent id", node.parent,  "  score = ", node.tscore)
            else:
                
                if(node.tscore>0.3):
                    if(time_checked==0):
                        print("first toxic reply!")
                        print("toxic_root_time: ",toxic_root_time)
                        print("node time: ",node.time)
                        first_reply_time=node.time
                        first_reply_level=i
                        time_taken_first_toxic_reply=toxic_root_time-node.time
                        time_checked=1
                    time_taken_last_toxic_reply=toxic_root_time-node.time
                    last_reply_time=node.time
                    last_toxic_level=i
            sum_toxicity+=node.tscore
            total_nodes_of_toxic_tree+=1
           
            n+=1
        i+=1
    avg_toxicity_of_toxic_tree=sum_toxicity/total_nodes_of_toxic_tree
    toxic_tree_info.append(first_reply_time)
    toxic_tree_info.append(last_reply_time)
    toxic_tree_info.append(total_nodes_of_toxic_tree)
    toxic_tree_info.append(avg_toxicity_of_toxic_tree)
    # print("avg_toxicity_of_toxic_tree: ",avg_toxicity_of_toxic_tree)
    total_levels_of_tree=i
    # print("total_levels_of_tree: ",total_levels_of_tree)
    toxic_tree_info.append(total_levels_of_tree)
    toxic_tree_info.append(time_taken_first_toxic_reply)
    toxic_tree_info.append(time_taken_last_toxic_reply)
    toxic_tree_info.append(first_reply_level)
    toxic_tree_info.append(last_toxic_level)
    toxic_trees_info.append(toxic_tree_info)
    # print(toxic_tree_info)
    toxic_tree_info=[]
    sum_toxicity=0
    total_nodes_of_toxic_tree=0
   
    j+=1

# for t in range(len(toxic_trees_info)):
#     print(toxic_trees_info[t])
#    # df = df.append(pd.DataFrame([toxic_trees_info[t]], columns =['root_id', 'root_toxicity','avg toxicity of tree','levels of tree']), ignore_index=True)
trees_df = pd.DataFrame(toxic_trees_info, columns =['root_id', 'root_toxicity','root_score','toxic_root_time','first_reply_time','last_reply_time','num of comments','avg toxicity of tree','levels of tree','time_taken_first_reply','time_taken_last_reply','first_reply_level','last_toxic_level'])
print (trees_df)
trees_df.to_csv('sports_cntr_statistics_toxic_nodes.csv', header=True, index=False)



        
