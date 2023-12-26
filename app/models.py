from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app import db, app
import enum

class LoaiNguoiDung(enum.Enum):
    ADMIN = 1
    NHANVIEN = 2
    GIAOVIEN = 3

class NguoiDung(db.Model, UserMixin):
    __tablename__ = 'nguoidung'

    manguoidung = Column(Integer, primary_key=True, autoincrement=True)
    tennguoidung = Column(String(50), nullable=False)
    taikhoan = Column(String(50), nullable=False, unique=True)
    matkhau = Column(String(50), nullable=False)
    loainguoidung = Column(Enum(LoaiNguoiDung))

    giaoviens = relationship('GiaoVien', backref='nguoidung', lazy=True)
    nhanviens = relationship('NhanVien', backref='nguoidung', lazy=True)

    def get_id(self):
        return self.manguoidung

class Khoi(db.Model):
    __tablename__ = 'khoi'

    makhoi = Column(Integer, primary_key=True, autoincrement=True)
    tenkhoi = Column(String(50), nullable=False)

    monhocs = relationship('MonHoc', backref='khoi', lazy=True)
    lops = relationship('Lop', backref='khoi', lazy=True)

class NamHoc(db.Model):
    __tablename__ = 'namhoc'
    manam = Column(Integer, primary_key=True, autoincrement=True)
    nam = Column(String(20), nullable=False)

    lops = relationship('Lop', backref='namhoc', lazy=True)
    phancongs = relationship('PhanCong', backref='namhoc', lazy=True)
    diems = relationship('Diem', backref='namhoc', lazy=True)
    bangdiemmonhocs = relationship('BangDiemMonHoc', backref='namhoc', lazy=True)
    bangdiemtrungbinhs = relationship('BangDiemTrungBinh', backref='namhoc', lazy=True)
    baocaos = relationship('BaoCao', backref='namhoc', lazy=True)

class HocKy(db.Model):
    __tablename__ = 'hocky'

    mahocky = Column(Integer, primary_key=True, autoincrement=True)
    hocky = Column(String(20), nullable=False)

    diems = relationship('Diem', backref='hocky', lazy=True)
    bangdiemmonhocs = relationship('BangDiemMonHoc', backref='hocky', lazy=True)

class MonHoc(db.Model):
    __tablename__ = 'monhoc'

    mamon = Column(Integer, primary_key=True, autoincrement=True)
    tenmon = Column(String(50), nullable=False)
    khoi_id = Column(Integer, ForeignKey('khoi.makhoi'), nullable=False)

    giaoviens = relationship('GiaoVien', backref='monhoc', lazy=True)
    phancongs = relationship('PhanCong', backref='monhoc', lazy=True)
    diems = relationship('Diem', backref='monhoc', lazy=True)
    bangdiemmonhocs = relationship('BangDiemMonHoc', backref='monhoc', lazy=True)
    baocaos = relationship('BaoCao', backref='hocsinh', lazy=True)

class HocSinh(db.Model):
    __tablename__ = 'hocsinh'

    mahocsinh = Column(Integer, primary_key=True, autoincrement=True)
    hoten = Column(String(50), nullable=False)
    ngaysinh = Column(Date, nullable=False)
    gioitinh = Column(String(10), nullable=False)
    diachi = Column(String(100), nullable=False)
    sodienthoai = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)

    phanlops = relationship('PhanLop', backref='hocsinh', lazy=True)
    diems = relationship('Diem', backref='hocsinh', lazy=True)
    bangdiemmonhocs = relationship('BangDiemMonHoc', backref='hocsinh', lazy=True)
    bangdiemtrungbinhs = relationship('BangDiemTrungBinh', backref='hocsinh', lazy=True)

class GiaoVien(db.Model):
    __tablename__ = 'giaovien'

    magiaovien = Column(Integer, primary_key=True, autoincrement=True)
    hoten = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    sodienthoai = Column(String(20), nullable=False)
    monhoc_id = Column(Integer, ForeignKey('monhoc.mamon'), nullable=False)
    nguoidung_id = Column(Integer, ForeignKey('nguoidung.manguoidung'), nullable=False)

    lops = relationship('Lop', backref='giaovien', lazy=True)
    phancongs = relationship('PhanCong', backref='giaovien', lazy=True)

class NhanVien(db.Model):
    __tablename__ = 'nhanvien'

    manhanvien = Column(Integer, primary_key=True, autoincrement=True)
    hoten = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    sodienthoai = Column(String(20), nullable=False)
    nguoidung_id = Column(Integer, ForeignKey('nguoidung.manguoidung'), nullable=False)

class Lop(db.Model):
    __tablename__ = 'lop'

    malop = Column(Integer, primary_key=True, autoincrement=True)
    tenlop = Column(String(50), nullable=False)
    siso = Column(Integer, nullable=False)
    khoi_id = Column(Integer, ForeignKey('khoi.makhoi'), nullable=False)
    namhoc_id = Column(Integer, ForeignKey('namhoc.manam'), nullable=False)
    giaovien_id = Column(Integer, ForeignKey('giaovien.magiaovien'), nullable=False)

    phanlops = relationship('PhanLop', backref='lop', lazy=True)
    phancongs = relationship('PhanCong', backref='lop', lazy=True)
    bangdiemmonhocs = relationship('BangDiemMonHoc', backref='lop', lazy=True)
    bangdiemtrungbinhs = relationship('BangDiemTrungBinh', backref='lop', lazy=True)
    baocaos = relationship('BaoCao', backref='lop', lazy=True)

class PhanLop(db.Model):
    __tablename__ = 'phanlop'

    stt = Column(Integer, primary_key=True, autoincrement=True)
    hocsinh_id = Column(Integer, ForeignKey('hocsinh.mahocsinh'), nullable=False)
    lop_id = Column(Integer, ForeignKey('lop.malop'), nullable=False)
    namhoc_id = Column(Integer, ForeignKey('namhoc.manam'), nullable=False)

class PhanCong(db.Model):
    __tablename__ = 'phancong'

    stt = Column(Integer, primary_key=True, autoincrement=True)
    giaovien_id = Column(Integer, ForeignKey('giaovien.magiaovien'), nullable=False)
    lop_id = Column(Integer, ForeignKey('lop.malop'), nullable=False)
    monhoc_id = Column(Integer, ForeignKey('monhoc.mamon'), nullable=False)
    namhoc_id = Column(Integer, ForeignKey('namhoc.manam'), nullable=False)

class Diem(db.Model):
    __tablename__ = 'diem'

    stt = Column(Integer, primary_key=True, autoincrement=True)
    hocsinh_id = Column(Integer, ForeignKey('hocsinh.mahocsinh'), nullable=False)
    monhoc_id = Column(Integer, ForeignKey('monhoc.mamon'), nullable=False)
    namhoc_id = Column(Integer, ForeignKey('namhoc.manam'), nullable=False)
    hocky_id = Column(Integer, ForeignKey('hocky.mahocky'), nullable=False)
    loaidiem = Column(String(20), nullable=False)
    diem = Column(Float, nullable=False)

class BangDiemMonHoc(db.Model):
    __tablename__ = 'bangdiemmonhoc'

    stt = Column(Integer, primary_key=True, autoincrement=True)
    hocsinh_id = Column(Integer, ForeignKey('hocsinh.mahocsinh'), nullable=False)
    lop_id = Column(Integer, ForeignKey('lop.malop'), nullable=False)
    monhoc_id = Column(Integer, ForeignKey('monhoc.mamon'), nullable=False)
    hocky_id = Column(Integer, ForeignKey('hocky.mahocky'), nullable=False)
    namhoc_id = Column(Integer, ForeignKey('namhoc.manam'), nullable=False)
    diem15p = Column(Float, nullable=False)
    diem1t = Column(Float, nullable=False)
    diemthi = Column(Float, nullable=False)

class BangDiemTrungBinh(db.Model):
    __tablename__ = 'bangdiemtrungbinh'

    stt = Column(Integer, primary_key=True, autoincrement=True)
    hocsinh_id = Column(Integer, ForeignKey('hocsinh.mahocsinh'), nullable=False)
    lop_id = Column(Integer, ForeignKey('lop.malop'), nullable=False)
    namhoc_id = Column(Integer, ForeignKey('namhoc.manam'), nullable=False)
    diemtbhk1 = Column(Float, nullable=False)
    diemtbhk2 = Column(Float, nullable=False)

class BaoCao(db.Model):
    __tablename__ = 'baocao'

    stt = Column(Integer, primary_key=True, autoincrement=True)
    monhoc_id = Column(Integer, ForeignKey('monhoc.mamon'), nullable=False)
    namhoc_id = Column(Integer, ForeignKey('namhoc.manam'), nullable=False)
    lop_id = Column(Integer, ForeignKey('lop.malop'), nullable=False)
    siso = Column(Integer, nullable=False)
    soluongdat = Column(Integer, nullable=False)
    tyle = Column(Float, nullable=False)

class QuyDinh(db.Model):
    __tablename__ = 'quydinh'

    maquydinh = Column(Integer, primary_key=True, autoincrement=True)
    tenquydinh = Column(String(50), nullable=False)
    giatri = Column(Integer, nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib
        a = NguoiDung(tennguoidung='Admin', taikhoan='admin', matkhau=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()), loainguoidung=LoaiNguoiDung.ADMIN)
        b = NguoiDung(tennguoidung='NhanVien', taikhoan='nhanvien', matkhau=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()), loainguoidung=LoaiNguoiDung.NHANVIEN)
        c = NguoiDung(tennguoidung='GiaoVien', taikhoan='giaovien', matkhau=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()), loainguoidung=LoaiNguoiDung.GIAOVIEN)
        db.session.add(a)
        db.session.add(b)
        db.session.add(c)
        db.session.commit()