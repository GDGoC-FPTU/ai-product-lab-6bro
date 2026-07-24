# 01-problem-scan.md

## Bài cá nhân — Phase 1: SCAN & Phase 2: QUICK-ASSESS

> **Phạm vi:** Các cơ hội AI trong hoạt động vận hành và kinh doanh của Vinhomes.  
> **Lưu ý về dữ liệu:** Các quy trình, thời gian và sản lượng dưới đây là **giả định làm việc** phục vụ bài tập, không phải số liệu nội bộ đã được xác minh. Khi triển khai thực tế cần phỏng vấn Operator, lấy log hệ thống và đo baseline trong 1–2 tuần.

---

# Phase 1 — SCAN

## 1. Bảng quét cơ hội

| #   | Bài toán thực tế                                                                | Đơn vị                                | Actor/Operator                            | Dấu hiệu vấn đề                                                                          | Thấu kính chính      | Thấu kính phụ                               | Vì sao đáng xem xét                                                                                      |
| --- | ------------------------------------------------------------------------------- | ------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| 1   | Phân loại và định tuyến yêu cầu dịch vụ cư dân từ app, hotline, email và chat   | Vinhomes / Ban quản lý khu đô thị     | Nhân viên CSKH, điều phối viên vận hành   | Phải đọc từng yêu cầu, hiểu ý định, xác định mức ưu tiên và chuyển đúng đội xử lý        | **Lặp lại**          | Tốn thời gian, Stakeholder Pain, AI-upgrade | Khối lượng lớn, quy tắc định tuyến tương đối rõ nhưng ngôn ngữ cư dân đa dạng; có thể kết hợp Rule + LLM |
| 2   | Tạo biên bản lỗi bàn giao căn hộ từ ảnh, ghi chú và giọng nói của kỹ thuật viên | Vinhomes / Ban bàn giao               | Kỹ thuật viên kiểm tra, điều phối sửa lỗi | Ghi chép rời rạc, nhập lại dữ liệu, mô tả lỗi không đồng nhất, dễ bỏ sót ảnh hoặc vị trí | **Tốn thời gian**    | Lặp lại, AI-upgrade                         | Multimodal AI có thể chuẩn hóa mô tả lỗi, gắn ảnh, vị trí và mức độ nghiêm trọng                         |
| 3   | Kiểm tra tính đầy đủ và trích xuất dữ liệu từ hồ sơ khách hàng/giao dịch        | Vinhomes / Kinh doanh, vận hành hồ sơ | Nhân viên xử lý hồ sơ                     | Đối chiếu nhiều loại giấy tờ, nhập dữ liệu lặp lại, phát hiện thiếu/sai muộn             | **Lặp lại**          | Tốn thời gian, Stakeholder Pain             | Document AI + Rule phù hợp; metric rõ về thời gian xử lý và tỷ lệ hồ sơ phải bổ sung                     |
| 4   | Trợ lý tra cứu quy định, phí dịch vụ và hướng dẫn thủ tục cho cư dân            | Vinhomes / CSKH                       | Nhân viên tổng đài, lễ tân, cư dân        | Câu hỏi lặp lại, tài liệu phân tán, trả lời không đồng nhất giữa nhân viên               | **AI-upgrade**       | Lặp lại, Stakeholder Pain                   | RAG có thể hỗ trợ tra cứu có nguồn; cần giới hạn trả lời theo tài liệu được duyệt                        |
| 5   | Tóm tắt khiếu nại và phát hiện vấn đề tái diễn theo tòa/khu vực                 | Vinhomes / Quản lý chất lượng dịch vụ | Trưởng nhóm CSKH, quản lý vận hành        | Phải đọc nhiều ticket để tổng hợp nguyên nhân, xu hướng và mức độ ảnh hưởng              | **Tốn thời gian**    | AI-upgrade, Stakeholder Pain                | LLM hỗ trợ tóm tắt; analytics phát hiện cụm vấn đề và xu hướng                                           |
| 6   | Ưu tiên lệnh bảo trì dựa trên mức độ khẩn cấp, SLA và ảnh hưởng cư dân          | Vinhomes / Kỹ thuật vận hành          | Điều phối bảo trì                         | Thứ tự xử lý phụ thuộc kinh nghiệm cá nhân; dễ ưu tiên sai khi có nhiều ticket đồng thời | **Stakeholder Pain** | Rule, AI-upgrade                            | Có thể bắt đầu bằng Rule engine; sau khi đủ dữ liệu mới dùng ML để dự báo rủi ro trễ SLA                 |
| 7   | Dự báo hỏng hóc thiết bị chung như thang máy, bơm, HVAC                         | Vinhomes / Kỹ thuật tòa nhà           | Kỹ sư vận hành, quản lý tài sản           | Bảo trì phản ứng sau sự cố; downtime ảnh hưởng nhiều cư dân                              | **AI-upgrade**       | Stakeholder Pain                            | Tiềm năng cao nhưng phụ thuộc dữ liệu sensor, lịch sử bảo trì và chuẩn hóa mã lỗi                        |
| 8   | Hỗ trợ nhân viên kinh doanh soạn nội dung follow-up cá nhân hóa sau tư vấn      | Vinhomes / Kinh doanh                 | Chuyên viên tư vấn                        | Soạn tin nhắn lặp lại, thông tin khách hàng dễ bị bỏ sót hoặc diễn đạt không nhất quán   | **Lặp lại**          | AI-upgrade                                  | LLM phù hợp ở chế độ gợi ý; bắt buộc nhân viên duyệt trước khi gửi                                       |

## 2. Sàng lọc ban đầu

Thang điểm 1–5:

- **Impact:** Tác động vận hành/khách hàng.
- **Frequency:** Tần suất xảy ra.
- **Measurability:** Dễ đo baseline và kết quả.
- **AI Fit:** Mức phù hợp với AI hiện tại.
- **Feasibility:** Khả năng PoC trong 8–12 tuần.
- **Risk:** Rủi ro dữ liệu, pháp lý, sai quyết định; điểm cao nghĩa là rủi ro cao.

| Bài toán                              | Impact | Frequency | Measurability | AI Fit | Feasibility | Risk | Nhận định                                                                           |
| ------------------------------------- | -----: | --------: | ------------: | -----: | ----------: | ---: | ----------------------------------------------------------------------------------- |
| Phân loại & định tuyến yêu cầu cư dân |      5 |         5 |             5 |      5 |           4 |    3 | **Ưu tiên 1** — quy trình rõ, dữ liệu ticket có thể sẵn có, HITL dễ thiết kế        |
| Tạo biên bản lỗi bàn giao             |      5 |         4 |             4 |      5 |           3 |    3 | **Ưu tiên 2** — giá trị cao, nhưng cần dữ liệu ảnh/voice và chuẩn taxonomy lỗi      |
| Kiểm tra hồ sơ khách hàng/giao dịch   |      4 |         5 |             5 |      4 |           4 |    4 | **Ưu tiên 3** — metric rõ, cần kiểm soát dữ liệu cá nhân và không tự động phê duyệt |
| Trợ lý tra cứu quy định               |      4 |         5 |             4 |      5 |           4 |    3 | Tốt cho PoC nhưng tác động có thể thấp hơn ba bài toán trên                         |
| Tóm tắt khiếu nại & xu hướng          |      4 |         4 |             4 |      4 |           4 |    2 | Quick win cho quản lý, ít can thiệp trực tiếp vào giao dịch                         |
| Ưu tiên lệnh bảo trì                  |      5 |         4 |             4 |      3 |           3 |    4 | Nên bắt đầu Rule-based, tránh để AI tự quyết định sự cố an toàn                     |
| Predictive maintenance                |      5 |         3 |             3 |      3 |           2 |    4 | Chưa phù hợp nếu thiếu sensor/log chuẩn hóa                                         |
| Soạn follow-up kinh doanh             |      3 |         5 |             3 |      5 |           5 |    3 | Dễ làm nhưng cần kiểm soát nội dung và dữ liệu khách hàng                           |

---

# Phase 2 — QUICK-ASSESS

# Quick Problem Card 1

## Tên bài toán

**AI tiếp nhận, phân loại và định tuyến yêu cầu dịch vụ cư dân — Vinhomes**

### 1. Actor/Operator

- Nhân viên CSKH tiếp nhận yêu cầu.
- Điều phối viên vận hành.
- Đội kỹ thuật, an ninh, vệ sinh, tiện ích và các nhà thầu liên quan.
- Cư dân là stakeholder bị ảnh hưởng bởi tốc độ và độ chính xác xử lý.

### 2. Current Manual Workflow

```text
Cư dân gửi yêu cầu
    ↓
CSKH đọc nội dung/ảnh
    ↓
Xác định loại vấn đề
    ↓
Đánh giá mức độ khẩn cấp
    ↓
Tra cứu tòa/căn/khu vực
    ↓
Chọn đội xử lý
    ↓
Tạo/chỉnh ticket và chuyển giao
    ↓
Đội xử lý xác nhận hoặc trả lại nếu phân loại sai
```

### 3. Bottleneck

- Bước tốn thời gian nhất: đọc nội dung, xác định category, priority và routing.
- **Baseline giả định:** 4–7 phút/ticket; ticket mơ hồ có thể mất 10–15 phút.
- Lỗi phổ biến: chọn sai category, thiếu thông tin, chuyển sai đội, bỏ sót dấu hiệu khẩn cấp.
- Hệ quả: tăng thời gian phản hồi đầu tiên, ticket bị chuyển vòng và nguy cơ trễ SLA.

### 4. AI Intervention

- Rule kiểm tra các từ khóa nguy hiểm: cháy, khói, mất điện diện rộng, kẹt thang máy, rò rỉ nước lớn.
- LLM trích xuất:
  - ý định;
  - vị trí;
  - đối tượng/sự cố;
  - mức độ khẩn cấp;
  - thông tin còn thiếu.
- Classifier đề xuất category, priority và đội xử lý.
- Hệ thống tạo draft ticket; nhân viên duyệt trước khi gửi.
- Với ticket confidence thấp hoặc thuộc nhóm an toàn, tự động escalates cho người trực.

### 5. Success Metrics

> Các ngưỡng cần xác minh sau khi đo baseline thật.

- Giảm thời gian phân loại trung vị từ **5 phút xuống dưới 90 giây/ticket**.
- Tỷ lệ định tuyến đúng ngay lần đầu đạt **≥ 90%**.
- Giảm ticket bị chuyển lại giữa các đội ít nhất **40%**.
- Recall phát hiện ticket khẩn cấp đạt **≥ 98%**.
- 100% quyết định priority cao có log giải thích và người duyệt.
- Không tăng tỷ lệ khiếu nại do phân loại sai so với baseline.

### 6. Kiến trúc sơ bộ

**Khuyến nghị: Rule + LLM Feature trước; Agentic Loop chỉ ở giai đoạn sau.**

```text
Input Gateway
 → PII Redaction
 → Safety Rules
 → LLM Information Extraction
 → Category/Priority Classifier
 → Routing Rules
 → Human Approval
 → Ticket System
 → Monitoring & Feedback
```

- **Không dùng Agent tự chủ hoàn toàn** ở PoC.
- Agent chỉ phù hợp sau khi có API ổn định, permission rõ và dữ liệu đánh giá đủ lớn.

---

# Quick Problem Card 2

## Tên bài toán

**AI tạo biên bản lỗi bàn giao căn hộ từ ảnh, ghi chú và giọng nói — Vinhomes**

### 1. Actor/Operator

- Kỹ thuật viên kiểm tra căn hộ.
- Điều phối viên sửa lỗi.
- Nhà thầu thi công.
- Bộ phận chăm sóc khách hàng/bàn giao.

### 2. Current Manual Workflow

```text
Kỹ thuật viên kiểm tra từng khu vực
    ↓
Chụp ảnh lỗi
    ↓
Ghi chú hoặc ghi âm
    ↓
Cuối ca tổng hợp ảnh và ghi chú
    ↓
Nhập lại mô tả lỗi vào biểu mẫu
    ↓
Gắn vị trí/hạng mục/nhà thầu
    ↓
Điều phối viên rà soát và gửi xử lý
```

### 3. Bottleneck

- Bước tốn thời gian nhất: đối chiếu ảnh với ghi chú và nhập lại biên bản.
- **Baseline giả định:** 25–45 phút/căn có 10–20 lỗi.
- Lỗi phổ biến: ảnh không gắn đúng vị trí, mô tả không thống nhất, thiếu severity, trùng lỗi hoặc bỏ sót.

### 4. AI Intervention

- Speech-to-text chuyển ghi âm thành văn bản.
- Vision model mô tả ảnh và kiểm tra chất lượng ảnh.
- LLM chuẩn hóa thành cấu trúc:
  - phòng/khu vực;
  - hạng mục;
  - loại lỗi;
  - mô tả;
  - severity;
  - ảnh liên quan;
  - nhà thầu dự kiến.
- Rule kiểm tra trường bắt buộc và phát hiện trùng lặp.
- Kỹ thuật viên duyệt biên bản trước khi phát hành.

### 5. Success Metrics

- Giảm thời gian lập biên bản từ **35 phút xuống dưới 10 phút/căn**.
- Tỷ lệ lỗi có đủ ảnh + vị trí + mô tả + severity đạt **≥ 95%**.
- Giảm lỗi bị trả lại do thiếu thông tin ít nhất **50%**.
- Tỷ lệ ghép đúng ảnh với lỗi đạt **≥ 95%** trên bộ test đã gán nhãn.
- 100% biên bản được con người duyệt trước khi gửi nhà thầu.

### 6. Kiến trúc sơ bộ

**Khuyến nghị: LLM Feature + Vision + Rule.**

```text
Mobile App
 → Upload ảnh/voice
 → Speech-to-Text + Vision
 → LLM Structured Extraction
 → Taxonomy & Validation Rules
 → Draft Defect Report
 → Human Review
 → Work-order System
```

- Agent chưa cần thiết trong PoC.
- Có thể thêm Agent ở giai đoạn sau để theo dõi vòng đời sửa lỗi, nhưng không tự xác nhận hoàn thành.

---

# Quick Problem Card 3

## Tên bài toán

**AI kiểm tra tính đầy đủ và trích xuất dữ liệu hồ sơ khách hàng/giao dịch — Vinhomes**

### 1. Actor/Operator

- Nhân viên kinh doanh.
- Nhân viên vận hành hồ sơ.
- Bộ phận kiểm soát/chăm sóc khách hàng.
- Khách hàng cung cấp giấy tờ.

### 2. Current Manual Workflow

```text
Nhận bộ hồ sơ
    ↓
Mở từng tài liệu
    ↓
Xác định loại giấy tờ
    ↓
Đọc và nhập trường dữ liệu
    ↓
Đối chiếu checklist
    ↓
Phát hiện thiếu/sai/không khớp
    ↓
Liên hệ bổ sung
    ↓
Chuyển bộ phận kiểm soát
```

### 3. Bottleneck

- Bước tốn thời gian nhất: đọc, nhập và đối chiếu nhiều tài liệu.
- **Baseline giả định:** 20–40 phút/bộ hồ sơ.
- Lỗi phổ biến: nhập sai ký tự, thiếu trang, thông tin không khớp, phát hiện thiếu giấy tờ muộn.

### 4. AI Intervention

- OCR/Document AI nhận dạng loại tài liệu và trích xuất trường.
- Rule kiểm tra trường bắt buộc, định dạng, ngày hiệu lực và đối chiếu chéo.
- LLM chỉ dùng để giải thích lỗi bằng ngôn ngữ dễ hiểu hoặc xử lý bố cục khó; không tự phê duyệt hồ sơ.
- Nhân viên duyệt các trường confidence thấp và toàn bộ ngoại lệ.

### 5. Success Metrics

- Giảm thời gian kiểm tra ban đầu từ **30 phút xuống dưới 8 phút/bộ**.
- Field-level accuracy trên trường trọng yếu đạt **≥ 98%**.
- Recall phát hiện thiếu tài liệu đạt **≥ 99%**.
- Giảm hồ sơ bị trả lại ở bước kiểm soát ít nhất **40%**.
- 0 hồ sơ được tự động phê duyệt chỉ dựa trên AI.
- 100% truy cập tài liệu và thay đổi dữ liệu có audit log.

### 6. Kiến trúc sơ bộ

**Khuyến nghị: Document AI + Rule; LLM là thành phần hỗ trợ, không phải trung tâm.**

```text
Secure Upload
 → Malware Scan
 → OCR/Document Classification
 → Field Extraction
 → Cross-document Rules
 → Confidence Scoring
 → Human Verification
 → Core System
```

---

# Quyết định cá nhân trước thảo luận nhóm

## Bài toán đề xuất ưu tiên

**AI tiếp nhận, phân loại và định tuyến yêu cầu dịch vụ cư dân.**

## Lý do

1. Actor và workflow rõ.
2. Tần suất cao, dễ đo baseline.
3. Có thể triển khai incremental:
   - Rule-only baseline;
   - LLM extraction;
   - gợi ý routing;
   - automation có kiểm soát.
4. Không cần AI tự đưa ra quyết định pháp lý hoặc phê duyệt giao dịch.
5. Có thể dùng dữ liệu ticket lịch sử để tạo bộ test offline.
6. Tác động trực tiếp tới thời gian phản hồi và trải nghiệm cư dân.

## Giả định cần xác minh với nhóm/Operator

- Kênh tiếp nhận nào chiếm phần lớn sản lượng.
- Số ticket trung bình/ngày và phân bố category.
- Taxonomy hiện tại có ổn định hay không.
- Baseline thời gian phân loại, tỷ lệ chuyển sai và SLA.
- Dữ liệu có ảnh, voice hay chỉ text.
- Hệ thống ticket có API/sandbox tích hợp không.
- Nhóm sự cố nào bắt buộc con người xử lý ngay.
