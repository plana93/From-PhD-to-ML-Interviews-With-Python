# Machine Learning Interview Preparation


## Table of Contents
1. [Introduction to Machine Learning](#1-introduction-to-machine-learning)
2. [ML Classic Concepts](#ml-classic-concepts)
   1. [Supervised Learning](#supervised-learning)
   2. [Unsupervised Learning](#unsupervised-learning)
   3. [Reinforcement Learning](#reinforcement-learning)
3. [Common Machine Learning Algorithms](#3-common-machine-learning-algorithms)
   1. [Linear Regression](#linear-regression)
   2. [Logistic Regression](#logistic-regression)
   3. [K-means Clustering](#k-means-clustering)
   4. [K-nearest Neighbors (KNN)](#k-nearest-neighbors)
   5. [Decision Trees](#decision-trees)
   6. [Random Forest](#random-forest)
   7. [Linear SVM](#linear-smv)
   8. [Principal Component Analysis (PCA)](#principal-component-analysis-pca)
   9. [Gradient Boosting](#gradient-boosting)
4. [Deep Learning](#deep-learning)
5. [Evaluation Metrics](#evaluation-metrics)
   1. [Confusion Matrix](#confusion-matrix)
   2. [Precision, Recall, F1 Score](#precision-recall-f1-score)
   3. [ROC Curve](#roc-curve)

### Introduction to Machine Learning

Machine learning is a field of artificial intelligence that focuses on the development of algorithms that enable computers to learn patterns and make predictions from data.
<p align="left">
<img width="300" src="../img/ml_cover.jpeg">
</p>

### ML Classic Concepts

#### Supervised Learning

Supervised learning involves training a model on a labeled dataset, where each input is paired with the corresponding correct output. 
Commonly used for classification and regression tasks.

#### Unsupervised Learning

Unsupervised learning deals with unlabeled data, aiming to find patterns or structures within it. 
Common techniques include clustering and dimensionality reduction.

#### Reinforcement Learning
Reinforcement learning involves an agent learning to make decisions by interacting with an environment. 
It receives feedback in the form of rewards or penalties.


### Common Machine Learning Algorithms

#### Linear Regression 

**Description:** Linear regression models the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the observed data.

**When to Use:** Suitable for predicting a continuous outcome.

**When Not to Use:** In cases where the relationship between variables is nonlinear.

**Pros and Cons:**
- *Pros:* Simple, interpretable.
- *Cons:* Assumes a linear relationship.

**Example:** Predicting house prices based on square footage.
---


Linear regression is a machine learning algorithm that explores relationships between variables, particularly between the output (dependent variable) and one or more inputs (independent variables). 
The fundamental equation is _y=mx+b_, where _y_ is the output, _x_ is the input, _m_ is the slope of the line, and _b_ is the bias.

The goal is to find a function that maps certain features or variables to others. 
Regression answers questions about how one phenomenon influences another or how different variables are correlated. 
It is also useful for making predictions with new data.

To obtain the best predictive weights, the algorithm minimizes residual errors, which are the differences between predicted and actual responses. 
This is achieved by reducing the sum of squared residuals (SSR) for all observations, known as the method of ordinary least squares.

When to use:
- easy simple to train and implement 
- quick: can be done in one-shot or gradient descent 
- handles linear data very well 

When not to use: 
- not linear relation (complex relation) 
- noise  
- outliers
- prone to overfitting 
- maybe need extra time for pre-processing or feature engineering 

#### Logistic Regression

**Description:** Logistic regression is used for binary classification problems, predicting the probability that an instance belongs to a particular class.

**When to Use:** Binary classification problems.

**When Not to Use:** Multiclass classification tasks.

**Pros and Cons:**
- *Pros:* Simple, efficient for binary outcomes.
- *Cons:* Assumes a linear relationship.

**Example:** Predicting whether an email is spam or not.
---

**Purpose**: Logistic regression is a statistical method used for <ins>binary classification</ins>.
Ideal for binary dependent variables (output) with continuous or categorical independent variables (input).

**Model Function**: Uses a logistic function (sigmoid) to map input values, providing probabilities between 0 and 1.

**Cost Function**: In logistic regression, the cost function is commonly expressed as the cross-entropy loss. For binary classification problems, the logistic loss or binary cross-entropy is used. 

**Coefficient Estimation**: Model estimates coefficients via **maximum likelihood estimation** or **gradient descent**.

**Prediction**: After training, predicts new data and classifies based on a user-defined threshold probability.


#### K-means Clustering

**Description:** K-Means partitions data into k clusters based on similarity.

**When to Use:** Identifying natural groupings in data.

**When Not to Use:** Sensitive to initial cluster centroids.

**Pros and Cons:**
- *Pros:* Simple, scalable for large datasets.
- *Cons:* Sensitive to outliers.

**Example:** Customer segmentation.

---

K-means clustering is a widely-used **unsupervised machine learning** algorithm designed to group data points with similarities into k clusters. 
The objective is to partition a given dataset into a <ins>predetermined number of clusters.</ins>



**Initialization**: Start by randomly placing k cluster centers in the feature space, with each center representing a cluster.
**Assignment**: Associate each data point with the nearest cluster center based on a chosen distance metric. <ins>Euclidean distance</ins> is common, but alternatives like Manhattan distance or cosine similarity are viable.
**Update**: Calculate the new mean for each cluster by averaging the data points within that cluster. These means become the updated cluster centers.
**Iteration**: Repeat the assignment and mean calculation steps until the cluster assignments stabilize or until a specified number of iterations is reached.

The outcome is a set of k clusters, where each cluster comprises data points that exhibit the most similarity according to the chosen distance metric.
K-means finds applications in diverse domains such as image segmentation, market segmentation, and customer profiling.

#### K-nearest Neighbors (KNN)

**Description:** KNN classifies new data points based on the majority class of their k nearest neighbors.

**When to Use:** Simple and effective for small datasets.

**When Not to Use:** Sensitive to irrelevant features.

**Pros and Cons:**
- *Pros:* Simple, easy to understand.
- *Cons:* Computationally expensive for large datasets.

**Example:** Handwritten digit recognition.

#### Decision Trees

**Description:** Decision trees are hierarchical structures that make decisions based on the values of input features.

**When to Use:** Versatile for both classification and regression tasks.

**When Not to Use:** Can overfit noisy data.

**Pros and Cons:**
- *Pros:* Easy to understand, no need for feature scaling.
- *Cons:* Prone to overfitting.

**Example:** Predicting whether a customer will buy a product.

#### Random Forest 

**Description:** Random Forest is an ensemble method that builds multiple decision trees and merges their predictions.

**When to Use:** Robust for various tasks, reduces overfitting.

**When Not to Use:** Less interpretable than a single decision tree.

**Pros and Cons:**
- *Pros:* High accuracy, handles missing values.
- *Cons:* Can be computationally expensive.

**Example:** Predicting stock prices.

#### Linear SVM

**Description:** SVM finds a hyperplane that best separates classes in a high-dimensional space.

**When to Use:** Effective for high-dimensional data.

**When Not to Use:** Less suitable for large datasets.

**Pros and Cons:**
- *Pros:* Effective in high-dimensional spaces.
- *Cons:* Not suitable for large datasets.

**Example:** Image classification.

#### Principal Component Analysis (PCA)

**Description:** PCA reduces the dimensionality of data by transforming it into a new coordinate system.

**When to Use:** Reducing dimensionality and noise.

**When Not to Use:** Assumes linear relationships.

**Pros and Cons:**
- *Pros:* Efficient for high-dimensional data.
- *Cons:* May lose interpretability.

**Example:** Facial recognition.

#### Gradient Boosting
**Description:** Gradient Boosting builds an ensemble of weak learners and improves upon their predictions.

**When to Use:** Effective for improving model performance.

**When Not to Use:** Computationally expensive.

**Pros and Cons:**
- *Pros:* High accuracy.
- *Cons:* Prone to overfitting.

**Example:** Predicting click-through rates.