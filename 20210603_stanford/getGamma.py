import numpy as np
from sklearn.linear_model import LinearRegression
import collections
import matplotlib.pyplot as plt
import math

class getGamma:
    def __init__(self, combined):
        lr = LinearRegression()
        node_name = []
        node_degree = []
        for com in combined:
            node_name.append(com[0])
            node_name.append(com[1])
        node_name = sorted(list(set(node_name)))
        #node_name
        
        node_degree = [0 for i in range(len(node_name))]
        for com in combined:
            node_degree[node_name.index(com[0])] += 1
            node_degree[node_name.index(com[1])] += 1
        node_degree
        
        avgnode_degree = np.mean(node_degree)
        N = len(node_name)
        c = collections.Counter(node_degree)
        x = []
        y = []
        yp = []#ポアソン

        for ci in c.items():
            x.append(ci[0])
            y.append(ci[1]/N)
            yp.append(math.e**(-avgnode_degree)*avgnode_degree**ci[0]/math.factorial(ci[0]))
        plt.scatter(x, y, marker='.', label='power law')
        plt.scatter(x, yp, marker='*', label='poisson')
        plt.xlabel('k')
        plt.ylabel('p_k')
        plt.legend()
        plt.xscale('log')
        plt.yscale('log')

        xlog = np.log(x)
        ylog = np.log(y)
        plt.scatter(xlog, ylog, marker='.')

        lr.fit(xlog.reshape(-1, 1),ylog.reshape(-1, 1))# 線形モデルの重みを学習
        print('coefficient = ', lr.coef_[0]) # 説明変数の係数を出力
        print('intercept = ', lr.intercept_) # 切片を出力
        #return [lr.coef_[0], lr.intercept_]