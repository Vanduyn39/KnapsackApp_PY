import random  # Thư viện để sinh các giá trị ngẫu nhiên
import math  # Thư viện toán học, dùng để tính toán với hàm exp

# Hàm tính giá trị của một giải pháp
def calculate_solution_value(weights, values, solution, max_weight):
    # Tính tổng trọng lượng của các vật phẩm được chọn
    total_weight = sum(weights[i] * solution[i] for i in range(len(solution)))
    # Tính tổng giá trị của các vật phẩm được chọn
    total_value = sum(values[i] * solution[i] for i in range(len(solution)))
    
    # Nếu tổng trọng lượng không vượt quá trọng lượng tối đa, trả về giá trị tổng
    # Nếu vượt quá, trả về 0 vì đây là một giải pháp không hợp lệ
    return total_value if total_weight <= max_weight else 0

# Hàm giải bài toán Knapsack bằng thuật toán Simulated Annealing
def simulated_annealing(weights, values, max_weight, initial_temp=1000, cooling_rate=0.99):
    n = len(weights)  # Số lượng vật phẩm
    # Khởi tạo giải pháp ban đầu với mỗi vật phẩm được chọn ngẫu nhiên (0 hoặc 1)
    current_solution = [random.choice([0, 1]) for _ in range(n)]
    # Giải pháp tốt nhất hiện tại là giải pháp ban đầu
    best_solution = current_solution[:]
    # Tính giá trị của giải pháp tốt nhất hiện tại
    best_value = calculate_solution_value(weights, values, best_solution, max_weight)
    
    # Khởi tạo nhiệt độ ban đầu
    temperature = initial_temp

    # Tiến hành thuật toán cho đến khi nhiệt độ giảm xuống dưới 1
    while temperature > 1:
        # Tạo ra một giải pháp mới bằng cách thay đổi ngẫu nhiên một phần tử trong giải pháp hiện tại
        new_solution = current_solution[:]
        index = random.randint(0, n - 1)  # Chọn một chỉ số ngẫu nhiên
        new_solution[index] = 1 - new_solution[index]  # Đảo trạng thái vật phẩm tại vị trí chỉ số đó (0 <=> 1)

        # Tính giá trị của giải pháp hiện tại
        current_value = calculate_solution_value(weights, values, current_solution, max_weight)
        # Tính giá trị của giải pháp mới
        new_value = calculate_solution_value(weights, values, new_solution, max_weight)

        # Quyết định có chấp nhận giải pháp mới hay không
        if new_value > current_value or random.uniform(0, 1) < math.exp((new_value - current_value) / temperature):
            current_solution = new_solution  # Chấp nhận giải pháp mới nếu có giá trị tốt hơn hoặc nếu thỏa mãn tiêu chí xác suất

        # Cập nhật giải pháp tốt nhất nếu giải pháp mới có giá trị tốt hơn
        if new_value > best_value:
            best_solution = new_solution[:]
            best_value = new_value

        # Giảm nhiệt độ theo tỉ lệ làm nguội (cooling rate)
        temperature *= cooling_rate

    # Trả về giải pháp tốt nhất tìm được và giá trị tổng của nó
    return best_solution, best_value
