# ДЗ модуль 2_6. Доп. задание по модулю 2_hard."Древний шифр."
# ==========================================================
import random
n = random.randint(3, 20)
pass_ = []
rebus = [n]
for i in range(1, 20):
    is_n = True
    for j in range(1, 20):
        a = i + j
        if n % a == 0:
            if a != i:
                if a != j:
                    is_n = True
                if is_n == True:
                    pass_.append([i,j])
print(rebus+pass_)
print(f'Если число в открытой вставке = {n}, ключи к открытию ворот пары чисел {pass_}')
