# Machine Learning Interview Preparation


# Table of Contents
1. [Introduction to Machine Learning](#introduction-to-machine-learning)
2. [ML Classic Concepts](#ml-classic-concepts)
   1. [Supervised Learning](#supervised-learning)
   2. [Unsupervised Learning](#unsupervised-learning)
   3. [Reinforcement Learning](#reinforcement-learning)
3. [Common Machine Learning Algorithms](#common-machine-learning-algorithms)
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

## Introduction to Machine Learning

Machine learning is a field of artificial intelligence that focuses on the development of algorithms that enable computers to learn patterns and make predictions from data.

<p align="left">
<img width="300" src="../img/ml_cover.jpeg">
</p>

## ML Classic Concepts

### Supervised Learning


:white_check_mark: Supervised learning involves training a model on a labeled dataset, where each input is paired with the corresponding correct output. 
Commonly used for classification and regression tasks.

### Unsupervised Learning

:white_check_mark: Unsupervised learning deals with unlabeled data, aiming to find patterns or structures within it. 
Common techniques include clustering and dimensionality reduction.

### Reinforcement Learning
:white_check_mark: Reinforcement learning involves an agent learning to make decisions by interacting with an environment. 
It receives feedback in the form of rewards or penalties.

### Parametric vs Nonparametric

:white_check_mark: **Parametric**: Assumptions can greatly simplify the learning process, but can also limit what can be learned. 
A learning model that summarizes data with a set of parameters of fixed size (independent of the number of 
training examples) is called a parametric model. **examples Parametric**: Logistic Regression, Perceptron
**Benefits of Parametric** Machine Learning Algorithms:
<ins>Simpler:</ins> These methods are easier to understand and interpret results.
<ins>Speed:</ins> Parametric models are very fast to learn from data.
<ins>Less Data:</ins> They do not require as much training data and can work well even if the fit to the data is not perfect.
**Limitations of Parametric** Machine Learning Algorithms:
<ins>Constrained:</ins> By choosing a functional form these methods are highly constrained to the specified form.
<ins>Limited Complexity:</ins> The methods are more suited to simpler problems.
<ins>Poor Fit:</ins> In practice the methods are unlikely to match the underlying mapping function.

:white_check_mark: **Nonparametric**: Algorithms that do not make strong assumptions about the form of the mapping 
function are called nonparametric machine learning algorithms. 
By not making assumptions, they are free to learn any functional form from the training data.
**examples Nonparametric**: k-Nearest Neighbors
**Benefits of Nonparametric** Machine Learning Algorithms:
<ins>Flexibility:</ins> Capable of fitting a large number of functional forms.
<ins>Power:</ins> No assumptions (or weak assumptions) about the underlying function.
<ins>Performance:</ins> Can result in higher performance models for prediction.
**Limitations of Nonparametric** Machine Learning Algorithms:
<ins>More data:</ins> Require a lot more training data to estimate the mapping function.
<ins>Slower:</ins> A lot slower to train as they often have far more parameters to train.
<ins>Overfitting:</ins> More of a risk to overfit the training data and it is harder to explain why specific predictions are made.


## Common Machine Learning Algorithms

###  Linear Regression 

:books: **Description:** Linear regression models the relationship between a dependent variable (output) and one or more independent variables (input) by fitting a linear equation (_y=mx+b_) to the observed data.

:diamond_shape_with_a_dot_inside: **How:** The solution is found by minimizing the sum of squared residuals (SSR) using methods like ordinary least squares.

:white_check_mark: **When to Use:** Suitable for predicting a continuous outcome.

:x: **When Not to Use:** In cases where the relationship between variables is nonlinear, noise data, outliers. It prones to overfitting. Sometimes need extra time for pre-processing or feature engineering. 

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* Simple, interpretable, handles linear data very well.
- :red_circle: *Cons:* Assumes a linear relationship.

:writing_hand: **Example:** Predicting house prices based on square footage.

:link: **Connected Argument:** Feature engineering to capture non-linear relationships.


### Logistic Regression

:books: **Description:** Logistic regression is used for binary classification problems, predicting the probability that an instance belongs to a particular class.

:diamond_shape_with_a_dot_inside: **How:** It uses a logistic function (sigmoid) to map input values, providing probabilities between 0 and 1. The logistic loss or binary cross-entropy are used. Model estimates coefficients via **maximum likelihood estimation** or **gradient descent**.

:white_check_mark: **When to Use:** Binary classification problems.

:x: **When Not to Use:** Multiclass classification tasks.

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* Simple, efficient for binary outcomes.
- :red_circle: *Cons:* Assumes a linear relationship.

:writing_hand: **Example:** Predicting whether an email is spam or not.

:link: **Connected Argument:** Regularization techniques for preventing overfitting.


### K-means Clustering

:books: **Description:** K-Means is a widely-used **unsupervised machine learning** to group data into _k_ clusters based on similarity.

:diamond_shape_with_a_dot_inside: **How:** It iteratively assigns data points to the nearest cluster center, updates the center by computing the mean of the assigned points, and repeats until convergence.

:white_check_mark: **When to Use:** Identifying natural groupings in data.

:x: **When Not to Use:** Sensitive to initial cluster centroids.

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* Simple, scalable for large datasets.
- :red_circle: *Cons:* Sensitive to outliers.

:writing_hand: **Example:** Customer segmentation.

:link: **Connected Argument:** Distance metrics: Euclidean, Manhattan, cosine (the choice of distance metric impacts the clusters formed).


### K-nearest Neighbors (KNN)

:books: **Description:** KNN classifies new data points based on the majority class of their _k_ nearest neighbors.

:diamond_shape_with_a_dot_inside: **How:** It classifies a new data point by identifying its _k_ nearest neighbors and selecting the majority class.

:white_check_mark: **When to Use:** Simple and effective for small datasets.

:x: **When Not to Use:** Sensitive to irrelevant features.

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* Simple, easy to understand.
- :red_circle: *Cons:* Computationally expensive for large datasets.

:writing_hand: **Example:** Handwritten digit recognition.

:link: **Connected Argument:** Distance metrics: Euclidean, Manhattan, cosine (the choice of distance metric and the value of _k_ impact classification results).


### Decision Trees

:books: **Description:** Decision trees are hierarchical structures that make decisions based on the values of input features.

:diamond_shape_with_a_dot_inside: **How:** It recursively splits the data based on the features that maximize information gain or Gini impurity.

:white_check_mark: **When to Use:** Versatile for both classification and regression tasks.

:x: **When Not to Use:** Can overfit noisy data.

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* Easy to understand, no need for feature scaling.
- :red_circle: *Cons:* Prone to overfitting.

:writing_hand: **Example:** Predicting whether a customer will buy a product.

:link: **Connected Argument:** Pruning (to control the tree depth and prevent overfitting).

### Random Forest 

:books: **Description:** Random Forest is an ensemble method that builds multiple decision trees and merges their predictions.

:diamond_shape_with_a_dot_inside: **How:** It builds multiple decision trees on different subsets of the data and combines their predictions.

:white_check_mark: **When to Use:** Robust for various tasks, reduces overfitting.

:x: **When Not to Use:** Less interpretable than a single decision tree.

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* High accuracy, handles missing values.
- :red_circle: *Cons:* Can be computationally expensive.

:writing_hand: **Example:** Predicting stock prices.

:link: **Connected Argument:** Tuning the number of trees and feature selection impact performance.


### Linear SVM 

:books: **Description:** SVM finds a hyperplane that best separates classes in a high-dimensional space.


:diamond_shape_with_a_dot_inside: **How:** It finds the hyperplane with the maximum margin by optimizing the weights using the following formula:

<div>
  <p align="left" style="width: 70%;">
  </p>
  <p align="left" style="width: 30%;">
    <img width="110" src="../img/optimization_formula_svm.jpeg" alt="Descrizione della formula del SVM">
  </p>
</div>

<div>
  <p align="left" style="width: 70%;">
    Subject to the constraints:
  </p>
  <p align="left" style="width: 30%;">
    <img width="110" src="../img/svm_formula.jpeg" alt="Descrizione della formula del SVM">
  </p>
</div>

where **w** is the weight vector, **b** is the bias term, and **x_i** is the data point.


:white_check_mark: **When to Use:** Effective for high-dimensional data.

:x: **When Not to Use:** Less suitable for large datasets.

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* Effective in high-dimensional spaces.
- :red_circle: *Cons:* Not suitable for large datasets.

:writing_hand: **Example:** Image classification.

:link: **Connected Argument:** The kernel trick for handling non-linear relationships. Hinge loss (the hinge loss is used for "maximum-margin" classification).


### Principal Component Analysis (PCA)

:books: **Description:** PCA reduces the dimensionality of data by transforming it into a new coordinate system.

:diamond_shape_with_a_dot_inside: **How:** Standardize the data -> Compute the covariance matrix -> calculating **eigenvectors** and **eigenvalues** of the covariance matrix -> Sort eigenvectors in decreasing order based on their eigenvalues -> Select the top K eigenvectors -> Transform the data into the new K-dimensional space using the dot product 

:white_check_mark: **When to Use:** Reducing dimensionality and noise.

:x: **When Not to Use:** Assumes linear relationships.

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* Efficient for high-dimensional data.
- :red_circle: *Cons:* May lose interpretability.

:writing_hand: **Example:** Facial recognition.

:link: **Connected Argument:** 1. The number of components impacts the trade-off between dimensionality reduction and information loss.  Covariance Matrix. Eigenvector: point in the direction of the maximum variance and the corresponding eigenvalues indicates the importance of its corresponding eigenvector



### Gradient Boosting
:books: **Description:** Gradient Boosting builds an ensemble of weak learners and improves upon their predictions.

:diamond_shape_with_a_dot_inside: **How:** It fits a series of weak learners, each correcting the errors of the previous one.


:white_check_mark: **When to Use:** Effective for improving model performance.

:x: **When Not to Use:** Computationally expensive.

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* High accuracy.
- :red_circle: *Cons:* Prone to overfitting.

:writing_hand: **Example:** Predicting click-through rates.

:link: **Connected Argument:** The learning rate and tree depth affect the trade-off between model complexity and accuracy.


### Perceptron

:books: **Description:** A perceptron is a simple binary classification algorithm capable of learning linear decision boundaries.

:diamond_shape_with_a_dot_inside: **How:** The perceptron learns by adjusting the weights based on misclassifications using the perceptron learning rule.

\[ \mathbf{w}_{\text{new}} = \mathbf{w}_{\text{old}} + \eta \cdot (\text{target} - \text{output}) \cdot \mathbf{x} \]

where \(\mathbf{w}\) is the weight vector, \(\eta\) is the learning rate, and \(\mathbf{x}\) is the input vector.

:white_check_mark: **When to Use:** Simple tasks with linearly separable data.

:x: **When Not to Use:** In the case of non-linear separability.

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* Fast convergence for linearly separable data.
- :red_circle: *Cons:* Limited to linear decision boundaries.

:writing_hand: **Example:** Binary classification of flower species based on petal length and width.

:link: **Connected Argument:** The choice of activation function influences the learning capacity.

### Multi-Layer Perceptron (MLP)

:books: **Description:** MLP is a type of artificial neural network with multiple layers, including an input layer, one or more hidden layers, and an output layer.

:diamond_shape_with_a_dot_inside: **How:** MLP learns by adjusting the weights using backpropagation and gradient descent.

:white_check_mark: **When to Use:** Complex tasks requiring non-linear mappings.

:x: **When Not to Use:** Small datasets or tasks with limited complexity.

:pushpin: **Pros and Cons:**
- :green_circle: *Pros:* Suitable for complex tasks, can learn non-linear relationships.
- :red_circle: *Cons:* Prone to overfitting, requires careful tuning.

:writing_hand: **Example:** Handwritten digit recognition.

:link: **Connected Argument:** The choice of activation functions in hidden layers and output layer affects the network's capacity to capture non-linear patterns.


## Evaluation Metrics

### Confusion Matrix

A confusion matrix is a table that describes the performance of a classification model. It shows the number of true positives, true negatives, false positives, and false negatives.

**How to Use:**
- Calculate metrics like accuracy, precision, recall, and F1 score.

:link: **Connected Argument:**
- Threshold tuning for classification models.

### Precision, Recall, F1 Score

These metrics provide more detailed insights into the performance of a classification model.

**Precision:**
Precision = True Positives / (True Positives + False Positives)

**Recall (Sensitivity or True Positive Rate):**
Recall =  True Positives / (True Positives + False Negatives)

**F1 Score (Harmonic Mean of Precision and Recall):**
 F1 Score = 2 * (Precision *  Recall)  / (Precision + Recall) 

**How to Use:**
- Precision: Focus on minimizing false positives.
- Recall: Focus on minimizing false negatives.
- F1 Score: Balance between precision and recall.

:link: **Connected Argument:**
- The choice of threshold in a classification model affects precision and recall.

### ROC Curve

The Receiver Operating Characteristic (ROC) curve is a graphical representation of the trade-off between **true positive rate (sensitivity)** and **false positive rate (1-specificity)** at various thresholds.

**How to Use:**
- Assess the model's ability to discriminate between positive and negative classes.

:link: **Connected Argument:**
- Area Under the ROC Curve (AUC-ROC) is a summary metric for the entire curve.

---
