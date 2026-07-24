## 1. Bảng quét cơ hội (Opportunity SCAN Table)

| STT | Công ty thành viên | Tên bài toán tiềm năng | Thấu kính áp dụng (Lens) |
| :--- | :--- | :--- | :--- |
| 1 | **Vinmec** | Tóm tắt hồ sơ bệnh án, lịch sử khám chữa bệnh dài hạn cho bác sĩ trước ca khám. | **Tốn thời gian** (Time-consuming) |
| 2 | **Vinhomes** | Phân loại và tự động điều phối các yêu cầu bảo trì (điện, nước, vệ sinh) từ cư dân qua app. | **Lặp lại** (Repetitive) |
| 3 | **Xanh SM** | Dự đoán nhu cầu gọi xe tăng đột biến do thời tiết/sự kiện để điều phối xe nhàn rỗi (Proactive Dispatching). | **Nỗi đau Stakeholder** (Stakeholder Pain - Tài xế & Điều phối viên) |
| 4 | **VinFast** | Trợ lý ảo (In-car Virtual Assistant) cá nhân hóa, hiểu ngữ cảnh đàm thoại tự nhiên và ra lệnh điều khiển xe. | **Nâng cấp AI** (AI-upgrade) |
| 5 | **Vinpearl** | Tạo lịch trình du lịch cá nhân hóa tự động cho nhóm khách gia đình dựa trên sở thích và tình trạng phòng/vé. | **Tốn thời gian & Nâng cấp AI** (Time-consuming, AI-upgrade) |

---

## 2. Thẻ bài toán nhanh (3 Quick Problem Cards)

### 💳 Problem Card 1: Tóm tắt hồ sơ y tế bệnh nhân
*   **Tên bài toán:** Rút trích và tóm tắt lịch sử khám chữa bệnh.
*   **Công ty thành viên:** Vinmec.
*   **Tác nhân (Actor):** Bác sĩ / Y tá tiếp nhận.
*   **Quy trình thủ công hiện tại:** 
    1. Bệnh nhân check-in.
    2. Bác sĩ mở hệ thống HIS (Hospital Information System).
    3. Bác sĩ đọc lại các ghi chú y khoa, toa thuốc, và kết quả xét nghiệm của 5-10 lần khám trước.
    4. Bác sĩ ghi chú lại các bệnh lý nền và rủi ro dị ứng.
    5. Bắt đầu phiên khám mới.
*   **Bước tốn thời gian/Gây lỗi nhất:** Đọc và tổng hợp thông tin từ nhiều trang ghi chú cũ (Ước tính: **10 - 15 phút/bệnh nhân**). Nguy cơ bỏ sót thông tin dị ứng thuốc nếu bác sĩ đọc lướt.
*   **Bước AI tham gia:** LLM tự động tổng hợp toàn bộ hồ sơ cũ và hiển thị một thẻ "Key Medical History" (Gồm: Bệnh lý nền, Thuốc đang dùng, Dị ứng, Lịch sử phẫu thuật) ngay khi bác sĩ mở hồ sơ.
*   **Metric đo lường thành công:** Giảm thời gian đọc hiểu hồ sơ y tế trước ca khám từ **15 phút xuống dưới 2 phút**, đạt độ chính xác > 99% trong việc trích xuất thông tin dị ứng.
*   **Kiến trúc đề xuất:** LLM (Sử dụng kỹ thuật RAG trên kho dữ liệu y bạ của bệnh nhân).

---

### 💳 Problem Card 2: Điều vận thông minh đa luồng
*   **Tên bài toán:** Điều phối xe chủ động dựa trên tín hiệu thời tiết và kẹt xe.
*   **Công ty thành viên:** Xanh SM.
*   **Tác nhân (Actor):** Điều phối viên (Dispatcher) / Tài xế.
*   **Quy trình thủ công hiện tại:**
    1. Trời bắt đầu mưa lớn hoặc có sự kiện.
    2. Nhu cầu gọi xe tại một khu vực tăng vọt.
    3. Điều phối viên nhìn bản đồ nhiệt (heatmap), phát hiện thiếu hụt xe.
    4. Điều phối viên gửi tin nhắn broadcast kêu gọi tài xế di chuyển về khu vực đó.
    5. Tài xế đọc tin nhắn và tự quyết định có chạy xe không khách (deadhead) đến đó không.
*   **Bước tốn thời gian/Gây lỗi nhất:** Việc giám sát heatmap và kêu gọi tài xế bị trễ nhịp (độ trễ **20 - 30 phút**), dẫn đến khách hàng phải chờ lâu và hủy chuyến.
*   **Bước AI tham gia:** Hệ thống liên tục quét dữ liệu thời tiết và luồng giao thông. Khi có dấu hiệu bất thường, AI Agent tự động tính toán chi phí cơ hội và trực tiếp gợi ý lộ trình di chuyển "đón đầu" cho các tài xế đang nhàn rỗi ở khu vực lân cận, kèm theo phần thưởng thưởng điểm.
*   **Metric đo lường thành công:** Giảm thời gian khách hàng chờ xe trong điều kiện thời tiết xấu từ **hơn 15 phút xuống dưới 7 phút**.
*   **Kiến trúc đề xuất:** AI Agent (Kết hợp Rule-based cho các ngưỡng trigger và Agent để tính toán, đàm phán luồng tài xế).

---

### 💳 Problem Card 3: Tự động phân luồng yêu cầu từ cư dân
*   **Tên bài toán:** Phân loại yêu cầu hỗ trợ bảo trì qua ứng dụng.
*   **Công ty thành viên:** Vinhomes.
*   **Tác nhân (Actor):** Lễ tân tòa nhà / Ban quản lý.
*   **Quy trình thủ công hiện tại:**
    1. Cư dân gửi yêu cầu qua app (định dạng văn bản tự do, VD: *"Điều hòa phòng khách kêu to quá mà nước chảy lênh láng"*).
    2. Lễ tân đọc tin nhắn trên hệ thống CRM.
    3. Lễ tân xác định phân loại sự cố (Điện, Nước, Mộc, Vệ sinh).
    4. Lễ tân tạo ticket và gán cho đội kỹ thuật tương ứng.
*   **Bước tốn thời gian/Gây lỗi nhất:** Đọc và phân loại thủ công các đoạn văn bản tự do, đặc biệt dễ quá tải và chậm trễ (tắc nghẽn) vào giờ cao điểm hoặc buổi tối (Ước tính: **3 - 5 phút/ticket**).
*   **Bước AI tham gia:** AI đọc hiểu tin nhắn tự do của cư dân, tự động trích xuất các thông tin (Mã căn hộ, Loại sự cố, Mức độ khẩn cấp) và gán thẳng ticket cho trưởng ca kỹ thuật phù hợp mà không cần lễ tân can thiệp.
*   **Metric đo lường thành công:** Giảm thời gian xử lý và phân luồng ticket từ **5 phút xuống dưới 5 giây/ticket** với tỷ lệ định tuyến sai (misrouting) dưới 3%.
*   **Kiến trúc đề xuất:** LLM (Sử dụng prompt cơ bản với cấu trúc đầu ra JSON để tích hợp thẳng vào CRM).