import tkinter as tk  # Thư viện để tạo giao diện người dùng (GUI)
from tkinter import messagebox  # Thư viện để hiển thị các hộp thông báo lỗi
from tkinter import ttk  # Thư viện mở rộng của tkinter cho các widget nâng cao (Treeview)
from knapsack_algorithm import simulated_annealing  # Nhập thuật toán Simulated Annealing từ tệp ngoài

class KnapsackApp:
    def __init__(self, root):
        self.root = root  # Cửa sổ chính của ứng dụng
        self.root.title("Knapsack Problem - Simulated Annealing")  # Tiêu đề cửa sổ
        self.items = []  # Danh sách chứa tên, giá trị, và trọng lượng của các vật phẩm

        # Frame để chứa các trường nhập liệu
        input_frame = tk.Frame(self.root)  # Tạo một frame chứa các trường nhập liệu
        input_frame.pack(pady=10)  # Đặt frame vào cửa sổ chính và có khoảng cách giữa các phần tử

        # Nhãn và ô nhập liệu cho tên vật phẩm
        tk.Label(input_frame, text="Tên vật phẩm").grid(row=0, column=0)  # Nhãn cho ô nhập tên
        self.name_entry = tk.Entry(input_frame)  # Ô nhập tên vật phẩm
        self.name_entry.grid(row=0, column=1)  # Đặt ô nhập liệu vào vị trí (0, 1)

        # Nhãn và ô nhập liệu cho giá trị vật phẩm
        tk.Label(input_frame, text="Giá trị").grid(row=1, column=0)  # Nhãn cho ô nhập giá trị
        self.value_entry = tk.Entry(input_frame)  # Ô nhập giá trị vật phẩm
        self.value_entry.grid(row=1, column=1)  # Đặt ô nhập liệu vào vị trí (1, 1)

        # Nhãn và ô nhập liệu cho trọng lượng vật phẩm
        tk.Label(input_frame, text="Trọng lượng").grid(row=2, column=0)  # Nhãn cho ô nhập trọng lượng
        self.weight_entry = tk.Entry(input_frame)  # Ô nhập trọng lượng vật phẩm
        self.weight_entry.grid(row=2, column=1)  # Đặt ô nhập liệu vào vị trí (2, 1)

        # Nút để thêm vật phẩm vào danh sách
        self.add_button = tk.Button(input_frame, text="Thêm vật phẩm", command=self.add_item)
        self.add_button.grid(row=3, columnspan=2, pady=5)  # Đặt nút vào vị trí cuối cùng trong frame

        # Khung dữ liệu (Treeview) để hiển thị các vật phẩm đã nhập
        self.tree = ttk.Treeview(self.root, columns=("Name", "Value", "Weight"), show="headings")
        self.tree.heading("Name", text="Tên")  # Cột tên vật phẩm
        self.tree.heading("Value", text="Giá trị")  # Cột giá trị
        self.tree.heading("Weight", text="Trọng lượng")  # Cột trọng lượng
        self.tree.pack(pady=10)  # Đặt khung Treeview vào cửa sổ chính

        # Nút xóa dữ liệu khỏi danh sách và các ô nhập liệu
        self.clear_button = tk.Button(self.root, text="Xóa Dữ Liệu", command=self.clear_data)
        self.clear_button.pack(pady=5)  # Đặt nút xóa vào cửa sổ chính

        # Nhãn và ô nhập liệu cho trọng lượng tối đa của túi
        tk.Label(self.root, text="Trọng lượng tối đa").pack()
        self.max_weight_entry = tk.Entry(self.root)  # Ô nhập trọng lượng tối đa
        self.max_weight_entry.pack()

        # Nút để chạy thuật toán và hiển thị kết quả
        self.run_button = tk.Button(self.root, text="Chạy thuật toán", command=self.run_algorithm)
        self.run_button.pack(pady=10)

        # Khung văn bản để hiển thị kết quả của thuật toán
        self.result_text = tk.Text(self.root, height=10, width=50, state="disabled")
        self.result_text.pack(pady=10)  # Đặt khung kết quả vào cửa sổ chính

    def add_item(self):
        # Hàm này sẽ thêm vật phẩm vào danh sách và khung Treeview
        name = self.name_entry.get()  # Lấy tên vật phẩm từ ô nhập liệu
        try:
            # Lấy giá trị và trọng lượng từ các ô nhập liệu và chuyển thành số nguyên
            value = int(self.value_entry.get())
            weight = int(self.weight_entry.get())
            self.items.append((name, value, weight))  # Thêm vật phẩm vào danh sách
            # Thêm vật phẩm vào khung Treeview
            self.tree.insert("", "end", values=(name, value, weight))
            # Xóa dữ liệu trong các ô nhập liệu sau khi thêm
            self.name_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)
            self.weight_entry.delete(0, tk.END)
        except ValueError:
            # Nếu người dùng nhập sai kiểu dữ liệu, hiển thị thông báo lỗi
            messagebox.showerror("Lỗi", "Vui lòng nhập giá trị và trọng lượng hợp lệ.")

    def clear_data(self):
        # Hàm này sẽ xóa tất cả các dữ liệu (vật phẩm) trong danh sách và khung Treeview
        self.items.clear()  # Xóa danh sách vật phẩm
        for item in self.tree.get_children():  # Duyệt qua tất cả các vật phẩm trong Treeview
            self.tree.delete(item)  # Xóa từng mục khỏi Treeview
        # Xóa dữ liệu trong tất cả các ô nhập liệu
        self.name_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.max_weight_entry.delete(0, tk.END)
        # Xóa kết quả trong khung Text
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state="disabled")

    def run_algorithm(self):
        # Hàm này chạy thuật toán Simulated Annealing và hiển thị kết quả
        try:
            max_weight = int(self.max_weight_entry.get())  # Lấy trọng lượng tối đa từ ô nhập liệu
            # Lấy tên, giá trị, và trọng lượng từ danh sách vật phẩm
            names, values, weights = zip(*self.items)
            # Chạy thuật toán Simulated Annealing
            selected_items, total_value = simulated_annealing(weights, values, max_weight)
            # Tạo chuỗi kết quả
            result_text = f"Tổng giá trị: {total_value}\nVật phẩm được chọn:\n"
            result_text += "\n".join([names[i] for i in range(len(selected_items)) if selected_items[i] == 1])
            # Hiển thị kết quả trong khung Text
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, tk.END)  # Xóa kết quả cũ
            self.result_text.insert(tk.END, result_text)  # Chèn kết quả mới
            self.result_text.config(state="disabled")
        except ValueError:
            # Nếu nhập trọng lượng tối đa sai, hiển thị thông báo lỗi
            messagebox.showerror("Lỗi", "Vui lòng nhập trọng lượng tối đa hợp lệ.")
        except Exception as e:
            # Bắt các lỗi khác và hiển thị thông báo lỗi
            messagebox.showerror("Lỗi", str(e))
