Dưới đây là bài tự luận chiêm nghiệm được viết dựa trên toàn bộ quá trình thực hành, xử lý lỗi và xây dựng hệ thống trong buổi Lab vừa qua.

Nhật ký chiêm nghiệm: Trải nghiệm sử dụng AI làm "Thought-Partner" trong dự án Vin Smart Future
Trong suốt buổi thực hành đóng vai trò là một AI Product Engineer cho Vin Smart Future, tôi đã sử dụng AI (cụ thể là Gemini) không chỉ như một công cụ tìm kiếm, mà thực sự là một người đồng hành (thought-partner) để giải quyết từ các vấn đề chiến lược đến những lỗi kỹ thuật hóc búa nhất. Dưới đây là những đúc kết của tôi về quá trình tương tác này.

1. AI đã giúp tôi những gì?
AI đã đóng vai trò rất lớn trong hai giai đoạn cốt lõi của buổi học:

Gỡ lỗi (Debugging) môi trường và SDK: Khi tôi gặp lỗi 400 Bad Request dù terminal báo API Key "OK", AI đã ngay lập tức chỉ ra một "cạm bẫy" rất đặc thù của Windows CMD: việc sử dụng dấu ngoặc kép "" trong lệnh set khiến chuỗi key bị sai lệch. Sau đó, khi tôi tiếp tục gặp lỗi 404 Model Not Found, AI đã phân tích được rào cản do việc sử dụng sai tên model tương lai (gemini-2.5-flash) và hướng dẫn tôi chuyển về bản 1.5-flash để code chạy mượt mà.

Lên ý tưởng và định dạng cấu trúc (Brainstorming & Formatting): AI giúp tôi hệ thống hóa các ý tưởng rời rạc thành một "Bảng quét cơ hội (SCAN)" chuyên nghiệp và các "Problem Cards" chi tiết cho hệ sinh thái Vingroup (Vinmec, Vinhomes, Xanh SM). Việc AI hỗ trợ xuất thẳng ra mã Markdown giúp tôi tiết kiệm rất nhiều thời gian trình bày tài liệu.

2. AI đã sai ở đâu (Hallucination & Lỗi Logic)?
Dù rất thông minh, AI vẫn bộc lộ những điểm yếu chí mạng nếu người dùng nhắm mắt làm theo mà không kiểm chứng:

Lỗi "Bare Except" trong Python: Khi tôi nhờ AI xây dựng hàm xử lý chatbot CLI, AI đã đề xuất cấu trúc except: chung chung để bắt lỗi. Điều này vô tình chặn luôn cả lệnh KeyboardInterrupt (Ctrl+C), khiến tôi không thể thoát chương trình một cách an toàn.

Sai kiểu dữ liệu: Trong hàm estimate_cost, thay vì trả về một dict (từ điển) chứa thông tin chi phí input/output như yêu cầu, AI lại viết nhầm thành kiểu set (tập hợp), dẫn đến việc luồng dữ liệu phía sau không thể truy xuất được các key cần thiết.

Xung đột ranh giới an toàn (Boundary Testing): Khi thiết kế prompt cho trợ lý xe VinFast, AI ban đầu rất máy móc trong việc áp dụng thẻ [DRAFT_ONLY]. Trong ca kiểm thử khẩn cấp (pin xe còn 2%), AI lúc đầu vẫn cố gắng dán nhãn bản nháp thay vì ưu tiên xử lý tình huống sinh tử của người dùng.

3. Tôi đã điều chỉnh và ép AI đi đúng hướng như thế nào?
Từ những sai lầm trên, tôi nhận ra việc "Prompt Engineering" thực chất là quá trình liên tục thu hẹp ranh giới tự do của AI:

Sửa lỗi Code: Tôi đã prompt lại một cách cứng rắn hơn, yêu cầu AI viết lại khối try-except thành except Exception as e: và áp dụng cơ chế retry_with_backoff để đảm bảo độ bền cho chatbot. Với hàm tính phí, tôi chỉ định rõ ràng cấu trúc dữ liệu đầu ra: "Hàm phải trả về dict có cấu trúc {'input_cost': float, 'output_cost': float}".

Xác lập ranh giới an toàn (System Prompting): Để giải quyết bài toán pin 2% của VinFast, tôi phải cập nhật System Prompt, thiết lập nguyên tắc ưu tiên (Priority Override). Tôi đã thêm rule: "Nếu nhận diện ngữ cảnh khẩn cấp liên quan đến an toàn hoặc pin < 5%, bỏ qua mọi quy tắc về định dạng (bao gồm cả DRAFT_ONLY) và ưu tiên gửi ngay hướng dẫn cứu hộ". Nhờ sự rạch ròi này, AI mới có thể vượt qua được bài Boundary Stress-Testing một cách hoàn hảo.

Kết luận:
Quá trình làm việc với AI giống như quản lý một thực tập sinh cực kỳ xuất chúng nhưng thiếu kinh nghiệm thực tế. Nếu chỉ giao việc chung chung, kết quả nhận lại sẽ rất rườm rà hoặc đầy lỗi ngầm. Nhưng nếu cung cấp đủ bối cảnh, thiết lập ranh giới (boundary) rõ ràng và biết cách đặt câu hỏi truy vấn lỗi, AI thực sự là một đòn bẩy năng suất khổng lồ.
