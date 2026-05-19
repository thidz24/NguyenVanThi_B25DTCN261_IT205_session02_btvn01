# Nhập dữ liệu từ người dùng
print('---HỆ THỐNG TIẾP NHẬN BỆNH NHÂN---');
name_patient = input('Nhập tên bệnh nhân: ');
age = int(input('Nhập tuổi: '));
sympton = input('Mời bạn nhập triệu chứng của bệnh nhân: ');

# In dữ liệu ra
print('---PHIẾU KHÁM BỆNH---');
print('Tên bệnh nhân:',name_patient);
print('Tuổi:',age);
print('Triệu chứng:',sympton);