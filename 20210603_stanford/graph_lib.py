import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class graph_lib:
    def __init__(self):
        self.G = ""
        self.nnode = 0 # ノード数
        self.nedge = 0 # エッジ数
        self.avedegree = 0.0 # 平均次数
        self.avespl = 0.0 # 平均最短経路長
        self.diameter = 0.0 # 直径
        self.aveclust = 0.0 # クラスタリング係数
        return

    def getnnode(self):
        return self.nnode
    
    def getnedge(self):
        return self.nedge
    
    def getavedegree(self):
        return self.avedegree
    
    def getavespl(self):
        return self.avespl
    
    def getdiameter(self):
        return self.diameter

    def getaveclust(self):
        return self.aveclust
    
    def combination_network(self, combination):
        self.G = nx.Graph()
        #print(combination)
        for conbi in combination:
            #print(conbi)
            self.G.add_edges_from([(conbi[0], conbi[1])])
        nx.draw(self.G, node_size=100, node_color='blue', with_labels=True, font_weight='bold') # グラフ描画
        
        # グラフ情報
        self.nnode = nx.number_of_nodes(self.G)
        self.nedge = nx.number_of_edges(self.G)
        degreeind = 0.0
        for degree in nx.degree(self.G):
            degreeind += degree[1]   
        self.avedegree = degreeind / len(nx.degree(self.G))
        #print(self.avedegree)
        #print(nx.info(self.G)) # 平均次数 : average degree
        
        return