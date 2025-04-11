import torch

import torch.nn as nn

# Define a dummy RNN model
class DummyRNN(nn.Module):
	def __init__(self, input_size, hidden_size, output_size, num_layers=1):
		super(DummyRNN, self).__init__()
		self.hidden_size = hidden_size
		self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
		self.fc = nn.Linear(hidden_size, output_size)

	def forward(self, x):
		# x shape: (batch_size, seq_length, input_size)
		h0 = torch.zeros(self.rnn.num_layers, x.size(0), self.hidden_size)
		out, _ = self.rnn(x, h0)
		# Get the output of the last time step
		out = self.fc(out[:, -1, :])
		return out

# Function to generate dummy data
def generate_dummy_data(batch_size, seq_length, input_size):
	X = torch.randn(batch_size, seq_length, input_size)
	y = torch.randn(batch_size, 1)  # Dummy regression targets
	return X, y

if __name__ == "__main__":
	# Hyperparameters
	input_size = 10     # Size of input features
	hidden_size = 20    # Number of features in hidden state
	output_size = 1     # Size of the output
	seq_length = 5      # Sequence length
	num_layers = 1      # Number of RNN layers
	num_epochs = 5      # Number of epochs
	batch_size = 8      # Batch size
	learning_rate = 0.001

	# Initialize model, loss function and optimizer
	model = DummyRNN(input_size, hidden_size, output_size, num_layers)
	criterion = nn.MSELoss()
	optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

	# Dummy training loop
	for epoch in range(num_epochs):
		X, y = generate_dummy_data(batch_size, seq_length, input_size)
		
		outputs = model(X)
		loss = criterion(outputs, y)
		
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()
		
		print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")