import tkinter as tk  # Thư viện Tkinter dùng để tạo giao diện đồ họa
from ui import KnapsackApp  # Nhập lớp KnapsackApp từ module ui.py

if __name__ == "__main__":  # Kiểm tra xem chương trình có đang được chạy trực tiếp không
    root = tk.Tk()  # Tạo cửa sổ chính (root window) cho ứng dụng
    app = KnapsackApp(root)  # Khởi tạo đối tượng KnapsackApp và truyền cửa sổ chính vào
    root.mainloop()  # Bắt đầu vòng lặp chính của Tkinter để xử lý các sự kiện
