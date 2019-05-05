def getImagePath(mh_info):
    base = 'https://mhpic.manhualang.com/comic/'
    aim = mh_info['imgpath']
    flag = ord('N') - ord(aim[0])
    one_result = ''
    result =[]
    for one_char in aim:
        one_result += chr(ord(one_char) + flag)
    one_result = base + one_result
    for n in range(1, mh_info['totalimg']):
        result.append(one_result + str(n) + '.' + mh_info['image_suffix'] + mh_info['comic_size'] + '.webp')
    return result


# from GetMhInfo import getMhInfo
# url = "https://www.manhuatai.com/nitianxieshen/60.html"
# print(getImagePath(getMhInfo(url)))






