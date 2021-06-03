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
    
    def one_dimensional_grid(self, nodenum):
        # 一次元格子
        self.G = nx.Graph()
        n = nodenum # 頂点の数
        self.G.add_nodes_from([i for i in range(n)])
        for i in range(n-1): # 辺の設定
            self.G.add_edges_from([(i, i+1)])
        #nx.draw(self.G, node_size=400, node_color='red', with_labels=True, font_weight='bold') # グラフ描画
            
        # グラフ情報
        self.nnode = nx.number_of_nodes(self.G)
        self.nedge = nx.number_of_edges(self.G)
        degreeind = 0.0
        for degree in nx.degree(self.G):
            degreeind += degree[1]   
        self.avedegree = degreeind / len(nx.degree(self.G))
        #print(self.avedegree)
        #print(nx.info(self.G)) # 平均次数 : average degree
        
        #plt.bar(len(nx.degree_histogram(self.G)), height = nx.degree_histogram(self.G))#次数ヒストグラム
        
        # 平均最短経路長
        self.avespl = nx.average_shortest_path_length(self.G)
        #print("average shortest path length : ",nx.average_shortest_path_length(self.G)) # average shortest path length
        
        # 直径
        self.diameter = nx.diameter(self.G)
        #print("diameter:" , nx.diameter(self.G))
        
        # クラスタ係数
        self.aveclust = nx.average_clustering(self.G)
        
        #最短経路・経路長
        #print(nx.shortest_path(self.G)[0])
        #print(nx.shortest_path_length(self.G))
        return 0

    def two_dimensional_square_lattice(self, nodenum):
        # 二次元正方格子
        self.G = nx.Graph()
        ngrid = nodenum # 1辺あたりのノード数
        self.G = nx.grid_graph(dim=[ngrid, ngrid])
            
        # グラフ情報
        self.nnode = nx.number_of_nodes(self.G)
        self.nedge = nx.number_of_edges(self.G)
        degreeind = 0.0
        for degree in nx.degree(self.G):
            degreeind += degree[1]   
        self.avedegree = degreeind / len(nx.degree(self.G))
        self.avedegree = sum(d for n, d in self.G.degree()) / self.G.number_of_nodes()
        #print(self.avedegree)
        #print(nx.info(self.G)) # 平均次数 : average degree
        
        #plt.bar(len(nx.degree_histogram(self.G)), height = nx.degree_histogram(self.G))#次数ヒストグラム
        
        # 平均最短経路長
        self.avespl = nx.average_shortest_path_length(self.G)
        #print("average shortest path length : ",nx.average_shortest_path_length(self.G)) # average shortest path length
        
        # 直径
        self.diameter = nx.diameter(self.G)
        #print("diameter:" , nx.diameter(self.G))
        
        # クラスタ係数
        self.aveclust = nx.average_clustering(self.G)
        
        #最短経路・経路長
        #print(nx.shortest_path(self.G)[0])
        #print(nx.shortest_path_length(self.G))
        return 0

    def three_dimensional_square_lattice(self, nodenum):
        # 二次元正方格子
        self.G = nx.Graph()
        ngrid = nodenum # 1辺あたりのノード数
        self.G = nx.grid_graph(dim=[ngrid, ngrid])
            
        # グラフ情報
        self.nnode = nx.number_of_nodes(self.G)
        self.nedge = nx.number_of_edges(self.G)
        degreeind = 0.0
        for degree in nx.degree(self.G):
            degreeind += degree[1]   
        self.avedegree = degreeind / len(nx.degree(self.G))
        #print(self.avedegree)
        #print(nx.info(self.G)) # 平均次数 : average degree
        
        #plt.bar(len(nx.degree_histogram(self.G)), height = nx.degree_histogram(self.G))#次数ヒストグラム
        
        # 平均最短経路長
        self.avespl = nx.average_shortest_path_length(self.G)
        #print("average shortest path length : ",nx.average_shortest_path_length(self.G)) # average shortest path length
        
        # 直径
        self.diameter = nx.diameter(self.G)
        #print("diameter:" , nx.diameter(self.G))
        
        # クラスタ係数
        self.aveclust = nx.average_clustering(self.G)
        
        #最短経路・経路長
        #print(nx.shortest_path(self.G)[0])
        #print(nx.shortest_path_length(self.G))
        return 0
    
    def two_dimensional_triangular_lattice(self, nodenum):
        # 二次元正方格子
        self.G = nx.Graph()
        ngrid = nodenum # 1辺あたりのノード数
        self.G = nx.triangular_lattice_graph(ngrid,ngrid)
            
        # グラフ情報
        self.nnode = nx.number_of_nodes(self.G)
        self.nedge = nx.number_of_edges(self.G)
        degreeind = 0.0
        for degree in nx.degree(self.G):
            degreeind += degree[1]   
        self.avedegree = degreeind / len(nx.degree(self.G))
        #print(self.avedegree)
        #print(nx.info(self.G)) # 平均次数 : average degree
        
        #plt.bar(len(nx.degree_histogram(self.G)), height = nx.degree_histogram(self.G))#次数ヒストグラム
        
        # 平均最短経路長
        self.avespl = nx.average_shortest_path_length(self.G)
        #print("average shortest path length : ",nx.average_shortest_path_length(self.G)) # average shortest path length
        
        # 直径
        self.diameter = nx.diameter(self.G)
        #print("diameter:" , nx.diameter(self.G))
        
        # クラスタ係数
        self.aveclust = nx.average_clustering(self.G)
        
        #最短経路・経路長
        #print(nx.shortest_path(self.G)[0])
        #print(nx.shortest_path_length(self.G))
        return 0