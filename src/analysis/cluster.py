"""
This module is used to define functions used in clustering the data.
The following clustering algorithms are used:
    - K-Means
    - K-Medoids
    - Agglomerative Clustering
    - Affinity Propagation
"""

from sklearn.cluster import AffinityPropagation, AgglomerativeClustering, KMeans
from sklearn_extra.cluster import KMedoids


def kmeans_clustering(data, n_clusters=5):
    """
    This function is used to cluster the data using K-Means.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
    return kmeans.labels_

def kmedoids_clustering(data, n_clusters=5):
    """
    This function is used to cluster the data using K-Medoids.
    """
    kmedoids = KMedoids(n_clusters=n_clusters, random_state=0).fit(data)
    return kmedoids.labels_

def agglomerative_clustering(data, n_clusters=5):
    """
    This function is used to cluster the data using Agglomerative Clustering.
    """
    agg = AgglomerativeClustering(n_clusters=n_clusters).fit(data)
    return agg.labels_

def affinity_propagation(data):
    """
    This function is used to cluster the data using Affinity Propagation.
    """
    aff = AffinityPropagation().fit(data)
    return aff.labels_

def get_representative(scores: dict):
    """
    This function is used to find the representative of a cluster using K-Medoids.
    
    Args:
        data: dict
            Data with postID and toxicity scores
    Returns:
        representative: dict
            The representative of the cluster
    """
    # unpack the data
    data = [i for i in scores.values()]
    
    kmedoids = KMedoids(n_clusters=1, random_state=0).fit(data)
    res = kmedoids.cluster_centers_[0]
    
    for key, value in scores.items():
        if (value == res).all():
            return key, value

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_blobs

    X = np.array([
        [1, 2, 10], [1, 4, 5], [1, 0, 3],
        [10, 2, 3], [10, 4, 5], [10, 0, 3],
        [-1, 2, 3], [-1, 4, 5], [-1, 0, 3]
    ])

    '''
    # Generate sample data
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                                random_state=0)

    # Plot the ground truth
    colors = np.array(['#377eb8', '#ff7f00', '#4daf4a',
                       '#f781bf', '#a65628', '#984ea3',
                       '#999999', '#e41a1c', '#dede00'])
    plt.scatter(X[:, 0], X[:, 1], color=colors[labels_true].tolist(), s=10)
    '''

    plt.show()
    #print("K-means, ", kmeans_clustering(X))
    #print("K-Medoids, ", kmedoids_clustering(X))
    #print("Agglomerative, ", agglomerative_clustering(X))
    #print("Affinity Propagation, ", affinity_propagation(X))

    # Find the representative of a cluster
    print("Representative, ", get_representative(X))