print(" -- EMERGENCY TRIAGE SYSTEM -")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

# Hệ thống phân loại u tiên
if heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")

# Dò luồng bằng cách nhập heart_rate = 135 
# if-elif-else thực hiện theo luồng từ trên xuống dưới nếu if đúng thì lấy if bỏ qua elif và else, còn nếu sai thì sẽ xét tiếp trường hợp của elif và else
# Khối lệnh RED bị bỏ qua vì khối lệnh của if > 100 đã đúng và không xét tiếp các trường hợp tiếp nữa
# Sửa lại khối lệnh :
print(" -- EMERGENCY TRIAGE SYSTEM -")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

# Hệ thống phân loại u tiên
if heart_rate < 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")
