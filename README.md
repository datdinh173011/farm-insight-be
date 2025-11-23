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
- `POST /api/forms/submissions/` – tạo câu trả lời cho template (truyền `template_type`, các trường thông tin hộ gia đình, `data` là JSON câu trả lời). Endpoint này mở, không cần đăng nhập.
- `GET /api/forms/submissions/` – danh sách tất cả submissions (chỉ cần đăng nhập), hỗ trợ filter `?template_type=` và `?status=`; phân trang `?page=`, mặc định 20 bản ghi/trang.
- Auth: `POST /api/auth/register/`, `POST /api/auth/token/`, `POST /api/auth/token/refresh/`, `POST /api/auth/logout/` (blacklist refresh token, requires auth header + refresh token in body).

Mặc định tất cả endpoint (trừ register/token) yêu cầu header `Authorization: Bearer <access_token>`.

## Cấu trúc form
- Models: `FormTemplate` (metadata + `schema` JSON), `FormSubmission` (liên kết template, user, dữ liệu câu trả lời).
- Seeder `seed_form_templates` lấy schema tóm tắt từ các PDF gốc trong thư mục `form_pdf/`.
- Schema dạng JSON hỗ trợ các section, field đơn (text/number/select/multi_select) và bảng (`type: "table"` với cột/`preset_rows`), thuận tiện cho frontend dựng form động.
- `FormSubmission` lưu thêm các trường chung: `ho_ten`, `nam_sinh`, `so_dien_thoai`, `thon`, `xa`, `tinh`, `template_type` + `data` (phần chi tiết theo từng mẫu PDF).

## Ví dụ POST `/api/forms/submissions/`
Payload mẫu cho form `nuoi-sau-canxi`:

```json
{
  "template_type": "nuoi-sau-canxi",
  "ho_ten": "Nguyen Van A",
  "nam_sinh": 1985,
  "so_dien_thoai": "0909123456",
  "thon": "Thon 1",
  "xa": "Xa ABC",
  "tinh": "Tinh XYZ",
  "data": {
    "vat_nuoi_an_sau": [
      { "ten_loai": "Ga", "so_con": 50, "so_lua_duoc_cho_an": 3 }
    ],
    "cay_trong_bon_phan_sau": [
      { "ten_cay_trong": "Lua", "so_vu": 2, "dien_tich": 3 }
    ],
    "thuc_an_sau": [
      {
        "loai_phu_pham": "Cam gao",
        "khoi_luong_ngay": 5,
        "so_luong_vat_nuoi_thai": 10,
        "so_ngay_lua": 45,
        "so_lua": 1,
        "tong_khoi_luong": 200,
        "phu_pham_dung_cho_sau": 150,
        "ty_le_su_dung": 75,
        "dien_tich_nuoi": 12,
        "chi_phi_giong": 50000,
        "so_ngay_thu_hoach": 45,
        "khoi_luong_sau": 20,
        "khoi_luong_phan": 8,
        "cong_lao_dong": 2
      }
    ],
    "bon_phan_sau": [
      {
        "ten_cay_trong": "Lua",
        "thoi_gian_trong": "06/2024",
        "dien_tich": 3,
        "phan_su_dung": "Phan sau canxi",
        "chi_phi_phan": 100000,
        "so_lan_phun_thuoc": 1,
        "chi_phi_thuoc": 30000,
        "chi_phi_cong": 20000,
        "sau_benh": "Không",
        "nang_suat": 450,
        "gia_ban": 8000,
        "thanh_tien": 3600000
      }
    ]
  },
  "status": "submitted"
}
```

Payload mẫu cho form `nhom-cau-hoi-chung` (gộp thông tin 4 trang):

```json
{
  "template_type": "nhom-cau-hoi-chung",
  "ho_ten": "Tran Thi B",
  "nam_sinh": 1990,
  "so_dien_thoai": "0911222333",
  "thon": "Thon 2",
  "xa": "Xa DEF",
  "tinh": "Tinh UVW",
  "data": {
    "xu_ly_phu_pham": [
      { "phuong_phap": "Dot", "truoc_tham_gia": 80, "sau_tham_gia": 20 }
    ],
    "xu_ly_goc_ra": [
      { "phuong_phap": "Chon dat", "truoc_tham_gia": 60, "sau_tham_gia": 10 }
    ],
    "xu_ly_phan_chan_nuoi": [
      { "phuong_phap": "U phan", "truoc_tham_gia": 50, "sau_tham_gia": 70 }
    ],
    "danh_gia_ky_thuat": [
      {
        "ten_ky_thuat": "Len men phu pham",
        "do_kho": 5,
        "loi_nhuan": 4,
        "giam_chi_phi": 4,
        "giam_cong_viec": 3,
        "tot_cho_moi_truong": 5,
        "cai_thien_dat": 4
      }
    ],
    "hoat_dong_truyen_thong": [
      { "hoat_dong": "Lop tap huan TOT", "da_nghe": "Đúng", "da_tham_du": "KHÔNG", "anh_huong": 3 }
    ]
  },
  "status": "submitted"
}
```

## Lưu ý
- Database mặc định SQLite, có thể đổi qua biến môi trường `DB_ENGINE/DB_NAME/DB_USER/DB_PASSWORD/DB_HOST/DB_PORT`.
- `TIME_ZONE` mặc định `Asia/Ho_Chi_Minh`.
- Repo chưa cài đặt sẵn dependency; hãy cài `requirements.txt` trước khi migrate/chạy.
