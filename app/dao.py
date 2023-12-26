from app.models import NguoiDung, LoaiNguoiDung
from app import app
import hashlib

def get_user_by_id(user_id):
    return NguoiDung.query.get(user_id)

def auth_user(taikhoan, matkhau):
    matkhau = str(hashlib.md5(matkhau.encode('utf-8')).hexdigest())

    return NguoiDung.query.filter(NguoiDung.taikhoan.__eq__(taikhoan), NguoiDung.matkhau.__eq__(matkhau)).first()