"""
This module is used to define functions used in clustering the data.
The following clustering algorithms are used:
    - K-Means
    - K-Medoids
    - Agglomerative Clustering
    - Affinity Propagation
"""

# TODO: Fix these functions
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