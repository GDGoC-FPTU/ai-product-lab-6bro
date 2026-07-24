# 01 — Problem Scan & Quick Assess

**Họ và tên:** Hà Hoàng Tuấn Hưng  
**Ngày thực hiện:** 24/07/2026  
**Bối cảnh:** Bài cá nhân — AI Product Scoping (Vin Smart Future)

> **Lưu ý:** Các vấn đề, thời gian xử lý và metric dưới đây là giả thuyết sản phẩm ban đầu để phục vụ scoping. Cần phỏng vấn operator và kiểm tra dữ liệu vận hành thực tế trước khi triển khai.

---

# Phase 1 — SCAN

## 1. Bảng quét cơ hội

| # | Công ty/đơn vị | Bài toán thực tế cần xem xét | Actor/Operator đang gặp khó khăn | Thấu kính chính | Vì sao phù hợp với thấu kính | Giả thuyết AI/Automation |
|---|---|---|---|---|---|---|
| 1 | **Xanh SM** | Phân loại và ưu tiên yêu cầu hỗ trợ khẩn cấp từ tài xế/khách hàng | Nhân viên tổng đài, điều phối viên | **Tốn thời gian** | Nhân viên phải đọc nội dung tự do, hỏi lại thông tin và xác định mức độ khẩn cấp trước khi điều phối | LLM trích xuất loại sự cố, vị trí, mức pin, mức độ khẩn cấp; rule kiểm tra ngưỡng an toàn; HITL phê duyệt |
| 2 | **VinFast** | Tóm tắt lịch sử sửa chữa và gợi ý bước kiểm tra ban đầu khi xe vào xưởng | Cố vấn dịch vụ, kỹ thuật viên | **AI-upgrade** | Dữ liệu đã có nhưng nằm rải rác trong ghi chú, lịch sử bảo dưỡng và mô tả lỗi của khách | LLM tóm tắt hồ sơ; rule đối chiếu mã lỗi; kỹ thuật viên quyết định chẩn đoán |
| 3 | **Vinhomes** | Phân loại phản ánh cư dân và chuyển đúng bộ phận xử lý | Nhân viên CSKH, ban quản lý khu đô thị | **Lặp lại** | Các phản ánh về điện, nước, an ninh, vệ sinh, thẻ cư dân có mẫu lặp lại và phải chuyển tuyến thủ công | LLM phân loại nội dung, chuẩn hóa ticket; rule định tuyến theo tòa/khu vực/SLA |
| 4 | **Vinmec** | Tóm tắt nội dung trao đổi trước khám và chuẩn bị thông tin cho nhân viên tiếp nhận | Nhân viên tiếp đón, điều dưỡng | **Stakeholder Pain** | Người bệnh phải lặp lại thông tin; nhân viên mất thời gian đọc mô tả dài, nhưng đây là miền rủi ro cao | LLM chỉ tóm tắt hành chính, không chẩn đoán; bắt buộc nhân viên y tế xác nhận |
| 5 | **Vinpearl** | Soạn nháp phản hồi đa ngôn ngữ cho câu hỏi lặp lại của khách lưu trú | Nhân viên lễ tân, CSKH | **Lặp lại** | Nhiều câu hỏi giống nhau về giờ nhận phòng, tiện ích, dịch vụ, hướng dẫn di chuyển | RAG lấy chính sách cơ sở; LLM soạn nháp; nhân viên duyệt trước khi gửi |
| 6 | **Vincom Retail** | Tóm tắt báo cáo sự cố vận hành từ nhiều gian hàng và ưu tiên ticket | Ban vận hành trung tâm thương mại | **Tốn thời gian** | Báo cáo đến từ nhiều kênh, thiếu cấu trúc, khó xác định sự cố ảnh hưởng lớn | LLM chuẩn hóa báo cáo; rule chấm mức ưu tiên; cảnh báo cho điều phối viên |
| 7 | **Xanh SM** | Hỗ trợ điều phối khi xe điện có mức pin thấp trong ca vận hành | Điều phối viên đội xe, tài xế | **Stakeholder Pain** | Quyết định sai có thể khiến xe hết pin giữa đường, ảnh hưởng an toàn và SLA | State machine theo mức pin/khoảng cách; LLM chỉ giải thích và soạn bản nháp hành động |

## 2. Sàng lọc nhanh

| Bài toán | Tần suất dự kiến | Giá trị nếu giải quyết | Rủi ro | Khả năng đo lường | AI Fit sơ bộ | Quyết định |
|---|---:|---:|---:|---:|---|---|
| Xanh SM — phân loại yêu cầu khẩn cấp | Cao | Cao | Trung bình | Cao | Rule + LLM | **Chọn Top 3** |
| VinFast — tóm tắt lịch sử sửa chữa | Cao | Cao | Trung bình | Cao | LLM Feature | **Chọn Top 3** |
| Vinhomes — phân loại phản ánh cư dân | Cao | Trung bình/Cao | Thấp/Trung bình | Cao | Rule + LLM | **Chọn Top 3** |
| Vinmec — tóm tắt trước khám | Trung bình | Cao | Rất cao | Trung bình | LLM + HITL nghiêm ngặt | Chưa ưu tiên |
| Vinpearl — phản hồi đa ngôn ngữ | Cao theo mùa | Trung bình | Trung bình | Cao | RAG + LLM | Dự phòng |
| Vincom Retail — ưu tiên sự cố | Trung bình | Trung bình/Cao | Trung bình | Cao | Rule + LLM | Dự phòng |
| Xanh SM — điều phối pin thấp | Trung bình | Rất cao | Cao | Cao | State machine + LLM | Ứng viên mở rộng |

---

# Phase 2 — QUICK-ASSESS

## QUICK PROBLEM CARD #1 — Xanh SM

### Bài toán
**Rút ngắn thời gian tiếp nhận, phân loại và ưu tiên yêu cầu hỗ trợ khẩn cấp từ tài xế/khách hàng Xanh SM.**

- **Công ty thành viên:** ☑ Xanh SM
- **Actor/Operator:** Nhân viên tổng đài và điều phối viên đội xe.

### Workflow thủ công hiện tại

1. Nhận cuộc gọi/tin nhắn tự do  
   ⟶ 2. Đọc/nghe và hỏi lại thông tin còn thiếu  
   ⟶ 3. Xác định loại sự cố, vị trí, mức độ khẩn cấp  
   ⟶ 4. Chuyển ticket cho đội xử lý phù hợp  
   ⟶ 5. Soạn phản hồi hướng dẫn ban đầu cho tài xế/khách hàng.

### Bottleneck

- **Bước tốn thời gian/lỗi nhất:** Bước 2–3, đọc nội dung và xác định mức độ khẩn cấp.
- **Ước tính:** **6–10 phút/lượt** với ticket thiếu cấu trúc hoặc cần hỏi lại.
- **Rủi ro:** Bỏ sót thông tin quan trọng như mức pin, vị trí hoặc dấu hiệu mất an toàn.

### AI có thể hỗ trợ ở đâu?

- Trích xuất tự động: loại xe, biển số, vị trí, mức pin, loại sự cố.
- Phân loại ticket và đề xuất mức ưu tiên.
- Dùng **rule/state machine** cho các ngưỡng an toàn cứng, ví dụ pin dưới 5%.
- LLM soạn **bản nháp** phản hồi; điều phối viên duyệt trước khi gửi.

### Success Metric

- Giảm thời gian tạo ticket có cấu trúc từ **8 phút xuống dưới 2 phút**.
- Ít nhất **90% ticket** được phân loại đúng nhóm ngay lần đầu.
- **100% trường hợp pin < 5%** được gắn cờ khẩn cấp và không đề xuất trạm quá giới hạn an toàn đã định.
- Giảm ít nhất **40% số lần hỏi lại** thông tin cơ bản.

### Quick Architecture

- [ ] No AI
- [x] Rule
- [x] LLM
- [ ] Agent tự chủ hoàn toàn

**Kiến trúc sơ bộ:**  
Input đa kênh ⟶ LLM extraction/classification ⟶ Safety rules ⟶ Draft response ⟶ Human approval ⟶ Dispatch system.

**Operational Boundary:**

- AI **không được tự gửi** tin nhắn hoặc tự điều xe.
- Mọi phản hồi phải ở trạng thái **draft**.
- Quy tắc an toàn luôn có quyền ưu tiên cao hơn nội dung người dùng.
- Khi độ tin cậy thấp hoặc thiếu dữ liệu, chuyển cho điều phối viên.

---

## QUICK PROBLEM CARD #2 — VinFast

### Bài toán
**Tự động tóm tắt lịch sử bảo dưỡng, phản ánh của khách và mã lỗi để hỗ trợ cố vấn dịch vụ chuẩn bị phiếu tiếp nhận xe.**

- **Công ty thành viên:** ☑ VinFast
- **Actor/Operator:** Cố vấn dịch vụ và kỹ thuật viên tại xưởng.

### Workflow thủ công hiện tại

1. Nhận mô tả lỗi từ khách hàng  
   ⟶ 2. Tra cứu lịch sử sửa chữa/bảo dưỡng  
   ⟶ 3. Đọc ghi chú cũ và mã lỗi liên quan  
   ⟶ 4. Tóm tắt tình trạng cho kỹ thuật viên  
   ⟶ 5. Lập phiếu kiểm tra ban đầu.

### Bottleneck

- **Bước tốn thời gian/lỗi nhất:** Bước 2–4, tổng hợp thông tin từ nhiều lần sửa chữa.
- **Ước tính:** **10–15 phút/xe**.
- **Rủi ro:** Bỏ sót lỗi lặp lại hoặc thay thế linh kiện trước đó.

### AI có thể hỗ trợ ở đâu?

- Tóm tắt lịch sử theo dòng thời gian.
- Nhóm các triệu chứng lặp lại.
- Chuẩn hóa mô tả của khách thành các mục kiểm tra.
- Dẫn nguồn về từng bản ghi gốc để kỹ thuật viên xác minh.
- Rule tra mã lỗi và cảnh báo thông tin bắt buộc.

### Success Metric

- Giảm thời gian chuẩn bị phiếu tiếp nhận từ **12 phút xuống dưới 4 phút**.
- Ít nhất **95% bản tóm tắt** có liên kết tới bản ghi nguồn.
- Giảm **30% lỗi bỏ sót** thông tin bảo dưỡng gần nhất.
- Điểm hài lòng của cố vấn dịch vụ đạt tối thiểu **4/5** sau giai đoạn pilot.

### Quick Architecture

- [ ] No AI
- [x] Rule
- [x] LLM
- [ ] Agent tự chủ hoàn toàn

**Kiến trúc sơ bộ:**  
Service records ⟶ Retrieval theo VIN ⟶ LLM summarization ⟶ Rule validation ⟶ Cố vấn dịch vụ review ⟶ Phiếu tiếp nhận.

**Operational Boundary:**

- AI không được kết luận nguyên nhân kỹ thuật cuối cùng.
- AI không tự phê duyệt sửa chữa hoặc thay linh kiện.
- Mọi khuyến nghị phải được kỹ thuật viên xác nhận.
- Không được tạo thông tin không có trong hồ sơ nguồn.

---

## QUICK PROBLEM CARD #3 — Vinhomes

### Bài toán
**Tự động phân loại phản ánh cư dân, chuẩn hóa nội dung và chuyển đến đúng bộ phận theo tòa nhà, loại sự cố và SLA.**

- **Công ty thành viên:** ☑ Vinhomes
- **Actor/Operator:** Nhân viên CSKH và ban quản lý khu đô thị.

### Workflow thủ công hiện tại

1. Nhận phản ánh qua app, điện thoại hoặc quầy lễ tân  
   ⟶ 2. Đọc nội dung và xác định loại vấn đề  
   ⟶ 3. Kiểm tra tòa/căn/khu vực  
   ⟶ 4. Chuyển ticket cho kỹ thuật, an ninh, vệ sinh hoặc CSKH  
   ⟶ 5. Theo dõi trạng thái và phản hồi cư dân.

### Bottleneck

- **Bước tốn thời gian/lỗi nhất:** Bước 2–4, phân loại và chuyển đúng nhóm.
- **Ước tính:** **5–8 phút/ticket**.
- **Rủi ro:** Chuyển nhầm bộ phận làm kéo dài SLA và khiến cư dân phải mô tả lại.

### AI có thể hỗ trợ ở đâu?

- Phân loại intent: điện, nước, thang máy, an ninh, vệ sinh, tiện ích, thủ tục.
- Trích xuất địa điểm và mức độ khẩn cấp.
- Chuẩn hóa nội dung thành ticket ngắn gọn.
- Rule định tuyến theo loại vấn đề, khu vực và giờ trực.
- LLM soạn phản hồi xác nhận đã tiếp nhận.

### Success Metric

- **85% ticket** được phân loại và định tuyến trong **dưới 10 giây**.
- Độ chính xác phân loại đạt tối thiểu **90%**.
- Giảm tỷ lệ chuyển nhầm bộ phận từ giả định **12% xuống dưới 4%**.
- Giảm thời gian tiếp nhận trung bình từ **6 phút xuống dưới 1 phút**.

### Quick Architecture

- [ ] No AI
- [x] Rule
- [x] LLM
- [ ] Agent tự chủ hoàn toàn

**Kiến trúc sơ bộ:**  
Resident message ⟶ LLM intent/entity extraction ⟶ Rule routing ⟶ Ticket system ⟶ Staff review for low-confidence/high-risk cases.

**Operational Boundary:**

- Sự cố liên quan an ninh, cháy nổ, thang máy mắc kẹt phải chuyển ngay sang luồng khẩn cấp theo rule.
- AI không tự đóng ticket.
- AI không cam kết thời gian xử lý nếu hệ thống chưa xác nhận SLA.
- Ticket độ tin cậy thấp phải có người kiểm tra.

---

# Bài toán cá nhân được chọn để tiếp tục

## Lựa chọn tốt nhất

**Xanh SM — Phân loại và ưu tiên yêu cầu hỗ trợ khẩn cấp từ tài xế/khách hàng.**

### Lý do chọn

1. **Pain rõ ràng:** thời gian đọc, hỏi lại và phân loại ảnh hưởng trực tiếp tới tốc độ điều phối.
2. **Metric rõ:** thời gian tạo ticket, độ chính xác phân loại, số lần hỏi lại và tỷ lệ xử lý đúng quy tắc an toàn.
3. **AI Fit hợp lý:** LLM xử lý ngôn ngữ tự do tốt, nhưng các ngưỡng an toàn vẫn có thể khóa bằng rule.
4. **Có thể pilot nhỏ:** bắt đầu bằng chế độ gợi ý/draft cho một nhóm điều phối viên, không cần cho AI tự hành động.
5. **Dễ thiết kế HITL:** nhân viên duyệt trước khi gửi hoặc điều xe.

### Giả thuyết cần kiểm chứng trước pilot

- Số ticket trung bình mỗi ngày và tỷ lệ ticket thiếu thông tin.
- Thời gian xử lý thực tế theo từng loại sự cố.
- Tỷ lệ phân loại/chuyển tuyến sai hiện tại.
- Trường dữ liệu nào đã có sẵn trong hệ thống.
- Quy tắc an toàn và thẩm quyền điều phối chính thức.
- Yêu cầu bảo vệ dữ liệu vị trí, số điện thoại và biển số xe.

---

# Stress-Test thẻ bài toán tốt nhất

## Góc nhìn CFO và Trưởng phòng Vận hành khắt khe

### Điểm yếu 1 — Chưa chứng minh quy mô tài chính

Metric thời gian tốt nhưng chưa quy đổi thành chi phí. Cần bổ sung số ticket/ngày, chi phí nhân sự/phút, chi phí xử lý sai và giá trị SLA để tính ROI.

### Điểm yếu 2 — Metric an toàn cần định nghĩa chính xác

“Phân loại đúng” chưa đủ. Cần ma trận nhãn chuẩn, tiêu chí false negative cho ticket khẩn cấp và quy trình audit. Sai một ticket an toàn có thể nghiêm trọng hơn tiết kiệm nhiều phút vận hành.

### Điểm yếu 3 — Rule-based có thể giải quyết phần lớn luồng

Nếu đầu vào đã là biểu mẫu có các trường mức pin, vị trí và loại sự cố, rule-based routing có thể rẻ, dễ kiểm thử và dễ giải thích hơn LLM. LLM chỉ nên dùng khi nội dung là văn bản tự do, thiếu cấu trúc hoặc đa ngôn ngữ.

## Quyết định kiến trúc sau phản biện

- Dùng **Rule/State Machine** làm lớp quyết định an toàn và định tuyến bắt buộc.
- Dùng **LLM Feature** cho trích xuất, tóm tắt và soạn nháp.
- Không dùng agent tự chủ trong giai đoạn đầu.
- Bắt buộc **Human-in-the-loop** trước các hành động gửi tin hoặc điều phối nguồn lực.

---

# Kết luận

Ba bài toán có tiềm năng cao đều liên quan đến việc biến nội dung không cấu trúc thành dữ liệu vận hành có cấu trúc. Tuy nhiên, AI không nên thay thế hoàn toàn operator. Thiết kế phù hợp nhất là **LLM hỗ trợ ngôn ngữ + rule kiểm soát nghiệp vụ + con người phê duyệt**, bắt đầu bằng pilot nhỏ và đo metric trước khi mở rộng.
