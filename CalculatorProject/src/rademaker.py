def buggy_function(arr, divisor):
    # 结果数组
    result = []

    # 尝试访问数组的第六个元素（可能导致数组越界错误）
    sixth_element = arr[5]
    result.append(sixth_element)

    # 尝试将数组的每个元素除以传入的divisor（可能导致零除错误）
    for i in range(len(arr)):
        result.append(arr[i] / divisor)


    return result

# 示例调用
arr = [1, 2, 3, 4, 5]
divisor = 0
result = buggy_function(arr, divisor)
print("结果：", result)
