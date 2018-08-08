import networkx as nx
# from networkx import *
import pandas as pd
# from python-louvain import community
# from networkx.algorithms.community.centrality import girvan_newman
# from networkx.algorithms.centrality import eigenvector_centrality_numpy
import nxviz as nv
pd.set_option('display.max_columns', 500)
import matplotlib.pyplot as plt
df = pd.read_csv('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Data/BuzzFeed/BuzzFeedUserUser.txt',sep='\t', names=['user_no', 'follows'])
df_t = pd.read_csv('C:/Users/Daroo/Documents/GitHub/FakeNewsNet/Python/fake_news_man.csv',sep=',')
df_t = df_t[['user_no', 'user_fake_spread_probability']]
'''
#Data preprocessing for gephi
df_weight = pd.merge(df, df_t, on='user_no', how='left')
df_weight.to_csv("weight.csv", index=False)
'''
# df_users = df.groupby('follows').count().reset_index()
# df_users['follows'].to_csv("nodes.csv", index=False)
# df.to_csv("edges.csv", index=False)
df_weight = pd.merge(df, df_t, right_on='user_no', left_on='follows', how='left')
dt['user_fake_spread_probability''user_fake_spread_probability'] =

print(df_weight)

# G = nx.Graph()
# di = nx.convert_matrix.from_pandas_edgelist(df_weight.head(1000),source='user_no', target='follows', edge_attr='user_fake_spread_probability')
# di = nx.DiGraph(G)
'''
#vis
# ap = nv.ArcPlot(di)
# ap.draw()
# plt.show()



elarge=[(u,v) for (u,v,d) in di.edges(data=True) if d['user_fake_spread_probability'] >0.7]
esmall=[(u,v) for (u,v,d) in di.edges(data=True) if d['user_fake_spread_probability'] <=0.5]
pos=nx.spring_layout(di)
# nodes
nx.draw_networkx_nodes(di,pos,node_size=700)

# edges
nx.draw_networkx_edges(di,pos,edgelist=elarge,
                    width=6)
nx.draw_networkx_edges(di,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')


nx.draw_networkx_labels(di,pos,font_size=20,font_family='sans-serif')

# nx.draw_networkx(di, node_color = 'green', node_size=700)
plt.show()

#get degree and cluster coficient
for v in nodes(di):
    print('%s, %d, %f  '%(v, degree(di, v), clustering(di, v)))
# network info
print(nx.info(di))

#alghorithms
print(G.number_of_edges(48))
print(nx.algorithms.degree_centrality(di))
'''
import community



# nx.transitivity(di)
# 
# # Find modularity
# part = community.best_partition(di)
# mod = community.modularity(part,di)
# 
# # Plot, color nodes using community structure
# values = [part.get(node) for node in di.nodes()]
# nx.draw_spring(di, cmap=plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
# plt.show()

'''
in_centrality = nx.in_degree_centrality(di)
srt_in = sorted(in_centrality.items(), key=lambda x: x[1], reverse=True)

out_centrality = nx.out_degree_centrality(di)
srt_out = sorted(out_centrality.items(), key=lambda x: x[1], reverse=True)
print("--------------------------in_degre")
print("------------hi_degre")
print(srt_in[-5:])
print("------------low_degre")
print(srt_in[:5])
print("--------------------------out_degre")
print("------------hi_degre")
print(srt_out[-5:])
print("------------low_degre")
print(srt_out[:5])

centrality = eigenvector_centrality_numpy(di)
srt_out = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
print(srt_out[-5:])
print(srt_out[-5:])

'''