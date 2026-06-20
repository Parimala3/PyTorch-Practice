# 🚀 PyTorch Learning - Day 1

Welcome to my **PyTorch Learning Journey**! This repository contains the code and notes I used to learn the fundamentals of PyTorch.

## 📌 What is PyTorch?

PyTorch is an open-source deep learning framework developed by Meta AI. It is widely used for:
- Machine Learning
- Deep Learning
- Computer Vision
- Natural Language Processing (NLP)
- Generative AI

PyTorch provides tensors, automatic differentiation (Autograd), neural network modules, and optimization tools.

---

# 📚 Topics Covered

- Tensor Creation
- Tensor Operations
- Matrix Multiplication
- Tensor Reshaping
- Autograd
- Gradients
- Neural Networks
- Forward Pass
- Loss Functions
- Optimizers
- Training Loop

---

# 1️⃣ Tensor Creation

```python
import torch

scalar = torch.tensor(7)
vector = torch.tensor([1, 2, 3])
matrix = torch.tensor([[1, 2], [3, 4]])
random_tensor = torch.rand(2, 3)

print(scalar)
print(vector)
print(matrix)
print(random_tensor)
```

### Explanation
- `torch.tensor(7)` creates a **scalar** (0D tensor).
- `torch.tensor([1,2,3])` creates a **vector** (1D tensor).
- `torch.tensor([[1,2],[3,4]])` creates a **matrix** (2D tensor).
- `torch.rand(2,3)` creates a **2 × 3 tensor** with random values between 0 and 1.

---

# 2️⃣ Tensor Operations

```python
a = torch.tensor([2, 4, 6])
b = torch.tensor([1, 3, 5])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

### Explanation
PyTorch performs element-wise operations:

- Addition → `[3, 7, 11]`
- Subtraction → `[1, 1, 1]`
- Multiplication → `[2, 12, 30]`
- Division → `[2.0, 1.33, 1.2]`

---

# 3️⃣ Matrix Multiplication

```python
A = torch.tensor([[1, 2],
                  [3, 4]])

B = torch.tensor([[5, 6],
                  [7, 8]])

result = torch.matmul(A, B)
print(result)
```

### Explanation

Matrix multiplication is different from element-wise multiplication.

Result:

```
tensor([[19, 22],
        [43, 50]])
```

It is heavily used in neural networks for computing outputs.

---

# 4️⃣ Tensor Reshaping

```python
x = torch.arange(12)

print(x.reshape(3, 4))
print(x.reshape(2, 6))
print(x.reshape(4, 3))
```

### Explanation

`torch.arange(12)` creates:

```
tensor([0,1,2,3,4,5,6,7,8,9,10,11])
```

`reshape()` changes the dimensions without changing the data.

---

# 5️⃣ Autograd (Automatic Differentiation)

```python
x = torch.tensor(3.0, requires_grad=True)

y = x ** 2

y.backward()

print(x.grad)
```

### Explanation

- `requires_grad=True` tells PyTorch to track operations.
- `y = x²`
- `y.backward()` computes the derivative.

Mathematically:

```
y = x²

dy/dx = 2x
```

At `x = 3`:

```
dy/dx = 6
```

Output:

```
tensor(6.)
```

---

# 6️⃣ Gradient

A **gradient** tells us how much a function changes when its input changes.

For example:

```
y = x²
```

Gradient:

```
dy/dx = 2x
```

At `x = 5`:

```
Gradient = 10
```

The gradient helps determine how model parameters should be updated.

---

# 7️⃣ Gradient Descent

Gradient Descent is an algorithm used to minimize the loss by updating model weights.

Formula:

```
new_weight = old_weight - learning_rate × gradient
```

Example:

```
Old Weight = 5
Gradient = 2
Learning Rate = 0.1

New Weight = 5 - (0.1 × 2)
           = 4.8
```

---

# 8️⃣ Neural Network

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(2, 4),
    nn.ReLU(),
    nn.Linear(4, 1)
)

print(model)
```

### Explanation

This model contains:

- Input layer → 2 features
- Hidden layer → 4 neurons
- ReLU activation
- Output layer → 1 neuron

Architecture:

```
Input
   │
Linear
   │
 ReLU
   │
Linear
   │
Output
```

---

# 9️⃣ Forward Pass

```python
x = torch.randn(5, 2)

output = model(x)

print(output)
```

### Explanation

- `torch.randn(5,2)` creates random input data.
- The data flows through the neural network.
- The network produces predictions.

This process is called the **forward pass**.

---

# 🔟 Loss Function

```python
loss_fn = nn.MSELoss()

pred = torch.tensor([2.0])
actual = torch.tensor([3.0])

loss = loss_fn(pred, actual)

print(loss)
```

### Explanation

Mean Squared Error (MSE):

```
Loss = (Actual - Predicted)²
```

Example:

```
(3 - 2)² = 1
```

Lower loss means better predictions.

---

# 1️⃣1️⃣ Optimizer

```python
import torch.optim as optim

optimizer = optim.SGD(model.parameters(), lr=0.01)
```

### Explanation

The optimizer updates model weights.

- `SGD` → Stochastic Gradient Descent
- `lr=0.01` → Learning rate

Weight update formula:

```
new_weight = old_weight - learning_rate × gradient
```

---

# 1️⃣2️⃣ Training Loop

```python
for epoch in range(5):

    optimizer.zero_grad()

    output = model(x)

    target = torch.randn(5, 1)

    loss = loss_fn(output, target)

    loss.backward()

    optimizer.step()

    print(loss.item())
```

### Step-by-step

### `optimizer.zero_grad()`
Clears old gradients before computing new ones.

### `output = model(x)`
Performs the forward pass.

### `loss = loss_fn(output, target)`
Computes the prediction error.

### `loss.backward()`
Calculates gradients automatically.

### `optimizer.step()`
Updates model weights using gradient descent.

### `print(loss.item())`
Displays the current loss value.

---

# 📖 Summary

| Concept | Description |
|----------|-------------|
| Tensor | Multi-dimensional array used in PyTorch |
| Autograd | Automatically computes gradients |
| Gradient | Derivative showing how parameters affect the loss |
| Gradient Descent | Updates parameters to reduce loss |
| Neural Network | Learns patterns from data |
| Forward Pass | Produces predictions |
| Loss Function | Measures prediction error |
| Optimizer | Updates model parameters |
| Training Loop | Repeats learning until the model improves |

---

# 🎯 Conclusion

This project demonstrates the core concepts of PyTorch, including tensors, automatic differentiation, neural networks, loss computation, optimization, and the training process. These fundamentals provide the foundation for building more advanced deep learning models and applications.
