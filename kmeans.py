
from statistics import mean
from ponto import Ponto
import matplotlib.pyplot as plt


class Kmeans:

    def __init__(self, len_clusters = 3):
        self.clusters = []
        self.cluster_points = [list() for _ in range(len_clusters)]
        self.df_in_ponto = []
        self.len_clusters = len_clusters
        self.__pre_process = False

    def pre_process_data(self, df):
        # Garantir que so vai ser executado somente uma vez este metodo
        if self.__pre_process:
            return

        # idx 4 referente ao primeiro quartil, idx 5 media, idx 6 terceiro quartil
        # Esta parte foi definida pela professora, mas poderia ser qualquer dataframe
        if self.len_clusters == 3:
            cordenadas_clusters = df.describe()[4:7]
        else:
            # Pegar pontos aleatorios
            pass
        
        # Transforma os clusters em seu respectivo ponto (x,y,z,w) inicial.
        for cordenadas in cordenadas_clusters.iloc:
            self.clusters.append( Ponto( list(cordenadas) ) )
        
        # Transforma todos os dado do df em pontos.
        idx = 0
        for ponto in df.iloc():     
            self.df_in_ponto.append( ( Ponto( list(ponto) ), idx ) )
            idx += 1

        self.__pre_process = True

    def score(self, feature, rotulos):
        self.pre_process_data(feature)
        not_loop = True
        while not_loop:
            self.cluster_points = [list() for _ in range(self.len_clusters)]

            for ponto in self.df_in_ponto:
                menor_distancia = Ponto.distancia(ponto[0],self.clusters[0])
                clust = 0
                for idx, ponto_cluster in enumerate(self.clusters):
                    dist = Ponto.distancia(ponto[0], ponto_cluster)
                    if dist < menor_distancia:
                        menor_distancia = dist
                        clust = idx

                self.cluster_points[clust].append(ponto)

            cluters_antigos = self.clusters
            self.clusters = []
        
            # Calcula os novos clusters, com base na media dos pontos deles

            
            for pontos_cluster in self.cluster_points:
                list_coordenada = [list() for _ in range(len(cluters_antigos[0].coordenadas))]
                # Aqui como são em quatro dimensões, está fixo o valor
                for ponto_cluster in pontos_cluster:
                    for idx, coord in enumerate(ponto_cluster[0].coordenadas):
                        list_coordenada[idx].append(coord)
            
                novo_ponto_cluster = [mean(li) for li in list_coordenada]

                self.clusters.append(Ponto( novo_ponto_cluster ) )
            
            # Caso nao haja alteração das cordenadas dos clusters, encerra.
            aux = 0
            for idx, cluster in enumerate(self.clusters):
                if cluster == cluters_antigos[idx]:
                    aux += 1
            if aux == len(self.clusters):
                not_loop = False

        rotulo = 0
        z = 0
        for todos_ponto in self.cluster_points:
            for ponto, idx in todos_ponto:
                if rotulos[idx] == rotulo: z += 1
            rotulo += 1
        print(f'Acertos: {z}\nTotal: {len(rotulos)}')
        print(f'Precisão: {z/len(rotulos):.2f}')
                
            


        
    
    def plot(self):
        plt.plot([q[0].coordenadas[0] for q in self.cluster_points[0]], [q[0].coordenadas[1] for q in self.cluster_points[0]], 'g*')
        plt.plot([q[0].coordenadas[0] for q in self.cluster_points[1]], [q[0].coordenadas[1] for q in self.cluster_points[1]], 'bx')
        plt.plot([q[0].coordenadas[0] for q in self.cluster_points[2]], [q[0].coordenadas[1] for q in self.cluster_points[2]], 'ro')
        plt.show()
    
    def savefig(self):
        plt.plot([q.coordenadas[0] for q in self.cluster_points[0]], [q.coordenadas[1] for q in self.cluster_points[0]], 'g*')
        plt.plot([q.coordenadas[0] for q in self.cluster_points[1]], [q.coordenadas[1] for q in self.cluster_points[1]], 'bx')
        plt.plot([q.coordenadas[0] for q in self.cluster_points[2]], [q.coordenadas[1] for q in self.cluster_points[2]], 'ro')
        plt.savefig()
            