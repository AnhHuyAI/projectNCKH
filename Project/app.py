from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

data = {
    "Nhà hàng": {
        "Phục vụ lau dọn nhà hàng": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Chạy bàn tại các nhà hàng": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Nhân viên quán nhậu": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Nhân viên quán bar": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Pha chế": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Phục vụ tiệc cưới tại nhà hàng": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Thu ngân tại quán ăn": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Hỗ trợ bếp ăn": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1)
    },
    "Cửa hàng bán lẻ": {
        "Bán hàng tại cửa hàng tiện lợi": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán hàng tại siêu thị": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán hàng tại cửa hàng thời trang": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán sách tại nhà sách": (1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        "Bán hàng thực phẩm sạch": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Bán hàng đồ handmade": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán đồ lưu niệm tại bảo tàng": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán hàng tại cửa hàng điện máy": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán hàng tại cửa hàng điện tử": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán hàng tại cửa hàng thể thao": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán hàng tại cửa hàng văn phòng phẩm": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán đồ lưu niệm tại cửa hàng quà tặng": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán giày dép": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1)
    },
    "Khách sạn": {
        "Dọn dẹp khách sạn": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Trực quầy lễ tân": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Điều phối sự kiện tại khách sạn": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1)
    },
    "Dịch vụ khách hàng": {
        "Trực tổng đài": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Chăm sóc khách hàng qua điện thoại": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Hỗ trợ khách hàng qua điện thoại": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Hỗ trợ dịch vụ khách hàng": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Hỗ trợ khách hàng qua email": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Hỗ trợ khách hàng trực tuyến": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Chăm sóc khách hàng qua mạng xã hội": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
    },
    "Giáo dục": {
        "Gia sư": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Trợ giảng tại các trung tâm ngoại ngữ": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Dạy kèm ngoại ngữ": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Hỗ trợ giảng dạy online": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Tư vấn tuyển sinh tại trung tâm": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
    },
     "Vận tải": {
        "Giao hàng": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Vận chuyển hàng hóa": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Giao nhận tài liệu": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Giao báo buổi sáng": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)
    },
    "Kho và hậu cần": {
        "Hỗ trợ kho": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Quản lý kho hàng": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Phụ trách kho hàng": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Đóng gói sản phẩm": (1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1)
    },
    "Sự kiện và giải trí": {
        "Hỗ trợ sự kiện": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Tổ chức sự kiện": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Chụp ảnh sự kiện": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Quay phim": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Hỗ trợ sự kiện thể thao": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1)
    },
    "Marketing và bán hàng": {
        "Bán hàng online": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Tư vấn bán hàng qua điện thoại": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bán vé tại rạp chiếu phim": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Hỗ trợ marketing": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Hỗ trợ marketing online": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Hỗ trợ bán hàng trên sàn TMĐT": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Hỗ trợ livestream bán hàng": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
    },
    "Sản xuất và chế tạo": {
        "Thiết kế đồ họa": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Phát triển nội dung số": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Phát triển nội dung website": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Phát triển phần mềm": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Phát triển ứng dụng di động": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
    },
    "IT và công nghệ": {
        "Hỗ trợ IT": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Sửa chữa máy tính": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Hỗ trợ kỹ thuật máy tính": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Hỗ trợ kỹ thuật tại trường học": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
    },
    "Nội dung và truyền thông": {
        "Cộng tác viên viết bài": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Biên tập nội dung": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Hỗ trợ truyền thông xã hội": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Hỗ trợ sản xuất video": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Quay phim sự kiện cưới": (1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Chụp ảnh sản phẩm online": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Chụp ảnh sản phẩm cho cửa hàng": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
    },    "Chăm sóc khách hàng": {
        "Tư vấn chăm sóc da": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Chăm sóc khách hàng doanh nghiệp": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Chăm sóc khách hàng tại spa": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        "Hỗ trợ khách hàng qua chat": (1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
    },
    "Bảo vệ và an ninh": {
        "Bảo vệ": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Bảo vệ tại trung tâm thương mại": (1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1),
        "Trông coi bãi xe": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)
    },
    "Lao động phổ thông": {
        "Phát tờ rơi": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Dọn dẹp nhà cửa": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Dọn dẹp văn phòng công ty": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Phụ trách vệ sinh tòa nhà": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        "Phụ trách vệ sinh khu vui chơi": (1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)
    },
    }


def result(salary, time, study, opportunities, experience, environment, safety, stress, dropout_rate, alienation, health_problems, academic_performance, mental_health, poor_nutrition):
    positive_factors = [salary, time, study, opportunities, experience, environment, safety]
    negative_factors = [stress, dropout_rate, alienation, health_problems, academic_performance, mental_health, poor_nutrition]

    positive_score = sum(math.log(1 + var) for var in positive_factors) / len(positive_factors)
    negative_score = sum(math.log(1 + var) for var in negative_factors) / len(negative_factors)

    mean_score = positive_score - negative_score

    if mean_score < 0.5:
        return "Không tốt"
    else:
        return "Tốt"

@app.route('/')
def index():
    industries = list(data.keys())
    industries.append("Khác")
    return render_template('index.html', industries=industries)

@app.route('/get_jobs', methods=['POST'])
def get_jobs():
    industry = request.form['industry']
    jobs = list(data.get(industry, {}).keys())
    return jsonify({'jobs': jobs})

@app.route('/evaluate', methods=['POST'])
def evaluate():
    industry = request.form['industry']
    job = request.form['job']

    if industry == "Khác":
        # Save the custom job to a file
        custom_job_file = 'custom_jobs.txt'
        with open(custom_job_file, 'a', encoding='utf-8') as file:
            file.write(f"{job}\n")
        response_message = f"Cảm ơn bạn đã cung cấp công việc: {job}. Chúng tôi sẽ cập nhật sau."
    else:
        variables = data[industry].get(job, None)
        if variables:
            evaluation = result(*variables)
            response_message = f"Ngành nghề '{job}' có môi trường làm việc: {evaluation}.\n Cảm ơn bạn nhiều."
        else:
            response_message = f"Ngành nghề '{job}' không có trong danh sách. Bạn muốn tìm hiểu thêm ngành nghề khác không?"

    return jsonify({'response_message': response_message})

if __name__ == '__main__':
    app.run(debug=True)
