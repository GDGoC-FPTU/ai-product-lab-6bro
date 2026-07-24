# 02 — Deep-Dive Report (Nhóm) — Vin Smart Future

> **Tên nhóm:** [Điền tên nhóm]
>
> **Thành viên:**
> | Họ và tên | MSSV |
> |---|---|
> | [Điền họ tên] | [Điền MSSV] |
> | [Điền họ tên] | [Điền MSSV] |
> | [Điền họ tên] | [Điền MSSV] |

---

## Bài toán được chọn để Deep-Dive
**Card #1 — Xanh SM: Điều phối hỗ trợ tài xế báo pin yếu / hết pin thực địa.**

Khi tài xế Xanh SM (GSM) báo pin yếu qua hotline, điều phối viên tại Trung tâm Điều vận phải tự tay tra cứu vị trí xe, tìm trạm sạc VinFast còn trụ trống phù hợp, và soạn tin nhắn hướng dẫn — hoàn toàn thủ công, tốn thời gian và dễ sai sót khi lưu lượng cuộc gọi tăng vào giờ cao điểm.

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping

Xem sơ đồ trực quan đầy đủ tại [04-workflow-diagram.png](04-workflow-diagram.png) (được vẽ bằng script [extras/generate_workflow_diagram.py](extras/generate_workflow_diagram.py)).

Tóm tắt các bước:

| # | Bước | Ai thực hiện | Thời gian | Ghi chú |
|---|---|---|---|---|
| 1 | Tài xế gọi hotline báo pin yếu | Tài xế → Tổng đài | 1 phút | 🔄 Handoff |
| 2 | Tổng đài xác nhận thông tin xe, mở phiếu sự cố | Tổng đài viên | 2 phút | |
| 3 | Điều phối viên tra cứu vị trí GPS xe trên bản đồ nội bộ | Điều phối viên | 3 phút | 🔄 Handoff (Tổng đài → Điều phối) |
| 4 | Tra cứu thủ công trạm sạc VinFast gần đó còn trụ trống, đúng loại cổng sạc | Điều phối viên | 6 phút | 🔴 Bottleneck |
| 5 | Soạn tin nhắn hướng dẫn/điều xe cứu hộ, gửi qua App tài xế | Điều phối viên | 5 phút | 🔴 Bottleneck |

**Tổng cộng = 17 phút/lượt.**

## 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) thuộc Trung tâm Điều vận Xanh SM. |
| **2. Current Workflow** | Nhận cuộc gọi báo pin yếu từ tài xế, tra cứu vị trí GPS trên bản đồ nội bộ, tra cứu thủ công trạm sạc VinFast còn trống và đúng loại cổng sạc, soạn và gửi tin nhắn hướng dẫn qua App tài xế. Toàn bộ thủ công, mất 17 phút/lượt. |
| **3. Bottleneck** | Bước 4 & 5 (11 phút): tra cứu trạm sạc phù hợp với dòng xe và soạn thảo hướng dẫn đường đi rõ ràng bằng tiếng Việt. |
| **4. Business Impact** | Ước tính ~60-80 sự cố pin/ngày tại mỗi thành phố lớn. Gây lãng phí hàng chục giờ công điều phối/ngày, kéo dài thời gian chờ của tài xế, tăng rủi ro xe cạn pin giữa đường gây ùn tắc, và giảm số cuốc xe thực hiện được. |
| **5. Success Metric** | 1. Giảm thời gian xử lý sự cố từ 17 phút xuống dưới 4 phút. <br>2. Tỉ lệ gợi ý đúng trạm sạc/đúng loại cổng đạt ≥ 95%. |
| **6. Operational Boundary** | AI được phép: truy xuất vị trí GPS xe, tra cứu API trạm sạc trống, soạn thảo tin nhắn hướng dẫn ở dạng **nháp** (`[DRAFT_ONLY]`). **TUYỆT ĐỐI CẤM:** tự động gửi tin nhắn khi chưa có điều phối viên phê duyệt (bắt buộc Human-in-the-loop); đề xuất trạm sạc cách xe hơn 5km khi pin dưới ngưỡng nguy cấp 5% — trường hợp này phải từ chối định tuyến và kích hoạt điều xe cứu hộ pin di động. |

## 3.3. Future-State Flow & AI Fit

**AI Fit:** `LLM Feature` — quy trình có cấu trúc cố định (tra vị trí → tra trạm sạc → soạn tin), không cần vòng lặp tự trị (Agent), nhưng rủi ro sai sót (điều xe đến trạm không phù hợp khi pin nguy cấp) đủ cao nên **bắt buộc phải có bước con người phê duyệt**.

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ 🔵 AI: Auto- │     │ 🔵 AI: Draft │     │ 🟢 Human:    │
│ Nhận cuộc    │ ──→ │ pull GPS &   │ ──→ │ tin hướng dẫn│ ──→ │ Điều phối    │
│ gọi sự cố    │     │ trạm sạc trống│    │ [DRAFT_ONLY] │     │ duyệt & gửi  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu AI không chắc
                                                               chắn hoặc pin <5%
                                                               & trạm >5km, tự
                                                               động chuyển sang
                                                               dispatch_mobile_charger,
                                                               điều phối viên xử
                                                               lý thủ công như cũ.
```

---

# 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? — Có (log vị trí GPS, danh sách trạm sạc và log sự cố lịch sử của Xanh SM/VinFast).
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? — Có, nhờ tag `[DRAFT_ONLY]` bắt buộc duyệt và fallback `dispatch_mobile_charger` khi pin nguy cấp.
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? — Có, điều phối viên chỉ cần duyệt/gửi thay vì tự tra cứu và soạn thảo.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET**
[ ] **NO-GO**

**Justification:**
> Bài toán có phạm vi hẹp, rõ ràng, metric đo được cụ thể (17 phút → dưới 4 phút, độ chính xác ≥95%). Kiến trúc LLM Feature đơn giản, không cần Agent multi-step. Ranh giới an toàn (Operational Boundary) đã được kiểm chứng thực nghiệm qua bản mẫu kỹ thuật [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py): hệ thống giữ vững tag `[DRAFT_ONLY]` dưới áp lực người dùng và từ chối định tuyến trạm sạc xa khi pin dưới 5%, thay vào đó kích hoạt xe cứu hộ pin di động đúng như thiết kế. Chi phí triển khai thấp (một API call LLM/lượt sự cố), lợi ích vận hành (tiết kiệm ~13 phút/lượt × hàng chục lượt/ngày) vượt xa chi phí, và rủi ro được kiểm soát chặt bằng HITL bắt buộc.
