def validate_resident_number(resident_number):
    if len(resident_number) != 13:
        return False

    digits = [int(digit) for digit in resident_number]

    total = sum(digits[i] * (i + 2) for i in range(12))

    remainder = total % 11

    result = 11 - remainder

    if result == digits[12]:
        return True
    else:
        return False

resident_number = input("주민등록번호를 입력하세요: ")

if validate_resident_number(resident_number):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
