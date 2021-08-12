def find_Longes_prefix(arr):
    if len(arr) == 1:
        return arr[0]

    ele = arr[0]

    ret = ""

    for e, c in enumerate(ele):
        for stri in arr[1:]:
            if c == stri[e]:
                continue
            else:
                return ret
        ret += c

    return ret

    #
    # small_ans = find_Longes_prefix(arr[1:]) #prepaid
    #
    # if small_ans == "":
    #     return ""
    # else:
    #     ret = ""
    #     i = 0
    #     for c in ele:#ele = prepone
    #         if c == small_ans[i]:
    #             ret += small_ans[i]
    #             i += 1
    #         else:
    #             return ret


li = ["prefix", "prepone", "prepaid"]

print(find_Longes_prefix(li))
