---
title: "Matrices"
author: "Syombua"
date: "March 25, 2018"
output:
  html_document: default
  word_document: default
  pdf_document: default
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

## Neural Network Matrix

I'm multiplying:

Matrix A * B

$A = \begin{bmatrix} 3 & 0 & 1\\ 1 & 2 & 1\\ 0 & 3 & 0\end{bmatrix}$

$B = \begin{bmatrix} 1 & 3 & 5\\ 2 & 0 & 4\\ 0 & 0 & 2\end{bmatrix}$



So I am using the RC: Row * Col to get the first 3:


$A = \begin{bmatrix} 3 & 0 & 1\end{bmatrix}$ * $\begin{bmatrix} 1 \\ 2 \\ 0\end{bmatrix}$ $= \begin{bmatrix} 3\end{bmatrix}$


Hence:

$\begin{bmatrix} 3 & 0 & 1\\ 1 & 2 & 1\\ 0 & 3 & 0\end{bmatrix}$ * $\begin{bmatrix} 1 & 3 & 5\\ 2 & 0 & 4\\ 0 & 0 & 2\end{bmatrix}$ = $\begin{bmatrix} 3 & 9 & 17\\ 5 & 3 & 15\\ 6 & 0 & 12\end{bmatrix}$




