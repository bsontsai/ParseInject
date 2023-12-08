import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Assuming X and Y are numpy arrays
X = np.arange(1, 11)
Y = 5 * (X**2) # change the formula of Y

print("The runtime data is as follows:")

plt.scatter(X, Y)
plt.title('plot')
plt.xlabel('N')
plt.ylabel('Count')
plt.show()

runtime_limit = input("What's the runtime limit? type from: linear(1), quadratic(2), cubic(3), log(log), exp(exp): ")

if runtime_limit == "quadratic" or runtime_limit == "2":
    Y = np.sqrt(Y)
elif runtime_limit == "cubic" or runtime_limit == "3":
    Y = np.cbrt(Y)
elif runtime_limit == "log":
    base_c = input("What base does the log have? ")
    if base_c == "natural" or base_c == "ln":
        Y = np.exp(Y)
    else:
        base = int(base_c)
        Y = base ** Y
elif runtime_limit == "exp":
    Y = np.log(Y)

# Reshape X for sklearn
X = X.reshape(-1, 1)
# normalize y to be between 0 and 1
Y = Y / max(Y)

# plt.scatter(X, Y)
# plt.title('Fitted Plot')
# plt.xlabel('x')
# plt.ylabel('fx')
# plt.show()

# Perform linear regression
model = LinearRegression().fit(X, Y)

# Get residuals
residuals = Y - model.predict(X)

# Plot residuals
plt.scatter(X, residuals)
plt.title('Residual plot')
plt.xlabel('X')
plt.ylabel('Residuals')
plt.show()



# print("the mid data is " + str(residuals[int(len(residuals) / 2)]))
# print("the start data is " + str(residuals[0]))
diff = residuals[int(len(residuals) / 2)] - residuals[0]
# print("The difference is " + str(diff))

# Analyze residuals
if diff > -0.005:
    print("The data is within the runtime limit you set")
elif diff < 0:
    print("The data is over the runtime limit you set")
else:
    print("The data does not strictly follow the runtime limit")
