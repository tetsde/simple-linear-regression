# 🚀 Hướng Dẫn Push Project Lên GitHub

## Bước 1: Khởi tạo Git Repository (nếu chưa có)

```bash
# Di chuyển vào thư mục project
cd "/Users/tt/Excersie/Simple Linear "

# Khởi tạo git (nếu chưa có)
git init

# Kiểm tra status
git status
```

## Bước 2: Add và Commit Files

```bash
# Thêm tất cả files vào staging
git add .

# Hoặc add từng file cụ thể
git add cli.py
git add Main.py
git add README.md
git add requirements.txt
git add .gitignore
git add LICENSE
git add Salary_dataset.csv

# Commit
git commit -m "Initial commit: Simple Linear Regression CLI"
```

## Bước 3: Tạo Repository Trên GitHub

1. Đi tới https://github.com
2. Click nút **"New"** hoặc **"+"** ở góc trên bên phải
3. Chọn **"New repository"**
4. Điền thông tin:
   - **Repository name**: `simple-linear-regression` (hoặc tên bạn muốn)
   - **Description**: "Simple Linear Regression CLI for Salary Prediction"
   - **Public** hoặc **Private**: Chọn theo ý bạn
   - ❌ **KHÔNG** tick "Initialize this repository with a README" (vì chúng ta đã có)
5. Click **"Create repository"**

## Bước 4: Link Local Repository Với GitHub

Sau khi tạo repo trên GitHub, bạn sẽ thấy hướng dẫn. Chạy các lệnh sau:

```bash
# Thêm remote origin (thay YOUR_USERNAME và REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/simple-linear-regression.git

# Đổi tên branch thành main (nếu cần)
git branch -M main

# Push code lên GitHub
git push -u origin main
```

### Ví dụ cụ thể:

Nếu username GitHub của bạn là `johndoe`:

```bash
git remote add origin https://github.com/johndoe/simple-linear-regression.git
git branch -M main
git push -u origin main
```

## Bước 5: Nhập Username & Password

Khi push lần đầu, GitHub sẽ yêu cầu xác thực:

- **Username**: Username GitHub của bạn
- **Password**: ⚠️ **KHÔNG phải password**, hãy dùng **Personal Access Token**

### Tạo Personal Access Token:

1. Đi tới GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Điền thông tin:
   - **Note**: "Git CLI Access"
   - **Expiration**: Chọn thời gian hết hạn
   - **Scopes**: Tick ✅ **repo** (full control)
4. Click **"Generate token"**
5. **Copy token** (chỉ hiện 1 lần, hãy lưu lại!)
6. Dùng token này làm password khi push

## Bước 6: Verify

Sau khi push thành công, kiểm tra:

```bash
# Xem remote
git remote -v

# Xem status
git status
```

Mở trình duyệt và truy cập:
```
https://github.com/YOUR_USERNAME/simple-linear-regression
```

Bạn sẽ thấy tất cả files đã được push lên! 🎉

## 📝 Các Lệnh Git Hữu Ích Khác

### Cập nhật code sau khi sửa:

```bash
# Check files đã thay đổi
git status

# Add files đã sửa
git add .

# Commit với message
git commit -m "Update: Improved CLI interface"

# Push lên GitHub
git push
```

### Clone repository về máy khác:

```bash
git clone https://github.com/YOUR_USERNAME/simple-linear-regression.git
```

### Pull code mới nhất:

```bash
git pull origin main
```

## ⚠️ Lưu Ý Quan Trọng

1. **Đừng commit files không cần thiết**: `.gitignore` đã được cấu hình để bỏ qua:
   - `__pycache__`
   - `.DS_Store`
   - Virtual environments
   - Output images (*.png)

2. **Nhớ cập nhật README.md**:
   - Thay `[Your Name]` thành tên của bạn
   - Thay `[@yourusername]` thành username GitHub
   - Thay email

3. **Dataset**: Nếu file CSV quá lớn hoặc chứa dữ liệu nhạy cảm, có thể thêm `*.csv` vào `.gitignore`

## 🎯 Checklist Trước Khi Push

- [ ] Đã test CLI (`python cli.py --help`)
- [ ] Đã update README với thông tin cá nhân
- [ ] Đã update LICENSE với tên của bạn
- [ ] Đã kiểm tra `.gitignore`
- [ ] Code chạy không lỗi
- [ ] Đã tạo repository trên GitHub
- [ ] Đã có Personal Access Token

## 🆘 Troubleshooting

### Lỗi: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

### Lỗi: "Authentication failed"
- Đảm bảo dùng **Personal Access Token** chứ không phải password
- Token phải có quyền **repo**

### Lỗi: "Updates were rejected"
```bash
git pull origin main --rebase
git push origin main
```

---

✅ **Chúc bạn push code thành công!** 🚀

Nếu cần hỗ trợ, hãy tham khảo [GitHub Docs](https://docs.github.com/en/get-started).
