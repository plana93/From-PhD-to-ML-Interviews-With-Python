import numpy as np
from matplotlib import pyplot as plt

class k_means:
    def __init__(self, k_cluster = 0, max_iterations=100):
        self.k_cluster = k_cluster
        self.centroids = None
        self.cluster_assignments = None
        self.max_iterations=max_iterations
        self.stable = False

    def fit(self, x_input):

        self.centroids = np.random.randn(self.k_cluster, x_input.shape[1])
        self.cluster_assignments = np.zeros(x_input.shape[0])
        iterations = 0
        while (iterations < self.max_iterations) or self.stable:
            for idx_element in range(len(x_input)):
                dist = np.linalg.norm(x_input[idx_element] - self.centroids, axis = 1)
                self.cluster_assignments[idx_element] = np.argmin(dist)
            import pdb;
            #pdb.set_trace()
            for k in range(self.k_cluster):
                vector_element = self.cluster_assignments == k
                n_elements_for_cluster = np.sum(vector_element, 0)
                vector_element = np.stack((vector_element,vector_element),0)
                mean_elements_for_cluster = np.sum(vector_element.T * x_input, 0) / n_elements_for_cluster
                self.centroids[k] = mean_elements_for_cluster

            # optimized version
            # distances = np.linalg.norm(x_input[:, np.newaxis] - self.centroids, axis=2)
            # self.cluster_assignments = np.argmin(distances, axis=1)
            # self.centroids = np.array([np.mean(x_input[np.where(self.cluster_assignments == j)], axis=0)
            #                           for j in range(self.k_cluster)])


            iterations += 1
            if iterations % 10 == 0 : print(iterations)


    def predict(self, x_input):
        distances = np.linalg.norm(x_input[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)



x1 = np.random.randn(5,2) + 5
x2 = np.random.randn(5,2) - 5
X = np.concatenate([x1,x2], axis=0)

# Initialize the KMeans object with k=3
kmeans = k_means(k_cluster=2)

# Fit the k-means model to the dataset
kmeans.fit(X)

# Get the cluster assignments for the input dataset
cluster_assignments = kmeans.predict(X)

print(cluster_assignments)
print(kmeans.centroids)

# Plot the data points with different colors based on their cluster assignments
colors = ['r', 'b']
for i in range(kmeans.k_cluster):
    plt.scatter(X[np.where(np.array(cluster_assignments) == i)][:,0],
                X[np.where(np.array(cluster_assignments) == i)][:,1],
                color=colors[i])

# Plot the centroids as black circles
plt.scatter(kmeans.centroids[:,0], kmeans.centroids[:,1], color='black', marker='o')

# Show the plot
plt.show()