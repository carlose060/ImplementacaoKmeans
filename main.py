from sklearn.datasets import load_iris
from kmeans import Kmeans


if __name__ == '__main__':

    
    database = load_iris(as_frame=True)
    feature = database['data']
    rotulos = database['target']
    
    kmeans = Kmeans()

    kmeans.score(feature, rotulos)
    #kmeans.plot()
    