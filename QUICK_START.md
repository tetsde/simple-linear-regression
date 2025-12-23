# ✅ CÁC BƯỚC ĐỂ PUSH LÊN GITHUB

Project đã được setup xong! Giờ chỉ cần làm theo các bước sau:

## 🚀 Quick Start (3 bước đơn giản)

### 1️⃣ Tạo Repository trên GitHub
- Truy cập: https://github.com/new
- Repository name: `simple-linear-regression`
- Description: "Simple Linear Regression CLI for Salary Prediction"
- Chọn **Public** hoặc **Private**
- ❌ **KHÔNG** tick "Initialize with README"
- Click **"Create repository"**

### 2️⃣ Link với GitHub (thay YOUR_USERNAME)
```bash
cd "/Users/tt/Excersie/Simple Linear "
git remote add origin https://github.com/YOUR_USERNAME/simple-linear-regression.git
git branch -M main
```

### 3️⃣ Push code lên
```bash
git push -u origin main
```

**Lưu ý**: Khi push, dùng **Personal Access Token** thay vì password!

---

## 📋 Chi tiết đã hoàn thành

✅ **Files đã tạo:**
- `cli.py` - CLI tool chính với 2 commands (train & predict)
- `README.md` - Hướng dẫn đầy đủ về project
- `requirements.txt` - Dependencies (pandas, numpy, matplotlib)
- `.gitignore` - Loại bỏ files không cần thiết
- `LICENSE` - MIT License
- `GITHUB_GUIDE.md` - Hướng dẫn chi tiết push lên GitHub
- `QUICK_START.md` - File này (hướng dẫn nhanh)

✅ **Git đã khởi tạo:**
- Git repository đã init
- All files đã được commit
- Sẵn sàng để push

✅ **CLI đã test:**
- ✅ `python3 cli.py --help` - OK
- ✅ `python3 cli.py train --plot` - OK (MSE: 46,129,192.53)
- ✅ `python3 cli.py predict --years 5` - OK (Predicted: $71,666.83)

---

## 🎯 Sử dụng CLI

**Train model và vẽ biểu đồ:**
```bash
python3 cli.py train --data Salary_dataset.csv --plot
```

**Dự đoán lương:**
```bash
python3 cli.py predict --years 5
python3 cli.py predict --years 10
```

---

## 📚 Tài liệu

- **Hướng dẫn sử dụng**: Xem `README.md`
- **Hướng dẫn GitHub chi tiết**: Xem `GITHUB_GUIDE.md`
- **Script demo gốc**: `Main.py` (đã sửa đường dẫn CSV)

---

## 🔑 Tạo Personal Access Token

1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token (classic)
4. Scopes: Tick ✅ **repo**
5. Generate → Copy token
6. Dùng token này khi Git yêu cầu password

---

## ⚠️ TODO trước khi push

- [ ] Update `README.md`: Thay `[Your Name]` và email
- [ ] Update `LICENSE`: Thay `[Your Name]`
- [ ] Tạo repository trên GitHub
- [ ] Tạo Personal Access Token
- [ ] Push code

---

🎉 **Chúc bạn thành công!**

Nếu gặp vấn đề, xem `GITHUB_GUIDE.md` để có hướng dẫn chi tiết hơn.
