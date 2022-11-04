from sklearn.datasets import load_iris
from statistics import mean
from ponto import Ponto
import matplotlib.pyplot as plt


class Kmeans:

    def __init__(self):
        self.clusters = []
        self.cluster_points = [[],[],[]]
        self.df_in_ponto = []
        self.__pre_process = False

    def pre_process_data(self):
        # Garantir que so vai ser executado somente uma vez este metodo
        if self.__pre_process:
            return
        # idx 4 referente ao primeiro quartil, idx 5 media, idx 6 terceiro quartil
        database = load_iris(as_frame=True)
        df = database['frame']
        cordenadas_clusters = df.describe()[4:7]

        # Transforma os clusters em seu respectivo ponto (x,y,z,w) inicial.
        for cordenadas in cordenadas_clusters.iloc:
            self.clusters.append(
                Ponto(
                    cordenadas[0],
                    cordenadas[1],
                    cordenadas[2],
                    cordenadas[3],
                ) 
            )
        
        # Transforma todos os dado do df em pontos.
        for ponto in df.iloc():
            self.df_in_ponto.append(
                Ponto(
                    ponto[0],
                    ponto[1],
                    ponto[2],
                    ponto[3],
                )
            )
        self.__pre_process = True

    def start(self):
        self.pre_process_data()
        not_loop = True
        while not_loop:
            self.cluster_points = [[],[],[]]

            for ponto in self.df_in_ponto:
                
                d1 = Ponto.distancia(ponto,self.clusters[0])
                d2 = Ponto.distancia(ponto,self.clusters[1])
                d3 = Ponto.distancia(ponto,self.clusters[2])
                # Verifica qual cluster esta mais perto
                if d1 < d2:
                    if d1 < d3:
                        self.cluster_points[0].append(ponto)
                    else:
                        self.cluster_points[2].append(ponto)
                elif d2 < d3:
                    self.cluster_points[1].append(ponto)
                else:
                    self.cluster_points[2].append(ponto)
            cluters_antigos = self.clusters
            self.clusters = []
        
            # Calcula os novos clusters, com base na media dos pontos deles
            for pontos_cluster in self.cluster_points:
                p_x = mean([ponto.x for ponto in pontos_cluster])
                p_y = mean([ponto.y for ponto in pontos_cluster])
                p_z = mean([ponto.z for ponto in pontos_cluster])
                p_w = mean([ponto.w for ponto in pontos_cluster])

                self.clusters.append(Ponto(p_x, p_y, p_z, p_w))
            
            # Caso nao haja alteração das cordenadas dos clusters, encerra.
            if self.clusters[0] == cluters_antigos[0]:
                if self.clusters[1] == cluters_antigos[1]:
                    if self.clusters[2] == cluters_antigos[2]:
                        not_loop = False
    
    def plot(self):
        plt.plot([q.x for q in self.cluster_points[0]], [q.y for q in self.cluster_points[0]], 'g*')
        plt.plot([q.x for q in self.cluster_points[1]], [q.y for q in self.cluster_points[1]], 'bx')
        plt.plot([q.x for q in self.cluster_points[2]], [q.y for q in self.cluster_points[2]], 'ro')
        plt.show()
    
    def savefig(self):
        plt.plot([q.x for q in self.cluster_points[0]], [q.y for q in self.cluster_points[0]], 'g*')
        plt.plot([q.x for q in self.cluster_points[1]], [q.y for q in self.cluster_points[1]], 'bx')
        plt.plot([q.x for q in self.cluster_points[2]], [q.y for q in self.cluster_points[2]], 'ro')
        plt.savefig()
            
