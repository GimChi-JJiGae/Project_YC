import string
from django.core.exceptions import ValidationError

def contains_special_character(value):
    for char in value:
        if char in string.punctuation:  # string.pucntuation에는 특수문자들이 저장되어 있음!
            return True                 # 그걸 이용해서 특수문자 걸러내기
    return False

def contains_uppercase_letter(value):
    for char in value:
        if char in string.ascii_uppercase:
            return True
    return False

def contains_lowercaes_letter(value):
    for char in value:
        if char in string.ascii_lowercase:
            return True
    return False

def contains_number(value):
    for char in value:
        if char in string.digits:
            return True
    return False

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
            len(password) < 8 or
            len(password) > 16 or
            # not contains_uppercase_letter(password) or
            not contains_lowercaes_letter(password) or
            not contains_number(password) or
            not contains_special_character(password)
        ):
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.")
    
    def get_help_text(self):
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자 조합을 입력해주세요.(get_help_text)"

def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")