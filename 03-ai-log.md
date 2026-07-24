# 03 — AI Log & Reflection (Cá nhân)

> **Thành viên viết log:** [Điền họ tên + MSSV của bạn]

---

## 1. AI giúp gì?

Trong buổi lab, tôi dùng Claude làm thought-partner cho nhiều bước:
- **Brainstorm bài toán:** Dùng danh sách gợi ý trong `03-inspiration-kit.md` để chọn nhanh 5 bài toán thuộc các mảng Xanh SM/VinFast/Vinhomes/Vinmec/Vinpearl cho Phase 1 SCAN, thay vì phải tự nghĩ từ đầu.
- **Soạn và phản biện System Prompt:** Nhờ AI đánh giá bản nháp `SYSTEM_PROMPT` (vai trò dispatcher, ranh giới `[DRAFT_ONLY]`, ngưỡng pin 5%) xem có đủ chặt so với yêu cầu đề bài không.
- **Debug code Python:** Khi chạy `prompt_prototype.py` bị lỗi `404 model gemini-2.5-flash is no longer available`, AI xác định đúng nguyên nhân là model ID đã bị deprecate và sửa sang `gemini-flash-latest`.
- **Soạn thảo báo cáo:** Hỗ trợ dựng khung `01-problem-scan.md` và `02-deep-dive-report.md` theo đúng cấu trúc rubric yêu cầu trong README.

## 2. AI sai gì?

Khi tôi nhờ AI đánh giá bản nháp system prompt ban đầu, AI phát hiện ra **một lỗi logic thật sự** chứ không phải AI tự sai: Rule 2 của bản nháp ghi "không được gợi ý trạm sạc xa hơn 5km" nhưng phần hành động lại luôn luôn từ chối định tuyến và gọi xe cứu hộ bất kể khoảng cách trạm — tức là điều kiện "farther than 5km" được nêu ra nhưng không thực sự được dùng để rẽ nhánh. Đây là điểm mà nếu không kiểm tra kỹ, lời gợi ý an toàn của AI có thể trông "có vẻ đúng" (đưa ra JSON đúng định dạng) nhưng không khớp chính xác với ý đồ ban đầu của đề bài.

Ngoài ra, ở lần chạy thử đầu tiên, code gốc dùng model `gemini-2.5-flash` — đây là một giả định "model name còn hợp lệ" không được kiểm chứng trước, dẫn đến lỗi 404 khi chạy thật.

## 3. Sửa đổi ra sao?

- Bổ sung rõ nhánh rẽ theo khoảng cách vào Rule 2: nếu pin <5% **và** trạm gần nhất ≤5km thì vẫn có thể draft hướng dẫn định tuyến; chỉ khi trạm >5km (hoặc không rõ khoảng cách) mới bắt buộc từ chối và gọi xe cứu hộ.
- Đổi `GEMINI_MODEL` từ `gemini-2.5-flash` sang `gemini-flash-latest` để khớp với model còn được hỗ trợ, và chạy lại script để xác nhận không còn lỗi 404.
- Khi viết Operational Boundary trong `02-deep-dive-report.md`, tôi diễn đạt lại điều kiện an toàn theo đúng logic đã sửa (không chỉ copy nguyên văn bản nháp ban đầu) để đảm bảo văn bản báo cáo khớp với hành vi thực tế của code.
