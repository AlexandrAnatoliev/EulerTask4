#  EulerTask4 - Наибольшее произведение-палиндром

# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

def is_plm(number):
    num_str = str(number)
    num_str_inv = num_str[::-1]
    if num_str == num_str_inv:
        return True
    else:
        return False


def max_plm(num1, num2):
    i_pol = 1
    j_pol = 1
    max_pol = 1
    pol = 1
    for i in range(num1, 0, -1):
        for j in range(num2, 0, -1):
            num = i * j
            if is_plm(num):
                pol = num
            if pol > max_pol:
                max_pol = pol
                i_pol = i
                j_pol = j
    print(f"{max_pol} - самый большой палиндром, полученный умножением двух чисел: {i_pol} и {j_pol}")


max_plm(999, 999)
