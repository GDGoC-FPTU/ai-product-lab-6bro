# Lab 02 — Nhật ký Chiêm nghiệm Tương tác với AI (AI Log & Reflection)

Tài liệu này ghi lại một cách trung thực quá trình tôi tương tác và sử dụng AI (ở đây là trợ lý AI coding) làm người bạn đồng hành (Thought-partner) trong suốt buổi Lab 02.

---

## 💡 1. Trợ lý AI đã giúp gì cho tôi?

AI đã đóng vai trò hỗ trợ rất đắc lực ở nhiều giai đoạn khác nhau của bài Lab:
* **Brainstorm ý tưởng quy trình:** Hỗ trợ tôi áp dụng 4 Thấu kính (Lenses) để nhanh chóng phát hiện các bài toán thực tế trong vận hành của 5 công ty con Vingroup (Vinhomes, Vinmec, Xanh SM, VinFast, Vinpearl) và hoàn thành bảng SCAN nhanh chóng.
* **Xây dựng System Prompt:** AI đã dịch chuyển các yêu cầu bài toán trong slide thành các chỉ thị rõ ràng và chặt chẽ bằng tiếng Anh cho mô hình Gemini, phân chia rạch ròi giữa [RULE 1] (gắn tag `[DRAFT_ONLY]`) và [RULE 2] (giới hạn pin xe điện < 5%).
* **Lập trình và Xử lý SDK:** AI giúp tối ưu hóa hàm `evaluate_prompt` để hỗ trợ song song cả SDK mới (`google-genai`) lẫn SDK cũ (`google-generativeai`) để tránh việc code bị lỗi khi môi trường chưa update phiên bản thư viện mới nhất.
* **Xử lý lỗi hệ thống:** Hỗ trợ debug lỗi mã hóa hiển thị `UnicodeEncodeError` (do Windows Terminal mặc định dùng mã hóa `cp1252` không in được các emoji như 🚀 hay ✅) bằng giải pháp thiết lập biến môi trường `$env:PYTHONIOENCODING='utf-8'`.

---

## ⚠️ 2. AI đã đưa ra những câu trả lời sai lệch (Hallucination) hoặc lỗi gì?

Trong quá trình đồng hành, AI cũng đã gặp một số điểm chưa tối ưu và lỗi logic:
1. **Ranh giới Prompt chưa đủ chặt chẽ (Weak Safety Boundary):** 
   * Ban đầu, khi thiết lập ranh giới cho `RULE 2`, AI chỉ yêu cầu mô hình từ chối trạm sạc xa và đề xuất cứu hộ bằng văn bản tự nhiên.
   * Lỗi này dẫn đến việc mô hình Gemini thỉnh thoảng phản hồi bằng câu thoại tự do (ví dụ: *"Tôi đề xuất bạn nên gọi xe cứu hộ..."*), điều này làm thất bại bộ test tự động (Assertion Checks) vốn yêu cầu từ khóa có cấu trúc dạng JSON `dispatch_mobile_charger`.
2. **Lỗi thực thi lệnh trên Windows:** 
   * Khi đề xuất lệnh kiểm thử, AI trực tiếp gọi lệnh chạy thông thường mà không tính đến việc PowerShell trên hệ điều hành Windows sẽ crash khi gặp ký tự emoji trong log in ra màn hình.

---

## 🛠️ 3. Tôi đã điều chỉnh và khắc phục ra sao?

Để khắc phục các hạn chế trên và ép AI đưa ra câu trả lời chính xác, tôi đã thực hiện:
* **Định hình lại chỉ thị định dạng:** Tôi đã bổ sung quy định nghiêm ngặt vào `SYSTEM_PROMPT` ở [RULE 2], yêu cầu mô hình: *"Thay vào đó, lập tức kích hoạt điều xe sạc di động bằng cách xuất ra một đối tượng JSON: `{"action": "dispatch_mobile_charger", "reason": "<giải thích>"}`"*. Điều này đảm bảo đầu ra luôn nhất quán và vượt qua kiểm thử tự động thành công.
* **Sửa lỗi môi trường mã hóa:** Thay vì chạy lệnh trực tiếp, tôi yêu cầu chạy kèm thiết lập mã hóa đầu ra: 
  ```powershell
  $env:PYTHONIOENCODING='utf-8'; .\venv\Scripts\python.exe starter-code/prompt_prototype.py
  ```
  Nhờ đó, toàn bộ tiến trình stress-test đã hiển thị chính xác các biểu tượng xác thực mà không bị crash.
