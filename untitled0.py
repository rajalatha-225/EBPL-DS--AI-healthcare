import matplotlib.pyplot as plt

# Data for the example: accuracy over epochs

epochs = \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accuracy = \[50.00, 54.00, 60.00, 70.00, 75.00, 80.00, 85.00, 88.00, 90.00, 90.00]

# Plotting the accuracy over epochs

plt.figure(figsize=(10, 6))
plt.plot(epochs, accuracy, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)
plt.title('Training Accuracy over Epochs (Medical Image Classification)', fontsize=14)
plt.xlabel('Epochs', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
plt.xticks(epochs)
plt.grid(True)
plt.show()
