import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import numpy as np

# hyperparameters
input_size = 784  
num_classes = 10  
learning_rate = 0.01  
num_epochs = 30
batch_size = 64 

def my_train(train_dataset, test_dataset=None):
    W = np.random.randn(num_classes, input_size)
    b = np.random.randn(num_classes)
    
    # Convert W and b to PyTorch tensors with gradients
    W = torch.tensor(W, dtype=torch.float32, requires_grad=True)
    b = torch.tensor(b, dtype=torch.float32, requires_grad=True)

    optimizer = optim.SGD([W, b], lr=learning_rate)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    
    for epoch in range(num_epochs):
        total_loss = 0
        for batch_X, batch_y in train_loader:
            batch_X = batch_X.view(-1, input_size)  # Flatten input images
            batch_y = batch_y.long()  # Ensure batch_y is of long type for cross-entropy

            # Calculate outputs with current W and b
            outputs = torch.matmul(batch_X, W.T) + b  # Linear transformation

            # Compute cross-entropy loss
            loss = nn.functional.cross_entropy(outputs, batch_y)
            optimizer.zero_grad()  # Clear gradients
            loss.backward()  # Backpropagation
            optimizer.step()  # Update W and b

            total_loss += loss.item()

        avg_loss = total_loss / len(train_loader)
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}")

    # Detach W and b to convert to numpy arrays for testing
    W = W.detach().numpy()
    b = b.detach().numpy()
    return W, b

# Testing function
def my_test(W, b, test_dataset):
    W_tensor = torch.tensor(W, dtype=torch.float32)
    b_tensor = torch.tensor(b, dtype=torch.float32)

    test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)
    correct = 0
    total = 0

    with torch.no_grad(): # No new outputs, therefore do not need gradient tracking
        for batch_X, batch_y in test_loader:
            batch_X = batch_X.view(-1, input_size)  # Flatten input images
            outputs = torch.matmul(batch_X, W_tensor.T) + b_tensor
            _, predicted = torch.max(outputs, 1)  # Get predicted class
            total += batch_y.size(0)
            correct += (predicted == batch_y).sum().item()  # Count correct predictions

    accuracy = correct / total
    test_error_rate = 1 - accuracy
    print(f"Test Error Rate: {test_error_rate * 100:.2f}%")
    return test_error_rate

