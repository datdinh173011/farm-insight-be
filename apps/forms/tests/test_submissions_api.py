from io import BytesIO

from django.contrib.auth import get_user_model
from django.urls import reverse
from openpyxl import load_workbook
from rest_framework import status
from rest_framework.test import APITestCase

from apps.forms.data.pdf_form_schemas import FORM_SCHEMAS
from apps.forms.models import FormSubmission, FormTemplate


class FormSubmissionApiTests(APITestCase):
    def setUp(self):
        template_data = next(
            t for t in FORM_SCHEMAS if t["template_type"] == "nuoi-sau-canxi")
        self.template = FormTemplate.objects.create(
            template_type=template_data["template_type"],
            title=template_data["title"],
            description=template_data.get("description", ""),
            source_pdf=template_data.get("source_pdf", ""),
            schema=template_data["schema"],
        )
        self.user = get_user_model().objects.create_user(
            username="exporter", password="password123"
        )

    def test_create_submission_for_nuoi_sau_canxi(self):
        url = reverse("form-submission-list")
        payload = {
            "template_type": self.template.template_type,
            "ho_ten": "Nguyen Van A",
            "nam_sinh": 1985,
            "so_dien_thoai": "0909123456",
            "thon": "Thon 1",
            "xa": "Xa ABC",
            "tinh": "Tinh XYZ",
            "data": {
                "vat_nuoi_an_sau": [
                    {"ten_loai": "Ga", "so_con": 50, "so_lua_duoc_cho_an": 3},
                ],
                "cay_trong_bon_phan_sau": [
                    {"ten_cay_trong": "Lua", "so_vu": 2, "dien_tich": 3},
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
                        "cong_lao_dong": 2,
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
                        "thanh_tien": 3600000,
                    }
                ],
            },
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data["template_type"], self.template.template_type)
        self.assertEqual(FormSubmission.objects.count(), 1)
        submission = FormSubmission.objects.first()
        self.assertIsNone(submission.created_by)
        self.assertEqual(submission.ho_ten, payload["ho_ten"])
        self.assertEqual(submission.template, self.template)

    def test_create_two_submissions_for_two_templates(self):
        # Create second template (nhom-cau-hoi-chung)
        chung_data = next(
            t for t in FORM_SCHEMAS if t["template_type"] == "nhom-cau-hoi-chung")
        chung_template = FormTemplate.objects.create(
            template_type=chung_data["template_type"],
            title=chung_data["title"],
            description=chung_data.get("description", ""),
            source_pdf=chung_data.get("source_pdf", ""),
            schema=chung_data["schema"],
        )

        url = reverse("form-submission-list")

        # First submission for nuoi-sau-canxi
        payload_sau = {
            "template_type": self.template.template_type,
            "ho_ten": "Nguyen Van A",
            "nam_sinh": 1985,
            "so_dien_thoai": "0909123456",
            "thon": "Thon 1",
            "xa": "Xa ABC",
            "tinh": "Tinh XYZ",
            "data": {"vat_nuoi_an_sau": [{"ten_loai": "Ga", "so_con": 10, "so_lua_duoc_cho_an": 1}]},
        }
        resp_sau = self.client.post(url, payload_sau, format="json")
        self.assertEqual(resp_sau.status_code, status.HTTP_201_CREATED)

        # Second submission for nhom-cau-hoi-chung
        payload_chung = {
            "template_type": chung_template.template_type,
            "ho_ten": "Tran Thi B",
            "nam_sinh": 1990,
            "so_dien_thoai": "0911222333",
            "thon": "Thon 2",
            "xa": "Xa DEF",
            "tinh": "Tinh UVW",
            "data": {
                "xu_ly_phu_pham": [
                    {"phuong_phap": "Dot", "truoc_tham_gia": 80, "sau_tham_gia": 20},
                ],
                "xu_ly_goc_ra": [
                    {"phuong_phap": "Chon dat",
                        "truoc_tham_gia": 60, "sau_tham_gia": 10},
                ],
                "xu_ly_phan_chan_nuoi": [
                    {"phuong_phap": "U phan", "truoc_tham_gia": 50, "sau_tham_gia": 70},
                ],
                "danh_gia_ky_thuat": [
                    {
                        "ten_ky_thuat": "Len men phu pham",
                        "do_kho": 5,
                        "loi_nhuan": 4,
                        "giam_chi_phi": 4,
                        "giam_cong_viec": 3,
                        "tot_cho_moi_truong": 5,
                        "cai_thien_dat": 4,
                    }
                ],
                "hoat_dong_truyen_thong": [
                    {"hoat_dong": "Lop tap huan TOT", "da_nghe": "Đúng",
                        "da_tham_du": "KHÔNG", "anh_huong": 3}
                ],
            },
        }
        resp_chung = self.client.post(url, payload_chung, format="json")
        self.assertEqual(resp_chung.status_code, status.HTTP_201_CREATED)

        self.assertEqual(FormSubmission.objects.count(), 2)
        self.assertEqual(
            set(FormSubmission.objects.values_list("template_type", flat=True)),
            {self.template.template_type, chung_template.template_type},
        )

    def test_export_excel_contains_submission_row(self):
        url = reverse("form-submission-list")
        # Use a len-men-phu-pham template so the labels are available for export formatting.
        len_men_data = next(
            t for t in FORM_SCHEMAS if t["template_type"] == "len-men-phu-pham")
        len_men_template = FormTemplate.objects.create(
            template_type=len_men_data["template_type"],
            title=len_men_data["title"],
            description=len_men_data.get("description", ""),
            source_pdf=len_men_data.get("source_pdf", ""),
            schema=len_men_data["schema"],
        )
        payload = {
            "template_type": len_men_template.template_type,
            "ho_ten": "Nguyen Van A",
            "nam_sinh": 1985,
            "so_dien_thoai": "0909123456",
            "thon": "Thon 1",
            "xa": "Xa ABC",
            "tinh": "Tinh XYZ",
            "data": {
                "sectionA": [{"tenPhuPhamCayTrong": "rom ra", "thangNamDau": "9/2023"}],
                "sectionB": [],
            },
        }
        self.client.post(url, payload, format="json")

        export_url = reverse("form-submission-export-excel")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(export_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response["Content-Type"],
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

        workbook = load_workbook(filename=BytesIO(response.content))
        sheet_name = len_men_template.template_type[:31]
        sheet = workbook[sheet_name]
        headers = [cell.value for cell in sheet[1]]
        row = [cell.value for cell in sheet[2]]
        row_data = dict(zip(headers, row))

        self.assertEqual(row_data["STT"], 1)
        self.assertEqual(row_data["Loại Mẫu Form"], len_men_template.template_type)
        self.assertEqual(row_data["Họ Tên"], payload["ho_ten"])
        self.assertEqual(row_data["Năm Sinh"], payload["nam_sinh"])
        first_field_header = "SECTIONA - Tên phụ phẩm cây trồng (sử dụng ủ lên men)"
        self.assertIn("rom ra", row_data[first_field_header])
