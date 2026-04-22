def get_zodiac(year):
    # 推薦寫法：
    idx = (year - 4) % 12
    zodiac_order = ('鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗', '豬')
    return zodiac_order[idx]

# 測試
year = int(input("請輸入年份: "))
print(f"{year}年是{get_zodiac(year)}年")
