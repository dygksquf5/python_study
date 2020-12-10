def product_except_self(nums):
    out = []
    p = 1

    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]

    print(out)

    p = 1
    for i in range(len(nums) -1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out


a = [1, 2, 3, 4]
print(product_except_self(a))