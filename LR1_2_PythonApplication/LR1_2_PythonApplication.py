# -*- coding: cp1251 -*-

# ���������, ������� ���������� ������ ��������� ��������� ������� �� ��������� �� 5 �� 14*10.
# ���������� ��������� � ������ 14+10.

import random

# ����� �� �������
journal_number = 14

# ����������� �������� � ������
min_value_in_list = 5
# ������������ �������� � ������ (14 * 100 = 1400)
max_value_in_list = journal_number * 100
# ����� ��������� � ������ (14 + 10 = 24)
element_count = journal_number + 10

# �������� ������� ������
random_list = []

# �������, ������� ���������� ������ ��������� ����� � �������� ��������� �������� � ����������� ���������
def generate_random_list(min_value_in_list, max_value_in_list, element_count):
    # ��������� ���������
    for i in range(element_count):
        # ���������� � ������ ���������� ����� �� 5 �� 1400
        random_list.append(random.randint(min_value_in_list, max_value_in_list))

    return random_list

# ����� ����������
print("��������������� ������: ", generate_random_list(min_value_in_list, max_value_in_list, element_count))
