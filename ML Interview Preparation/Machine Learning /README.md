# Machine Learning Interview Preparation


## Table of Contents
0. [Linear Regression](#linear-regression)
1. [Logistic Regression](#logistic-regression)
2. [K-means Clustering](#k-means-clustering)
3. [K-nearest Neighbors](#k-nearest-neighbors)
4. [Decision Trees](#decision-trees)
5. [Linear SVM](#linear-smv)

### Linear Regression 

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

### Logistic Regression

**Purpose**: Logistic regression is a statistical method used for <ins>binary classification</ins>.

**Data Type**: Ideal for binary dependent variables (output) with continuous or categorical independent variables (input).

**Objective**: Establishes the relationship between independent variables and the probability of the dependent variable being 1.

**Model Function**: Uses a logistic function (sigmoid) to map input values, providing probabilities between 0 and 1.

**Cost Function**: In logistic regression, the cost function is commonly expressed as the cross-entropy loss. For binary classification problems, the logistic loss or binary cross-entropy is used. 

**Coefficient Estimation**: Model estimates coefficients via **maximum likelihood estimation** or **gradient descent**.

**Prediction**: After training, predicts new data and classifies based on a user-defined threshold probability.


### K-means Clustering

### K-nearest Neighbors

### Decision Trees

### Linear SVM
