# Lab 02 — Problem Scan & Quick Assessments

## 🔍 Phase 1 — SCAN (Cá nhân)

Dưới đây là bảng quét cơ hội (SCAN) ứng dụng AI tại các công ty thành viên thuộc tập đoàn Vingroup, sử dụng **4 Lenses** (Thấu kính) để tìm kiếm các nút thắt cổ chai thực tế trong vận hành.

### 📝 Bảng quét cơ hội (SCAN):

| # | Công ty thành viên | Thấu kính (Lens) | Quy trình thủ công & Mô tả ngắn bài toán |
|---|---------------------|------------------|----------------------------------------|
| 1 | **Vinhomes** | Tốn thời gian (Time-consuming) | **Xử lý và phản hồi ý kiến cư dân trên ứng dụng VinID:** Nhân viên vận hành tòa nhà phải đọc thủ công hàng trăm phản hồi, khiếu nại (tiếng ồn, rác thải, hỏng hóc thiết bị), tự phân loại rồi soạn thư trả lời cư dân theo cách thủ công. |
| 2 | **Vinmec** | Tốn thời gian (Time-consuming) | **Tóm tắt hồ sơ bệnh án xuất viện:** Bác sĩ và nhân viên hành chính phải đọc lại hàng loạt tài liệu lâm sàng (ghi chú khám, kết quả xét nghiệm, lịch sử đơn thuốc) để viết báo cáo tóm tắt xuất viện và hồ sơ gửi bảo hiểm. |
| 3 | **Xanh SM (GSM)** | Stakeholder Pain & Lặp lại | **Hỗ trợ định vị lại lộ trình tối ưu khi gặp sự cố trên đường:** Tài xế khi gặp tắc đường bất ngờ hoặc sự cố giao thông phải vừa lái xe vừa tra cứu bản đồ ngoài (Google Maps) để tìm đường mới và thương lượng lộ trình với khách hàng. |
| 4 | **VinFast** | Lặp lại (Repetitive) | **Đối soát hóa đơn sạc điện của khách hàng:** Nhân viên kế toán đối soát thủ công mã giao dịch ngân hàng với lịch sử phiên sạc trên hệ thống cơ sở dữ liệu khi có sai lệch mô tả chuyển khoản từ người dùng. |
| 5 | **Vinpearl** | AI-upgrade | **Tư vấn lịch trình du lịch cá nhân hóa tại resort:** Nhân viên CSKH/Concierge trao đổi thủ công với du khách qua Zalo/Email để tư vấn lịch trình vui chơi tại VinWonders, ăn uống và thư giãn dựa trên sở thích riêng lẻ của gia đình họ. |

---

## 🃏 Phase 2 — QUICK-ASSESS (Cá nhân)

Chọn 3 bài toán tiềm năng nhất từ danh sách trên để phân tích sơ bộ qua các thẻ bài toán (Quick Problem Cards).

### 1. QUICK PROBLEM CARD #1: Phân loại và Phản hồi tự động Khiếu nại Cư dân (Vinhomes)
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tự động hóa phân loại khiếu nại và soạn   │
│ thảo thư phản hồi cá nhân hóa cho cư dân trên VinID.        │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH/Ban quản lý tòa nhà.    │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Cư dân gửi khiếu nại qua app VinID.                    │
│   2. Nhân viên đọc thủ công, phân loại nội dung khiếu nại.  │
│   3. Chuyển giao thông tin tới bộ phận kỹ thuật/vệ sinh...  │
│   4. Soạn thảo thư phản hồi lịch sự theo mẫu.               │
│   5. Gửi thư phản hồi xác nhận cho cư dân.                  │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Soạn thư phản hồi thủ công │
│ và phân loại chính xác bộ phận xử lý (⏱ 10 phút/lượt).      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Phân loại tự động và  │
│ soạn thảo dự thảo thư phản hồi cho cư dân.                  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian soạn phản hồi từ 10 phút ──> dưới 1.5 phút  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 2. QUICK PROBLEM CARD #2: Tóm tắt Hồ sơ Bệnh án xuất viện Chuẩn Y khoa (Vinmec)
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động tổng hợp dữ liệu lâm sàng thô     │
│ để tạo dự thảo báo cáo tóm tắt xuất viện cho bệnh nhân.     │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị và Thư ký y khoa.      │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Bệnh nhân có chỉ định xuất viện từ bác sĩ.             │
│   2. Bác sĩ tra cứu lại toàn bộ bệnh án trên hệ thống EHR.   │
│   3. Tổng hợp tay các kết quả xét nghiệm, đơn thuốc, chẩn   │
│      đoán thành văn bản tóm tắt y khoa ra viện.            │
│   4. Ký duyệt hồ sơ và gửi cho bộ phận kế toán/bảo hiểm.     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Đọc hiểu, lọc thông tin    │
│ chính xác từ các file bệnh án rải rác (⏱ 20 phút/lượt).     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Trích xuất thông tin, │
│ tổng hợp dữ liệu và viết dự thảo tóm tắt xuất viện y khoa.   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian tạo tóm tắt bệnh án từ 20 phút ──> dưới 3    │
│   phút (bác sĩ chỉ cần kiểm tra nhanh và nhấn nút duyệt).   │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 3. QUICK PROBLEM CARD #3: Trợ lý Lộ trình và Điều vận Thông minh (Xanh SM)
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Hỗ trợ tài xế tìm kiếm lộ trình thay thế  │
│ tối ưu qua giọng nói rảnh tay khi phát hiện tắc đường.      │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế Xanh SM đang chở khách thực địa. │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Xe gặp sự cố tắc đường hoặc rào chắn trên lộ trình.   │
│   2. Tài xế dừng xe hoặc vừa lái vừa mở app phụ bản đồ.    │
│   3. Tra cứu, gõ tìm lộ trình tránh tắc đường.               │
│   4. Giải thích và thương lượng phương án mới với khách.    │
│   5. Đổi hướng di chuyển.                                   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Tìm kiếm đường thay thế    │
│ thủ công và giải thích cho khách hàng (⏱ 3-5 phút/lượt).     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Nhận diện giọng nói, │
│ tự động đề xuất lộ trình mới và tạo mẫu thông báo cho khách.│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian xử lý định vị lại lộ trình từ 3 phút       │
│   ──> dưới 10 giây qua tương tác giọng nói an toàn.          │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘
```
