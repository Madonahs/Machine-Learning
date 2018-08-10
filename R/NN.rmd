---
title: "Neural Network Matrices"
author: "Syombua"
date: "March 25, 2018"
output:
  html_document: default
  word_document: default
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

## NN

Multiply  $X^TW_1W_2W_3$ 

## Where:

$X^T = \begin{bmatrix} 1\\2\\3 \end{bmatrix}$


$W_1 =\begin{bmatrix} 2 & 0 & 1\\ 0& 1 & 2\\ 3 & 0 & 1\end{bmatrix}$ 


$W_2 =\begin{bmatrix} 1 & 0 & 1\\ 2& 2 & 1\\ 0 & 3 & 0\end{bmatrix}$ 


$W_3 = \begin{bmatrix} 2\\4\\1 \end{bmatrix}$


Solution: Feel Free to ask me a question

```
Always remember to use RC| Row and Columns 
We know X transpose will change from column to row; hence
```
$X^T = \begin{bmatrix} 1&2 &3 \end{bmatrix}$

So:

 $X^TW_1 =\begin{bmatrix} 1&2 &3 \end{bmatrix} *  W_1 =\begin{bmatrix} 2 & 0 & 1\\ 0& 1 & 2\\ 3 & 0 & 1\end{bmatrix}  = \begin{bmatrix} 11&2 & 8\end{bmatrix}$
 
 $X^TW_1W_2 = \begin{bmatrix} 11&2 & 8\end{bmatrix} *  W_2\begin{bmatrix} 1 & 0 & 1\\ 2& 2 & 1\\ 0 & 3 & 0\end{bmatrix} = \begin{bmatrix} 15 &28 & 13\end{bmatrix}$
 
 
$X^TW_1W_2W_3 = \begin{bmatrix} 15 &28 & 13\end{bmatrix} *  W_3 \begin{bmatrix} 2\\4\\1 \end{bmatrix} = \begin{bmatrix} 155 \end{bmatrix}$ 



