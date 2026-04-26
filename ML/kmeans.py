from sklearn.cluster import KMeans
import numpy as np
x = np.array([[1,2],[1,3],[3,4],[2,4]])
kmeans = KMeans(n_clusters = 2 , random_state = 0 , n_init = 10)
kmeans.fit(x,y)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
