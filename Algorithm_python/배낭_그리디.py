

data_list = [(15, 12), (10, 10), (25, 8), (30, 5), (20, 10)]


def get_max_value(data_list, K):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True) # 무게 대비 가치가 가장 높은 것 부터 앞으로 배치 !
    total_value = 0
    details = []

    for data in data_list:
        if K - data[0] >= 0:
            K -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = K / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break # 한개의 무개가 온전히 다 들어갈 수 없는 상태라는건 결국 이거만큼 들어가면 더이상 들어가라 자리 없다는거, 즉 => 브레이크 걸기

    return details, total_value


print(get_max_value(data_list, 30))



