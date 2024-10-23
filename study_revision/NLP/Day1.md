# Natural Language Processing (NLP) Notebook

# Kindly refer the Natural Language Processing (NLP) Notebook in apple notes which covers the following 

- **Word Embeddings**
- **Matrix Factorization**
- **Language Modelling**
- **Topic Modelling**
- **RNN**




## Word Embeddings

### How Do Word Embeddings Work?
Word embeddings represent words in continuous vector space where similar words have closer representations. 

### Matrix Creation for Word Embeddings
Given a word `i`, we aim to find its vector `v_i` in a `d`-dimensional space. This is typically done using **matrix factorization** techniques.

- **Matrix Factorization**: 
  \[
  A = BC \quad \text{(We decompose the matrix \(A\) into matrices \(B\) and \(C\))}
  \]
  Multiplying \(B\) and \(C\) should give back the original matrix \(A\).

### Problem: How to Obtain the Data Matrix \(A\)?
A simple approach is using the **bag-of-words (BoW)** model, which, however, ignores word sequence information.

### Alternative: Co-occurrence Matrix
One method to incorporate word order is using a **co-occurrence matrix**. Let's consider a sentence:

Example Sentence: "The cat sat on the mat."

|        | The | cat | sat | on  | mat |
|--------|-----|-----|-----|-----|-----|
| The    |  0  |  1  |  0  |  1  |  1  |
| cat    |  1  |  0  |  1  |  0  |  1  |
| sat    |  0  |  1  |  0  |  1  |  0  |
| on     |  1  |  0  |  1  |  0  |  1  |
| mat    |  1  |  1  |  0  |  1  |  0  |

- The co-occurrence matrix tracks word proximity within a certain window size (e.g., window size 5 in this case).

### Word Similarity Using a Siamese Network
Take two words \(w_1\) and \(w_2\) from the co-occurrence matrix and pass them to a **Siamese network** to compute similarity via dot product. 
- The word vectors \(v_i\) and \(v_j\) are then passed through an MLP (Multi-layer Perceptron) to learn the word embeddings.

### Autoencoders for Word Embeddings
Another approach to learn embeddings is **Autoencoders**. 
- Example: Compressing an image for transmission, where the network learns a lower-dimensional representation (bottleneck) and reconstructs the original image at the other end.
- **Bottleneck**: This is where the large matrix is reduced to a smaller one.

---

## Language Modelling

### One-Hot Encoding (OHE)
One simple solution for representing words is **one-hot encoding**, where each word is a vector with one '1' and the rest '0's.

### Naive Bayes for Language Modelling
Naive Bayes is another probabilistic approach, where we model the probability of sequences of words.

---

## Topic Modelling

### Problem
Given `M` documents and `K` topics, the task is to find the probability distribution of topics for each document.

---

## Recurrent Neural Networks (RNNs)

### Multi-Class Classification with RNNs
RNNs are designed to handle sequences by maintaining a **hidden state** that is updated with each new input. 

- Example structure:
  \[
  h_t = f(W_h h_{t-1} + W_x x_t)
  \]
  Where:
  - \(X\): input
  - \(H\): hidden state
  - \(Y\): output
  
### Backpropagation Through Time (BPTT)
The process of updating the weights in RNNs involves **backpropagation through time**, allowing the model to learn from previous time steps.

### Bi-Directional RNNs
Bi-directional RNNs process sequences in both forward and backward directions to capture more context.

---
