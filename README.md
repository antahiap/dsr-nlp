# dsr-nlp

## Overview

- Regression:
  - Metrics: mean error
  - Loss: RMSE
- Classification
  - Loss: cross entropy categorical sparse/ negative likelihood loss, for binary (sigmoid).

<img src="img\01.png" style="width:400px;"/>


- What happens with only 2 layers NN? NN is learning the function, if it has only two layers, no hidden layer, then it can't learn the function (XOR example).

- More layers vs more nodes, more layers perform better, no mathematical proof so far just observation.
- NN, is a directed, weighted a-cyclic graph.

## Solve overfit
- add more data
- fewer layers
- regularization
- Drop out 


<img src="img\02.png" style="width:400px;"/>