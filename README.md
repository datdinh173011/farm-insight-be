# Farm Insight API (Django REST)

Backend skeleton for đăng nhập và quản lý các form khảo sát dựa trên các phiếu phỏng vấn PDF.

## Thiết lập nhanh

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
# Tạo user admin (tùy chọn)
python manage.py createsuperuser
# Nạp sẵn các mẫu form lấy từ PDF
python manage.py seed_form_templates
python manage.py runserver
```

## API chính
- `POST /api/auth/register/` – đăng ký người dùng (username/password).
- `POST /api/auth/token/` – lấy JWT (SimpleJWT).
- `POST /api/auth/token/refresh/` – refresh JWT.
- `GET /api/forms/templates/` – danh sách template (cấu trúc form + siêu dữ liệu PDF).
- `GET /api/forms/templates/{template_type}/` – chi tiết template (lookup theo `template_type`).
- `POST /api/forms/submissions/` – tạo câu trả lời cho template (truyền `template_type`, các trường thông tin hộ gia đình, `data` là JSON câu trả lời).
- `GET /api/forms/submissions/` – danh sách bài làm của chính người dùng (admin xem được tất cả, hỗ trợ filter `?template_type=`).

Mặc định tất cả endpoint (trừ register/token) yêu cầu header `Authorization: Bearer <access_token>`.

## Cấu trúc form
- Models: `FormTemplate` (metadata + `schema` JSON), `FormSubmission` (liên kết template, user, dữ liệu câu trả lời).
- Seeder `seed_form_templates` lấy schema tóm tắt từ các PDF gốc trong thư mục `form_pdf/`.
- Schema dạng JSON hỗ trợ các section, field đơn (text/number/select/multi_select) và bảng (`type: "table"` với cột/`preset_rows`), thuận tiện cho frontend dựng form động.
- `FormSubmission` lưu thêm các trường chung: `ho_ten`, `nam_sinh`, `so_dien_thoai`, `thon`, `xa`, `tinh`, `template_type` + `data` (phần chi tiết theo từng mẫu PDF).

## Lưu ý
- Database mặc định SQLite, có thể đổi qua biến môi trường `DB_ENGINE/DB_NAME/DB_USER/DB_PASSWORD/DB_HOST/DB_PORT`.
- `TIME_ZONE` mặc định `Asia/Ho_Chi_Minh`.
- Repo chưa cài đặt sẵn dependency; hãy cài `requirements.txt` trước khi migrate/chạy.
