import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_dataset.csv")
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

n = len(df)
print(f"Data have {n} rows")

train_end = int(0.7 * n)
dev_end   = int(0.85 * n)

train_df = df.iloc[:train_end]
dev_df   = df.iloc[train_end:dev_end]
test_df  = df.iloc[dev_end:]

print("Train / Dev / Test:", len(train_df), len(dev_df), len(test_df))

def prepare_xy(dataframe):
    X = dataframe[["YearsExperience"]].copy()
    X.insert(0, "bias", 1)
    y = dataframe["Salary"]
    return X, y

X_train, y_train = prepare_xy(train_df)
X_dev,   y_dev   = prepare_xy(dev_df)
X_test,  y_test  = prepare_xy(test_df)


X_train_np = X_train.values
y_train_np = y_train.values

w = np.linalg.inv(X_train_np.T @ X_train_np) @ X_train_np.T @ y_train_np
print("Trọng số w:", w)


y_pred = X_test.values @ w

output_df = pd.DataFrame({
    "X values": X_test["YearsExperience"].values,
    "Y Pred": y_pred.round(2)
})
error = y_test.values - y_pred     
squared_error = error ** 2        
MSE_score = squared_error.mean()   
print(f"MSE SCRORE: {MSE_score}")
print(output_df)
sorted_idx = X_test["YearsExperience"].argsort()

X_sorted = X_test["YearsExperience"].values[sorted_idx]
y_test_sorted = y_test.values[sorted_idx]
y_pred_sorted = y_pred[sorted_idx]


plt.scatter(
    X_sorted,
    y_test_sorted,
    label="Actual data"
)

plt.plot(
    X_sorted,
    y_pred_sorted,
    label="Regression line"
)

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression: Salary vs Experience")
plt.legend()
plt.show()
plt.savefig("regression.png")









