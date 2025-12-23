#!/usr/bin/env python3
"""
Simple Linear Regression CLI
Dự đoán mức lương dựa trên năm kinh nghiệm
"""

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os


class LinearRegressionModel:
    def __init__(self):
        self.weights = None
        self.mse = None
        
    def load_data(self, filepath):
        """Load và shuffle dataset"""
        try:
            df = pd.read_csv(filepath)
            df = df.sample(frac=1, random_state=42).reset_index(drop=True)
            return df
        except FileNotFoundError:
            print(f"❌ Không tìm thấy file: {filepath}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Lỗi khi đọc file: {e}")
            sys.exit(1)
    
    def split_data(self, df, train_ratio=0.7, dev_ratio=0.15):
        """Chia dữ liệu thành train/dev/test"""
        n = len(df)
        train_end = int(train_ratio * n)
        dev_end = int((train_ratio + dev_ratio) * n)
        
        train_df = df.iloc[:train_end]
        dev_df = df.iloc[train_end:dev_end]
        test_df = df.iloc[dev_end:]
        
        return train_df, dev_df, test_df
    
    def prepare_xy(self, dataframe):
        """Chuẩn bị X và y từ dataframe"""
        X = dataframe[["YearsExperience"]].copy()
        X.insert(0, "bias", 1)
        y = dataframe["Salary"]
        return X, y
    
    def train(self, X_train, y_train):
        """Train model bằng Normal Equation"""
        X_train_np = X_train.values
        y_train_np = y_train.values
        
        # Normal Equation: w = (X^T X)^-1 X^T y
        self.weights = np.linalg.inv(X_train_np.T @ X_train_np) @ X_train_np.T @ y_train_np
        return self.weights
    
    def predict(self, X):
        """Dự đoán với dữ liệu mới"""
        if self.weights is None:
            raise ValueError("Model chưa được train!")
        return X.values @ self.weights
    
    def evaluate(self, X_test, y_test):
        """Đánh giá model với MSE"""
        y_pred = self.predict(X_test)
        error = y_test.values - y_pred
        squared_error = error ** 2
        self.mse = squared_error.mean()
        return self.mse
    
    def plot_results(self, X_test, y_test, save_path="regression.png"):
        """Vẽ biểu đồ kết quả"""
        y_pred = self.predict(X_test)
        
        sorted_idx = X_test["YearsExperience"].argsort()
        X_sorted = X_test["YearsExperience"].values[sorted_idx]
        y_test_sorted = y_test.values[sorted_idx]
        y_pred_sorted = y_pred[sorted_idx]
        
        plt.figure(figsize=(10, 6))
        plt.scatter(X_sorted, y_test_sorted, label="Dữ liệu thực tế", alpha=0.6)
        plt.plot(X_sorted, y_pred_sorted, color='red', linewidth=2, label="Đường hồi quy")
        
        plt.xlabel("Năm kinh nghiệm")
        plt.ylabel("Lương ($)")
        plt.title("Linear Regression: Mối quan hệ giữa Lương và Kinh nghiệm")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✅ Biểu đồ đã được lưu tại: {save_path}")
        plt.close()


def train_command(args):
    """Lệnh train model"""
    print("=" * 50)
    print("🚀 BẮT ĐẦU TRAIN MODEL")
    print("=" * 50)
    
    model = LinearRegressionModel()
    
    # Load data
    print(f"📂 Đang load dữ liệu từ: {args.data}")
    df = model.load_data(args.data)
    print(f"✅ Đã load {len(df)} dòng dữ liệu")
    
    # Split data
    print("📊 Chia dữ liệu...")
    train_df, dev_df, test_df = model.split_data(df)
    print(f"   Train: {len(train_df)} | Dev: {len(dev_df)} | Test: {len(test_df)}")
    
    # Prepare data
    X_train, y_train = model.prepare_xy(train_df)
    X_test, y_test = model.prepare_xy(test_df)
    
    # Train
    print("🎯 Đang train model...")
    weights = model.train(X_train, y_train)
    print(f"✅ Trọng số (w): {weights}")
    
    # Evaluate
    print("📈 Đánh giá model...")
    mse = model.evaluate(X_test, y_test)
    print(f"✅ MSE Score: {mse:,.2f}")
    
    # Plot if requested
    if args.plot:
        print("📊 Đang tạo biểu đồ...")
        model.plot_results(X_test, y_test, args.output)
    
    print("=" * 50)
    print("✅ HOÀN THÀNH!")
    print("=" * 50)


def predict_command(args):
    """Lệnh dự đoán lương"""
    print("=" * 50)
    print("🔮 DỰ ĐOÁN LƯƠNG")
    print("=" * 50)
    
    # Train model trước
    model = LinearRegressionModel()
    df = model.load_data(args.data)
    train_df, dev_df, test_df = model.split_data(df)
    X_train, y_train = model.prepare_xy(train_df)
    model.train(X_train, y_train)
    
    # Predict
    years = args.years
    X_new = pd.DataFrame({
        "bias": [1],
        "YearsExperience": [years]
    })
    
    predicted_salary = model.predict(X_new)[0]
    
    print(f"📊 Năm kinh nghiệm: {years}")
    print(f"💰 Lương dự đoán: ${predicted_salary:,.2f}")
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="🎯 Simple Linear Regression CLI - Dự đoán lương theo kinh nghiệm",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  # Train model và hiển thị kết quả
  python cli.py train --data Salary_dataset.csv --plot
  
  # Dự đoán lương cho người có 5 năm kinh nghiệm
  python cli.py predict --years 5 --data Salary_dataset.csv
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Lệnh để thực hiện")
    
    # Train command
    train_parser = subparsers.add_parser("train", help="Train model")
    train_parser.add_argument("--data", default="Salary_dataset.csv", help="Đường dẫn tới file CSV")
    train_parser.add_argument("--plot", action="store_true", help="Vẽ biểu đồ kết quả")
    train_parser.add_argument("--output", default="regression.png", help="Tên file biểu đồ output")
    
    # Predict command
    predict_parser = subparsers.add_parser("predict", help="Dự đoán lương")
    predict_parser.add_argument("--years", type=float, required=True, help="Số năm kinh nghiệm")
    predict_parser.add_argument("--data", default="Salary_dataset.csv", help="Đường dẫn tới file CSV")
    
    args = parser.parse_args()
    
    if args.command == "train":
        train_command(args)
    elif args.command == "predict":
        predict_command(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
