def buggy_function(arr, divisor):
    # 结果数组
    result = []

    sixth_element = arr[5]
    result.append(sixth_element)

    for i in range(len(arr)):
        result.append(arr[i] / divisor)


    return result

# 示例调用
arr = [1, 2, 3, 4, 5]
divisor = 0
result = buggy_function(arr, divisor)
print("结果：", result)
