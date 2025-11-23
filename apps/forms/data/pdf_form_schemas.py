"""
Form templates derived from the provided PDF interview sheets.

Each schema is intentionally concise but keeps the structure (sections, tables,
and key questions) so the frontend can render dynamic forms that mirror the
original questionnaires.
"""

FORM_SCHEMAS = [
    {
        "slug": "len-men-phu-pham",
        "title": "Lên men phụ phẩm cây trồng làm thức ăn chăn nuôi",
        "source_pdf": "form_pdf/251106 Phiếu phỏng vấn (Lên men phụ phẩm cây trồng làm thức ăn chăn nuôi).pdf",
        "description": "Theo dõi hộ gia đình áp dụng kỹ thuật ủ lên men phụ phẩm cây trồng.",
        "schema": {
            "sections": [
                {
                    "title": "Thông tin hộ gia đình",
                    "fields": [
                        {"key": "ho_ten", "label": "Họ và tên người được phỏng vấn", "type": "text", "required": True},
                        {"key": "nam_sinh", "label": "Năm sinh", "type": "number"},
                        {"key": "so_dien_thoai", "label": "Số điện thoại liên hệ", "type": "text"},
                        {"key": "thon", "label": "Thôn", "type": "text"},
                        {"key": "xa", "label": "Xã", "type": "text"},
                        {"key": "tinh", "label": "Tỉnh", "type": "text"},
                    ],
                },
                {
                    "title": "A. Quản lý phụ phẩm sau khi ủ lên men",
                    "fields": [
                        {
                            "type": "table",
                            "key": "quan_ly_sau_ferment",
                            "label": "Từ trước đến nay và lứa lên men gần đây nhất",
                            "description": "Ghi 1 dòng cho từng loại phụ phẩm đã ủ lên men.",
                            "columns": [
                                {"key": "ten_phu_pham", "label": "Tên phụ phẩm cây trồng", "type": "text", "required": True},
                                {"key": "thoi_diem_ap_dung_dau", "label": "Tháng/năm áp dụng kỹ thuật lần đầu", "type": "text"},
                                {"key": "dien_tich_trong", "label": "Diện tích trồng (sào/vụ)", "type": "number"},
                                {"key": "so_lan_len_men", "label": "Tổng số lần đã tiến hành", "type": "number"},
                                {"key": "thoi_diem_gan_nhat", "label": "Thời điểm lứa lên men gần nhất (tháng/năm)", "type": "text"},
                                {"key": "dien_tich_thu_gom", "label": "Diện tích phụ phẩm thu gom (sào)", "type": "number"},
                                {"key": "khoi_luong_thu_gom", "label": "Khối lượng phụ phẩm thu gom (kg)", "type": "number"},
                                {"key": "khoi_luong_u", "label": "Khối lượng phụ phẩm dùng ủ (kg)", "type": "number"},
                                {"key": "co_may_bam", "label": "Sử dụng máy băm/cắt", "type": "select", "options": ["Có", "Không"]},
                                {"key": "nhien_lieu", "label": "Nhiên liệu đã dùng (dầu/điện)", "type": "text"},
                                {"key": "chi_phi_khac", "label": "Chi phí vật liệu/đầu vào khác (đồng)", "type": "number"},
                            ],
                        }
                    ],
                },
                {
                    "title": "B. Phụ phẩm trước khi áp dụng ủ lên men",
                    "fields": [
                        {
                            "type": "table",
                            "key": "quan_ly_truoc_khi_ferment",
                            "label": "Tình trạng phụ phẩm cây trồng trước khi áp dụng",
                            "columns": [
                                {"key": "loai_cay_trong", "label": "Loại cây trồng", "type": "text", "required": True},
                                {
                                    "key": "co_ap_dung",
                                    "label": "Có áp dụng kỹ thuật ủ lên men?",
                                    "type": "select",
                                    "options": ["Có", "Không"],
                                    "required": True,
                                },
                                {"key": "dien_tich", "label": "Diện tích (sào/vụ x số vụ/năm)", "type": "text"},
                                {"key": "loai_phu_pham", "label": "Loại phụ phẩm", "type": "text"},
                                {"key": "khoi_luong_phu_pham", "label": "KG phụ phẩm thu gom (kg/sào/vụ)", "type": "number"},
                                {"key": "khoi_luong_su_dung", "label": "KG phụ phẩm được dùng ủ (kg/sào/vụ)", "type": "number"},
                            ],
                        }
                    ],
                },
                {
                    "title": "C. Sử dụng thức ăn ủ lên men cho vật nuôi",
                    "fields": [
                        {
                            "type": "table",
                            "key": "chan_nuoi_so_sanh",
                            "label": "Lứa nuôi gần đây nhất và trước khi dùng thức ăn ủ",
                            "description": "So sánh chi phí, sức khỏe vật nuôi trước và sau khi dùng thức ăn ủ lên men.",
                            "columns": [
                                {"key": "ten_vat_nuoi", "label": "Tên vật nuôi", "type": "text", "required": True},
                                {"key": "tong_so_lua", "label": "Số lứa đã nuôi bằng thức ăn ủ", "type": "number"},
                                {"key": "thuc_an_sau", "label": "Các loại thức ăn (SAU khi dùng thức ăn ủ)", "type": "text"},
                                {"key": "chi_phi_sau", "label": "Số tiền mua thức ăn/lứa (sau)", "type": "number"},
                                {"key": "suc_khoe_sau", "label": "Đánh giá sức khỏe (1-10) sau khi dùng", "type": "number"},
                                {"key": "thoi_gian_xuat_sau", "label": "Thời gian & trọng lượng xuất chuồng (sau)", "type": "text"},
                                {"key": "thuc_an_truoc", "label": "Các loại thức ăn (TRƯỚC khi dùng thức ăn ủ)", "type": "text"},
                                {"key": "chi_phi_truoc", "label": "Số tiền mua thức ăn/lứa (trước)", "type": "number"},
                                {"key": "suc_khoe_truoc", "label": "Đánh giá sức khỏe (1-10) trước khi dùng", "type": "number"},
                                {"key": "thoi_gian_xuat_truoc", "label": "Thời gian & trọng lượng xuất chuồng (trước)", "type": "text"},
                            ],
                        }
                    ],
                },
            ]
        },
    },
    {
        "slug": "nhom-cau-hoi-chung",
        "title": "Nhóm câu hỏi chung (sau câu 37)",
        "source_pdf": "form_pdf/251106 Phiếu phỏng vấn (Nhóm câu hỏi chung, sau câu 37).pdf",
        "description": "Các câu hỏi chung về xử lý phụ phẩm, tập huấn và mức độ chấp thuận kỹ thuật.",
        "schema": {
            "sections": [
                {
                    "title": "Xử lý phụ phẩm cây trồng",
                    "fields": [
                        {
                            "type": "table",
                            "key": "xu_ly_phu_pham",
                            "label": "Cách xử lý phụ phẩm trước/sau tham gia mô hình (tổng 100%)",
                            "columns": [
                                {"key": "phuong_phap", "label": "Phương pháp", "type": "text", "required": True},
                                {"key": "truoc_tham_gia", "label": "Trước khi tham gia (%)", "type": "number"},
                                {"key": "sau_tham_gia", "label": "Sau khi tham gia (%)", "type": "number"},
                            ],
                            "preset_rows": [
                                "Vứt bỏ trong vườn/cánh đồng",
                                "Đốt",
                                "Đưa đến bãi tập kết/chôn lấp",
                                "Chôn lấp tại chỗ",
                                "Bán hoặc cho người khác",
                                "Ủ phân hữu cơ tại ruộng",
                                "Lên men phụ phẩm làm thức ăn chăn nuôi",
                                "Làm thức ăn cho sâu canxi/trùn quế",
                                "Làm lớp lót nuôi gà đệm lót sinh học",
                                "Khác",
                            ],
                        },
                        {
                            "type": "table",
                            "key": "xu_ly_goc_ra",
                            "label": "Xử lý gốc rạ trước/sau tham gia mô hình",
                            "columns": [
                                {"key": "phuong_phap", "label": "Phương pháp", "type": "text", "required": True},
                                {"key": "truoc_tham_gia", "label": "Trước khi tham gia (%)", "type": "number"},
                                {"key": "sau_tham_gia", "label": "Sau khi tham gia (%)", "type": "number"},
                            ],
                            "preset_rows": ["Đốt", "Vùi trong nước", "Chôn xuống đất", "Sử dụng chế phẩm sinh học", "Khác"],
                        },
                        {"key": "co_chan_nuoi", "label": "Gia đình có nuôi động vật?", "type": "select", "options": ["Có", "Không"]},
                        {
                            "type": "table",
                            "key": "xu_ly_phan_chan_nuoi",
                            "label": "Xử lý phân gia súc trước/sau tham gia mô hình",
                            "columns": [
                                {"key": "phuong_phap", "label": "Phương pháp", "type": "text", "required": True},
                                {"key": "truoc_tham_gia", "label": "Trước khi tham gia (%)", "type": "number"},
                                {"key": "sau_tham_gia", "label": "Sau khi tham gia (%)", "type": "number"},
                            ],
                            "preset_rows": [
                                "Ủ phân",
                                "Xả nước ra khu vực xung quanh",
                                "Chôn xuống đất",
                                "Bán cho người khác",
                                "Hố tự hoại/Biogas",
                                "Làm thức ăn sâu canxi",
                                "Làm thức ăn trùn quế",
                                "Khác",
                            ],
                        },
                    ],
                },
                {
                    "title": "Cảm nhận về kỹ thuật",
                    "fields": [
                        {
                            "type": "table",
                            "key": "danh_gia_ky_thuat",
                            "label": "Đánh giá độ khó và lợi ích (1=thấp, 6= cao/không biết)",
                            "columns": [
                                {"key": "ten_ky_thuat", "label": "Kỹ thuật", "type": "text", "required": True},
                                {"key": "do_kho", "label": "Dễ/khó (1-10)", "type": "number"},
                                {"key": "loi_nhuan", "label": "Tăng lợi nhuận", "type": "number"},
                                {"key": "giam_chi_phi", "label": "Giảm chi phí", "type": "number"},
                                {"key": "giam_cong_viec", "label": "Giảm khối lượng công việc", "type": "number"},
                                {"key": "tot_cho_moi_truong", "label": "Tốt cho môi trường", "type": "number"},
                                {"key": "cai_thien_dat", "label": "Cải thiện chất lượng đất", "type": "number"},
                            ],
                            "preset_rows": [
                                "Lên men phụ phẩm cây trồng",
                                "Ủ phân hữu cơ từ phụ phẩm cây trồng tại ruộng",
                                "Xử lý gốc rạ bằng chế phẩm sinh học",
                                "Nuôi trùn quế",
                                "Nuôi sâu canxi",
                                "Nuôi gà trên đệm lót sinh học dày",
                            ],
                        },
                        {
                            "key": "se_tiep_tuc",
                            "label": "Khả năng tiếp tục áp dụng (1=tiếp tục, 6=không tiếp tục)",
                            "type": "table",
                            "columns": [
                                {"key": "ten_ky_thuat", "label": "Kỹ thuật", "type": "text", "required": True},
                                {"key": "muc_do", "label": "Mức độ", "type": "number"},
                            ],
                            "preset_rows": [
                                "Lên men phụ phẩm cây trồng",
                                "Ủ phân hữu cơ tại ruộng",
                                "Xử lý gốc rạ bằng chế phẩm sinh học",
                                "Nuôi trùn quế",
                                "Nuôi sâu canxi",
                                "Nuôi gà trên đệm lót sinh học dày",
                            ],
                        },
                        {
                            "key": "yeu_to_quan_trong",
                            "label": "Yếu tố cân nhắc khi xử lý chất thải (1=không quan trọng, 3=rất quan trọng)",
                            "type": "table",
                            "columns": [
                                {"key": "yeu_to", "label": "Yếu tố", "type": "text", "required": True},
                                {"key": "diem", "label": "Điểm", "type": "number"},
                            ],
                            "preset_rows": [
                                "Tác động đến môi trường",
                                "Tác động cộng đồng xung quanh",
                                "Ý kiến cộng đồng",
                                "Mức độ dễ dàng/tốn công",
                                "Chi phí",
                                "Vệ sinh và sức khỏe",
                                "Ảnh hưởng mùi của chất thải",
                                "Phương pháp người khác áp dụng",
                            ],
                        },
                    ],
                },
                {
                    "title": "Tiếp cận truyền thông & sự kiện",
                    "fields": [
                        {
                            "type": "table",
                            "key": "hoat_dong_truyen_thong",
                            "label": "Nghe nói / tham dự / ảnh hưởng tới quyết định áp dụng",
                            "columns": [
                                {"key": "hoat_dong", "label": "Hoạt động", "type": "text", "required": True},
                                {"key": "da_nghe", "label": "Đã nghe nói", "type": "select", "options": ["Đúng", "Không"]},
                                {"key": "da_tham_du", "label": "Đã tham dự", "type": "select", "options": ["Đúng", "Không"]},
                                {"key": "anh_huong", "label": "Mức ảnh hưởng (1-5)", "type": "number"},
                            ],
                            "preset_rows": [
                                "Được dự án hỗ trợ giống/vật tư (Demo sites)",
                                "Lớp tập huấn TOT",
                                "Lớp tập huấn FFS",
                                "Sinh hoạt HTX/chi hội/câu lạc bộ",
                                "Hội nghị/sự kiện truyền thông",
                                "Chuyến tham quan học tập",
                                "Nông dân khác hướng dẫn",
                            ],
                        },
                        {"key": "su_kien_muon_tham_gia", "label": "Bạn sẽ tham gia sự kiện nào?", "type": "text"},
                        {"key": "ly_do_khong_tham_gia", "label": "Nếu không tham gia, lý do là gì?", "type": "text"},
                        {
                            "type": "table",
                            "key": "kenh_truyen_thong",
                            "label": "Nguồn thông tin đã thấy/nghe và ảnh hưởng (1-5)",
                            "columns": [
                                {"key": "kenh", "label": "Kênh truyền thông", "type": "text", "required": True},
                                {"key": "da_tiep_can", "label": "Đã nghe/nhìn thấy", "type": "select", "options": ["Đúng", "Không"]},
                                {"key": "anh_huong", "label": "Mức ảnh hưởng (1-5)", "type": "number"},
                            ],
                            "preset_rows": [
                                "Băng rôn/áp phích/lịch tuyên truyền",
                                "Loa phát thanh",
                                "Tài liệu kỹ thuật",
                                "Bài viết trên mạng xã hội",
                                "Video trên mạng xã hội",
                                "Trang web Hội Nông dân",
                                "Thông tin trên TV",
                                "Báo/đài phát thanh",
                                "Thấy người khác áp dụng",
                            ],
                        },
                        {
                            "key": "loi_ich_su_kien",
                            "label": "Lợi ích quan trọng nhất/thứ hai khi tham dự sự kiện",
                            "type": "text",
                        },
                    ],
                },
                {
                    "title": "Thông tin kinh tế - xã hội",
                    "fields": [
                        {"key": "thu_nhap_2025", "label": "Ước tính thu nhập trung bình 2025 (đồng/tháng)", "type": "number"},
                        {"key": "nguon_thu_nhap", "label": "Nguồn thu nhập chính", "type": "multi_select", "options": ["Trồng trọt", "Chăn nuôi", "Công ty", "Doanh nghiệp", "Khác"]},
                        {
                            "key": "trinh_do_hoc_van",
                            "label": "Trình độ học vấn",
                            "type": "select",
                            "options": ["Tiểu học", "Trung học cơ sở", "Trung học phổ thông", "Trung cấp", "Cao đẳng/Đại học trở lên"],
                        },
                        {"key": "tham_gia_xanh", "label": "Biết/ tham gia nhóm Người gìn giữ tương lai xanh", "type": "select", "options": ["Thuộc nhóm", "Đã nghe", "Không biết"]},
                        {"key": "muon_tham_gia_xanh", "label": "Có muốn tham gia nhóm Người gìn giữ tương lai xanh?", "type": "select", "options": ["Có", "Không"]},
                    ],
                },
            ]
        },
    },
    {
        "slug": "nuoi-ga-dem-lot",
        "title": "Nuôi gà trên nền đệm lót sinh học dày",
        "source_pdf": "form_pdf/251106 Phiếu phỏng vấn (Nuôi gà trên nền đệm lót sinh học dày) (1).pdf",
        "description": "Theo dõi hộ nuôi gà với đệm lót sinh học dày và sử dụng phân ủ.",
        "schema": {
            "sections": [
                {
                    "title": "Thông tin hộ gia đình",
                    "fields": [
                        {"key": "ho_ten", "label": "Họ và tên người được phỏng vấn", "type": "text", "required": True},
                        {"key": "nam_sinh", "label": "Năm sinh", "type": "number"},
                        {"key": "so_dien_thoai", "label": "Số điện thoại liên hệ", "type": "text"},
                        {"key": "thon", "label": "Thôn", "type": "text"},
                        {"key": "xa", "label": "Xã", "type": "text"},
                        {"key": "tinh", "label": "Tỉnh", "type": "text"},
                    ],
                },
                {
                    "title": "A. Quản lý phụ phẩm cây trồng làm đệm lót",
                    "fields": [
                        {
                            "type": "table",
                            "key": "dem_lot_sinh_hoc",
                            "label": "Lần làm đệm lót sinh học dày",
                            "columns": [
                                {"key": "ten_phu_pham", "label": "Tên phụ phẩm cây trồng", "type": "text", "required": True},
                                {"key": "thoi_diem_bat_dau", "label": "Tháng/năm bắt đầu tận dụng phụ phẩm", "type": "text"},
                                {"key": "tong_mua_vu", "label": "Tổng số mùa vụ đã tận dụng", "type": "number"},
                                {"key": "dien_tich_trong", "label": "Diện tích trồng (sào/vụ)", "type": "number"},
                                {"key": "thoi_diem_lam_dem", "label": "Thời điểm làm đệm gần nhất", "type": "text"},
                                {"key": "dien_tich_su_dung", "label": "Diện tích dùng làm đệm (sào)", "type": "number"},
                                {"key": "khoi_luong_tao_ra", "label": "Khối lượng phụ phẩm tạo ra (kg/sào)", "type": "number"},
                                {"key": "khoi_luong_thu_gom", "label": "Khối lượng phụ phẩm thu gom (kg)", "type": "number"},
                                {"key": "khoi_luong_lam_dem", "label": "Khối lượng dùng làm đệm (kg)", "type": "number"},
                                {"key": "co_may_bam", "label": "Sử dụng máy băm/cắt", "type": "select", "options": ["Có", "Không"]},
                                {"key": "nhien_lieu", "label": "Nhiên liệu đã sử dụng", "type": "text"},
                                {"key": "chi_phi_khac", "label": "Chi phí vật liệu/đầu vào khác (đồng)", "type": "number"},
                            ],
                        }
                    ],
                },
                {
                    "title": "B. Phụ phẩm trước khi áp dụng đệm lót (Năm 2022)",
                    "fields": [
                        {
                            "type": "table",
                            "key": "truoc_khi_dem_lot",
                            "label": "Tình trạng phụ phẩm trước khi làm đệm lót",
                            "columns": [
                                {"key": "loai_cay_trong", "label": "Loại cây trồng", "type": "text", "required": True},
                                {"key": "co_trong", "label": "Có trồng", "type": "select", "options": ["Có", "Không"]},
                                {"key": "dien_tich", "label": "Diện tích (sào/vụ x số vụ/năm)", "type": "text"},
                                {"key": "loai_phu_pham", "label": "Loại phụ phẩm", "type": "text"},
                                {"key": "kg_phu_pham", "label": "KG phụ phẩm tại ruộng (kg/sào/vụ)", "type": "number"},
                                {"key": "kg_thu_gom", "label": "KG phụ phẩm thu gom (kg/sào/vụ)", "type": "number"},
                            ],
                        }
                    ],
                },
                {
                    "title": "C. Bón phân ủ từ lớp đệm lót",
                    "fields": [
                        {
                            "type": "table",
                            "key": "bon_phan_dem_lot",
                            "label": "Một vụ cây trồng gần đây nhất và vụ trước đó",
                            "columns": [
                                {"key": "ten_cay_trong", "label": "Tên cây trồng", "type": "text", "required": True},
                                {"key": "dien_tich", "label": "Diện tích (sào)", "type": "number"},
                                {"key": "phan_su_dung", "label": "Tên/khối lượng từng loại phân bón", "type": "text"},
                                {"key": "chi_phi_phan", "label": "Chi phí mua phân (đồng)", "type": "number"},
                                {"key": "so_lan_phun_thuoc", "label": "Số lần phun thuốc trừ sâu/cỏ", "type": "number"},
                                {"key": "chi_phi_thuoc", "label": "Chi phí thuốc (đồng)", "type": "number"},
                                {"key": "chi_phi_cong", "label": "Chi phí công lao động (đồng)", "type": "number"},
                                {"key": "sau_benh", "label": "Cây bị sâu bệnh?", "type": "select", "options": ["Có", "Không"]},
                                {"key": "nang_suat", "label": "Năng suất thu hoạch (kg/sào)", "type": "number"},
                                {"key": "gia_ban", "label": "Giá bán (đồng/kg)", "type": "number"},
                                {"key": "thanh_tien", "label": "Thành tiền (đồng)", "type": "number"},
                            ],
                        }
                    ],
                },
                {
                    "title": "D. Sử dụng thức ăn & sức khỏe đàn gà",
                    "fields": [
                        {
                            "type": "table",
                            "key": "dan_ga_suc_khoe",
                            "label": "Lứa nuôi gà trên đệm lót gần đây nhất",
                            "columns": [
                                {"key": "thoi_diem", "label": "Thời điểm lứa nuôi", "type": "text", "required": True},
                                {"key": "so_luong", "label": "Số lượng gà trong đợt (con)", "type": "number"},
                                {"key": "thuc_an", "label": "Thức ăn cho lứa nuôi", "type": "text"},
                                {"key": "chi_phi_thuc_an", "label": "Chi phí thức ăn (đồng)", "type": "number"},
                                {"key": "chi_phi_thuoc", "label": "Chi phí thuốc thú y (đồng)", "type": "number"},
                                {"key": "cong_don_dep", "label": "Số giờ dọn dẹp mỗi tuần", "type": "number"},
                                {"key": "benh", "label": "Đàn gà có mắc bệnh không", "type": "select", "options": ["Có", "Không"]},
                                {"key": "suc_khoe", "label": "Đánh giá sức khỏe đàn gà (1-10)", "type": "number"},
                                {"key": "ngay_dat_trong_luong", "label": "Số ngày đạt trọng lượng", "type": "number"},
                                {"key": "trong_luong_tb", "label": "Trọng lượng TB khi xuất chuồng (kg/con)", "type": "number"},
                                {"key": "tong_thoi_gian_nuoi", "label": "Tổng thời gian nuôi đến xuất chuồng (tháng)", "type": "number"},
                                {"key": "gia_ban", "label": "Giá bán (đồng/kg)", "type": "number"},
                                {"key": "thu_nhap", "label": "Tổng thu nhập (đồng)", "type": "number"},
                                {"key": "muc_do_mui", "label": "Đánh giá mùi chuồng gà (0-10)", "type": "number"},
                            ],
                        }
                    ],
                },
            ]
        },
    },
    {
        "slug": "nuoi-sau-canxi",
        "title": "Nuôi sâu canxi",
        "source_pdf": "form_pdf/251106 Phiếu phỏng vấn (Nuôi sâu canxi).pdf",
        "description": "Theo dõi hộ áp dụng nuôi sâu canxi, sử dụng sâu và phân sâu.",
        "schema": {
            "sections": [
                {
                    "title": "A. Quy mô nuôi sâu và cách sử dụng",
                    "fields": [
                        {"key": "ngay_bat_dau", "label": "Tháng/năm bắt đầu nuôi", "type": "text"},
                        {"key": "so_lua_da_nuoi", "label": "Số lứa sâu đã nuôi", "type": "number"},
                        {"key": "so_ngay_mot_lua", "label": "Số ngày cho một lứa (TB 45 ngày)", "type": "number"},
                        {"key": "chi_phi_xay_dung", "label": "Tổng chi phí xây dựng khu nuôi (đồng)", "type": "number"},
                        {"key": "chi_phi_giong", "label": "Chi phí mua giống sâu (trứng)", "type": "number"},
                        {"key": "chi_phi_khac", "label": "Chi phí đầu vào/vật liệu khác", "type": "number"},
                        {
                            "key": "cach_su_dung_sau",
                            "label": "Cách sử dụng sâu canxi",
                            "type": "multi_select",
                            "options": ["Làm thức ăn vật nuôi", "Đem bán", "Khác"],
                        },
                        {
                            "type": "table",
                            "key": "vat_nuoi_an_sau",
                            "label": "Động vật sử dụng sâu canxi làm thức ăn",
                            "columns": [
                                {"key": "ten_loai", "label": "Tên loài vật nuôi", "type": "text", "required": True},
                                {"key": "so_con", "label": "Số lượng con/lứa", "type": "number"},
                                {"key": "so_lua_duoc_cho_an", "label": "Số lứa được cho ăn sâu", "type": "number"},
                            ],
                        },
                        {
                            "type": "table",
                            "key": "cay_trong_bon_phan_sau",
                            "label": "Cây trồng được bón phân sâu canxi",
                            "columns": [
                                {"key": "ten_cay_trong", "label": "Tên cây trồng", "type": "text", "required": True},
                                {"key": "so_vu", "label": "Tổng số vụ bón", "type": "number"},
                                {"key": "dien_tich", "label": "Diện tích (sào/vụ)", "type": "number"},
                            ],
                        },
                    ],
                },
                {
                    "title": "B. Thức ăn cho sâu và sản phẩm lứa gần đây nhất",
                    "fields": [
                        {
                            "type": "table",
                            "key": "thuc_an_sau",
                            "label": "Thức ăn và đầu ra của lứa sâu gần nhất",
                            "columns": [
                                {"key": "loai_phu_pham", "label": "Loại phụ phẩm nông nghiệp", "type": "text", "required": True},
                                {"key": "khoi_luong_ngay", "label": "Khối lượng phụ phẩm/ngày", "type": "number"},
                                {"key": "so_luong_vat_nuoi_thai", "label": "Số lượng vật nuôi tạo phân thải", "type": "number"},
                                {"key": "so_ngay_lua", "label": "Số ngày/lứa nuôi", "type": "number"},
                                {"key": "so_lua", "label": "Số lứa nuôi bằng phụ phẩm này", "type": "number"},
                                {"key": "tong_khoi_luong", "label": "Tổng khối lượng phụ phẩm tạo ra (kg)", "type": "number"},
                                {"key": "phu_pham_dung_cho_sau", "label": "Khối lượng dùng cho sâu (kg/ngày)", "type": "number"},
                                {"key": "ty_le_su_dung", "label": "Tỷ lệ % phụ phẩm dùng cho sâu", "type": "number"},
                                {"key": "dien_tich_nuoi", "label": "Diện tích nuôi sâu (m2/lứa)", "type": "number"},
                                {"key": "chi_phi_giong", "label": "Chi phí mua giống (đồng)", "type": "number"},
                                {"key": "so_ngay_thu_hoach", "label": "Số ngày để thu hoạch một lứa", "type": "number"},
                                {"key": "khoi_luong_sau", "label": "Khối lượng sâu thu được (kg/lứa)", "type": "number"},
                                {"key": "khoi_luong_phan", "label": "Khối lượng phân sâu thu được (kg/lứa)", "type": "number"},
                                {"key": "cong_lao_dong", "label": "Công lao động (giờ/ngày)", "type": "number"},
                            ],
                        }
                    ],
                },
                {
                    "title": "C. Sử dụng phân sâu canxi cho cây trồng",
                    "fields": [
                        {
                            "type": "table",
                            "key": "bon_phan_sau",
                            "label": "Vụ cây trồng gần đây nhất",
                            "columns": [
                                {"key": "ten_cay_trong", "label": "Tên cây trồng", "type": "text", "required": True},
                                {"key": "thoi_gian_trong", "label": "Thời gian trồng (tháng/năm)", "type": "text"},
                                {"key": "dien_tich", "label": "Diện tích (sào/vụ)", "type": "number"},
                                {"key": "phan_su_dung", "label": "Khối lượng từng loại phân bón", "type": "text"},
                                {"key": "chi_phi_phan", "label": "Chi phí mua phân (đồng)", "type": "number"},
                                {"key": "so_lan_phun_thuoc", "label": "Số lần phun thuốc trừ sâu/cỏ", "type": "number"},
                                {"key": "chi_phi_thuoc", "label": "Chi phí thuốc (đồng)", "type": "number"},
                                {"key": "chi_phi_cong", "label": "Chi phí chăm sóc/nhân công (đồng)", "type": "number"},
                                {"key": "sau_benh", "label": "Cây bị sâu bệnh?", "type": "select", "options": ["Có", "Không"]},
                                {"key": "nang_suat", "label": "Năng suất thu hoạch (kg/sào)", "type": "number"},
                                {"key": "gia_ban", "label": "Giá bán (đồng/kg)", "type": "number"},
                                {"key": "thanh_tien", "label": "Thành tiền (đồng)", "type": "number"},
                            ],
                        }
                    ],
                },
            ]
        },
    },
    {
        "slug": "nuoi-trun-que",
        "title": "Nuôi trùn quế",
        "source_pdf": "form_pdf/251106 Phiếu phỏng vấn (Nuôi trùn quế).pdf",
        "description": "Theo dõi hộ áp dụng nuôi trùn quế, sử dụng trùn và phân trùn.",
        "schema": {
            "sections": [
                {
                    "title": "A. Quy mô nuôi trùn và sử dụng",
                    "fields": [
                        {"key": "ngay_bat_dau", "label": "Tháng/năm bắt đầu nuôi", "type": "text"},
                        {"key": "so_lua_da_nuoi", "label": "Số lứa trùn đã nuôi", "type": "number"},
                        {"key": "so_ngay_mot_lua", "label": "Số ngày cho một lứa (TB 60 ngày)", "type": "number"},
                        {"key": "chi_phi_xay_dung", "label": "Tổng chi phí xây dựng khu nuôi (đồng)", "type": "number"},
                        {"key": "chi_phi_giong", "label": "Chi phí mua sinh khối trùn giống", "type": "number"},
                        {"key": "chi_phi_khac", "label": "Chi phí đầu vào/vật liệu khác", "type": "number"},
                        {
                            "key": "cach_su_dung_trun",
                            "label": "Cách sử dụng trùn quế",
                            "type": "multi_select",
                            "options": ["Làm thức ăn vật nuôi", "Đem bán", "Khác"],
                        },
                        {
                            "type": "table",
                            "key": "vat_nuoi_an_trun",
                            "label": "Động vật sử dụng trùn quế làm thức ăn",
                            "columns": [
                                {"key": "ten_loai", "label": "Tên loài vật nuôi", "type": "text", "required": True},
                                {"key": "so_con", "label": "Số lượng con/lứa", "type": "number"},
                                {"key": "so_lua_duoc_cho_an", "label": "Số lứa được cho ăn trùn", "type": "number"},
                            ],
                        },
                        {
                            "type": "table",
                            "key": "cay_trong_bon_phan_trun",
                            "label": "Cây trồng được bón phân trùn quế",
                            "columns": [
                                {"key": "ten_cay_trong", "label": "Tên cây trồng", "type": "text", "required": True},
                                {"key": "so_vu", "label": "Tổng số vụ bón", "type": "number"},
                                {"key": "dien_tich", "label": "Diện tích (sào/vụ)", "type": "number"},
                            ],
                        },
                    ],
                },
                {
                    "title": "B. Thức ăn cho trùn và sản phẩm lứa gần đây nhất",
                    "fields": [
                        {
                            "type": "table",
                            "key": "thuc_an_trun",
                            "label": "Thức ăn và đầu ra của lứa trùn gần nhất",
                            "columns": [
                                {"key": "loai_phu_pham", "label": "Loại phụ phẩm nông nghiệp", "type": "text", "required": True},
                                {"key": "khoi_luong_ngay", "label": "Khối lượng phụ phẩm/ngày", "type": "number"},
                                {"key": "so_luong_vat_nuoi_thai", "label": "Số lượng vật nuôi tạo phân thải", "type": "number"},
                                {"key": "so_ngay_lua", "label": "Số ngày/lứa nuôi", "type": "number"},
                                {"key": "so_lua", "label": "Số lứa nuôi bằng phụ phẩm này", "type": "number"},
                                {"key": "tong_khoi_luong", "label": "Tổng khối lượng phụ phẩm tạo ra (kg)", "type": "number"},
                                {"key": "phu_pham_dung_cho_trun", "label": "Khối lượng dùng cho trùn (kg/ngày)", "type": "number"},
                                {"key": "ty_le_su_dung", "label": "Tỷ lệ % phụ phẩm dùng cho trùn", "type": "number"},
                                {"key": "dien_tich_nuoi", "label": "Diện tích nuôi trùn (m2/lứa)", "type": "number"},
                                {"key": "chi_phi_giong", "label": "Chi phí mua giống (đồng)", "type": "number"},
                                {"key": "so_ngay_thu_hoach", "label": "Số ngày để thu hoạch một lứa", "type": "number"},
                                {"key": "khoi_luong_trun", "label": "Khối lượng trùn thu được (kg/lứa)", "type": "number"},
                                {"key": "khoi_luong_phan", "label": "Khối lượng phân trùn thu được (kg/lứa)", "type": "number"},
                                {"key": "cong_lao_dong", "label": "Công lao động (giờ/ngày)", "type": "number"},
                            ],
                        }
                    ],
                },
                {
                    "title": "C. Sử dụng phân trùn quế cho cây trồng",
                    "fields": [
                        {
                            "type": "table",
                            "key": "bon_phan_trun",
                            "label": "Vụ cây trồng gần đây nhất",
                            "columns": [
                                {"key": "ten_cay_trong", "label": "Tên cây trồng", "type": "text", "required": True},
                                {"key": "thoi_gian_trong", "label": "Thời gian trồng (tháng/năm)", "type": "text"},
                                {"key": "dien_tich", "label": "Diện tích (sào/vụ)", "type": "number"},
                                {"key": "phan_su_dung", "label": "Khối lượng từng loại phân bón", "type": "text"},
                                {"key": "chi_phi_phan", "label": "Chi phí mua phân (đồng)", "type": "number"},
                                {"key": "so_lan_phun_thuoc", "label": "Số lần phun thuốc trừ sâu/cỏ", "type": "number"},
                                {"key": "chi_phi_thuoc", "label": "Chi phí thuốc (đồng)", "type": "number"},
                                {"key": "chi_phi_cong", "label": "Chi phí chăm sóc/nhân công (đồng)", "type": "number"},
                                {"key": "sau_benh", "label": "Cây bị sâu bệnh?", "type": "select", "options": ["Có", "Không"]},
                                {"key": "nang_suat", "label": "Năng suất thu hoạch (kg/sào)", "type": "number"},
                                {"key": "gia_ban", "label": "Giá bán (đồng/kg)", "type": "number"},
                                {"key": "thanh_tien", "label": "Thành tiền (đồng)", "type": "number"},
                            ],
                        }
                    ],
                },
                {
                    "title": "D. Sử dụng trùn quế làm thức ăn cho vật nuôi",
                    "fields": [
                        {
                            "type": "table",
                            "key": "thuc_an_trun_cho_vat_nuoi",
                            "label": "So sánh lứa nuôi gần đây nhất và trước khi dùng trùn quế",
                            "columns": [
                                {"key": "ten_vat_nuoi", "label": "Loại vật nuôi", "type": "text", "required": True},
                                {"key": "so_con", "label": "Số con/lứa", "type": "number"},
                                {"key": "thuc_an_sau", "label": "Thức ăn (sau khi dùng trùn)", "type": "text"},
                                {"key": "chi_phi_sau", "label": "Chi phí thức ăn (sau) (đồng)", "type": "number"},
                                {"key": "suc_khoe_sau", "label": "Đánh giá sức khỏe (1-10) sau", "type": "number"},
                                {"key": "thoi_gian_xuat_sau", "label": "Thời gian & trọng lượng xuất chuồng (sau)", "type": "text"},
                                {"key": "thuc_an_truoc", "label": "Thức ăn (trước khi dùng trùn)", "type": "text"},
                                {"key": "chi_phi_truoc", "label": "Chi phí thức ăn (trước) (đồng)", "type": "number"},
                                {"key": "suc_khoe_truoc", "label": "Đánh giá sức khỏe (1-10) trước", "type": "number"},
                                {"key": "thoi_gian_xuat_truoc", "label": "Thời gian & trọng lượng xuất chuồng (trước)", "type": "text"},
                                {"key": "gia_ban", "label": "Giá bán (đồng/kg)", "type": "number"},
                                {"key": "thu_nhap", "label": "Thành tiền/thu nhập (đồng)", "type": "number"},
                            ],
                        }
                    ],
                },
            ]
        },
    },
]
