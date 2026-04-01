print(" 星座判斷程式 ")
print(" 請輸入生日資訊，程式將輸出對應星座與特質 ")
print("\n -------- Input Block -------- ")
My_Birthday = input("請輸入生日 YYYYMMDD : ")

print("\n ------- Output Block --------- ")
My_Year = My_Birthday[:4]
My_Month = My_Birthday[4:6]
My_Day = My_Birthday[6:]

Year = int(My_Birthday[:4])  # 為了判斷平年閏年


# 1. 月份日期是否出入正確
if (My_Month >= "01" and My_Month <= "12") and (My_Day >= "01" and My_Day <= "31"):
    # 2. 星座判斷
    if (My_Month == "01" and My_Day >= "20") or (My_Month == "02" and My_Day <= "18"):
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("水瓶座")
    elif (My_Month == "02" and My_Day >= "19") or (My_Month == "03" and My_Day <= "20") :
        # 如果是 2 月，需根據是否為閏年來檢查日期是否超過 28 或 29 天
        if My_Month == "02":
            # 整合 year.py 的閏年判斷邏輯
            is_leap = False
            if Year % 400 == 0:
                is_leap = True
            elif Year % 100 == 0:
                is_leap = False
            elif Year % 4 == 0:
                is_leap = True
            
            # 根據閏年狀態決定 2 月最大天數
            max_feb_days = 29 if is_leap else 28
            
            # 判斷輸入的天數是否合理
            if int(My_Day) <= max_feb_days:
                print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
                print("星座: 雙魚座")
            else:
                print("輸入錯誤")
        
        # 如果是 3 月，1~20 號都是合法的雙魚座範圍
        else:
            print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
            print("星座: 雙魚座")
    elif (My_Month == "03" and My_Day >= "21") or (My_Month == "04" and My_Day <= "19") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 牡羊座")
    elif (My_Month == "04" and My_Day >= "20") or (My_Month == "05" and My_Day <= "20") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 金牛座")
    elif (My_Month == "05" and My_Day >= "21") or (My_Month == "06" and My_Day <= "21") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 雙子座")
    elif (My_Month == "06" and My_Day >= "22") or (My_Month == "07" and My_Day <= "22") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 巨蟹座")
    elif (My_Month == "07" and My_Day >= "23") or (My_Month == "08" and My_Day <= "22") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 獅子座")
    elif (My_Month == "08" and My_Day >= "23") or (My_Month == "09" and My_Day <= "22") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 處女座")
    elif (My_Month == "09" and My_Day >= "23") or (My_Month == "10" and My_Day <= "23") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 天秤座")
    elif (My_Month == "10" and My_Day >= "24") or (My_Month == "11" and My_Day <= "22") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 天蠍座")
    elif (My_Month == "11" and My_Day >= "23") or (My_Month == "12" and My_Day <= "21") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 射手座")
    elif (My_Month == "12" and My_Day >= "22") or (My_Month == "01" and My_Day <= "19") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 摩羯座")
else :
    print("輸入錯誤")
