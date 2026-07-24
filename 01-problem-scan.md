# 01 — Problem Scan (Cá nhân) — Vin Smart Future

> **Thành viên thực hiện:** [Điền họ tên + MSSV của bạn]

---

# 🔍 Phase 1 — SCAN

Quét qua hoạt động vận hành của các công ty thành viên Vingroup bằng 4 Lenses (Lặp lại / Tốn thời gian / AI có thể tốt hơn / Pain từ người khác).

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công báo cáo pin yếu/hết pin của tài xế: tra cứu GPS, tìm trạm sạc trống, soạn tin hướng dẫn — mất 15-20 phút/lượt. |
| 2 | **VinFast** | AI có thể tốt hơn | Trợ lý hướng dẫn trạm sạc hiện chưa tự động lọc theo loại cổng sạc (CCS2/GBT) phù hợp với từng dòng xe (VF5/VF8/VF9), khách phải tự tra cứu. |
| 3 | **Vinhomes** | Lặp lại | Phân loại và điều hướng thủ công các phản ánh cư dân (mất nước, hỏng đèn, ồn ào...) gửi qua App Vinhomes Resident đến đúng ban quản lý toà nhà. |
| 4 | **Vinmec** | Tốn thời gian | Bác sĩ mất 20-30 phút/bệnh nhân để soạn thảo tóm tắt hồ sơ xuất viện bằng ngôn ngữ dễ hiểu từ dữ liệu bệnh án điện tử. |
| 5 | **Vinpearl** | Pain từ người khác | Quản lý khách sạn phải tự đọc thủ công hàng trăm review trên Booking.com/Agoda/Google Map mỗi tuần để phát hiện phàn nàn khẩn cấp. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Top 3 bài toán được chọn từ danh sách SCAN: **#1 (Xanh SM pin yếu), #2 (VinFast trạm sạc), #3 (Vinhomes phản ánh cư dân).**

## Quick Problem Card #1

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo pin yếu cần điều phối viên     │
│ hướng dẫn trạm sạc gần nhất hoặc điều xe cứu hộ.            │
│ Công ty thành viên: [x] Xanh SM                             │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (mất cuốc, chờ đợi),            │
│ Điều phối viên (quá tải giờ cao điểm)                       │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Gọi hotline báo sự cố ──> 2. Tổng đài mở phiếu         │
│   ──> 3. Điều phối tra GPS xe ──> 4. Tra trạm sạc trống     │
│   ──> 5. Soạn & gửi tin hướng dẫn                           │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 4-5 (⏱ 11 phút/lượt) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 4-5              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian xử lý sự cố từ 17 phút ──> dưới 4 phút.      │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```

## Quick Problem Card #2

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Khách hàng VinFast không biết trạm sạc nào tương  │
│ thích với loại cổng sạc của xe mình, phải tự tra cứu thủ    │
│ công qua nhiều app/website khác nhau.                       │
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau (Actor)? Chủ xe VinFast (VF5/VF8/VF9)           │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Mở app tra trạm sạc gần đây ──> 2. Kiểm tra thủ công   │
│   loại cổng sạc từng trạm ──> 3. Gọi hotline xác nhận nếu   │
│   không chắc ──> 4. Tự lái đến, có thể trạm không phù hợp   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ 8 phút/lượt)     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ 95% gợi ý trạm sạc đúng loại cổng cho đúng dòng xe.         │
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```

## Quick Problem Card #3

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Ban quản lý Vinhomes phân loại và điều hướng thủ  │
│ công phản ánh cư dân đến đúng bộ phận xử lý.                │
│ Công ty thành viên: [x] Vinhomes                             │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên trực App Resident, cư dân    │
│ (chờ phản hồi lâu)                                          │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh trên App ──> 2. Nhân viên đọc &    │
│   phân loại thủ công ──> 3. Chuyển tiếp email/ticket đến    │
│   đúng ban quản lý ──> 4. Theo dõi & đóng ticket             │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ 6 phút/lượt,     │
│ tỉ lệ phân loại sai ~15%)                                   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian phân loại từ 6 phút ──> dưới 30 giây,        │
│ độ chính xác phân loại ≥ 90%.                                │
│                                                             │
│ Quick Architecture: [x] Rule + LLM Feature                  │
└─────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn của nhóm

Nhóm thống nhất chọn **Card #1 — Xanh SM: Điều phối hỗ trợ pin yếu** để thực hiện Deep-Dive tại file [02-deep-dive-report.md](02-deep-dive-report.md), vì đây là tác vụ vận hành thời gian thực (real-time), ảnh hưởng trực tiếp đến an toàn giao thông và trải nghiệm tài xế, đồng thời đã có sẵn bản mẫu kỹ thuật (`prompt_prototype.py`) để kiểm chứng ranh giới an toàn.
