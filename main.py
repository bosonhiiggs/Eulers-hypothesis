import time
start_time = time.time()

for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum_num = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(sum_num ** (1 / 5))
                if sum_num == e ** 5:
                    print(a, b, c, d, e)
                    print(a + b + c + d + e)
                    time_out = time.time()
                    print(f'Time answer: {time_out - start_time}')
                    break

time_out = time.time()
print(f'Time out: {time_out - start_time}')
