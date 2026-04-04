print(" 星座判斷程式 ")
print(" 請輸入生日資訊，程式將輸出對應星座與特質 ")
print("\n -------- Input Block -------- ")

My_Birthday = input("請輸入生日 YYYYMMDD : ")

print("\n ------- Output Block --------- ")

My_Year = My_Birthday[:4]
My_Month = My_Birthday[4:6]
My_Day = My_Birthday[6:]

Year = int(My_Birthday[:4])  # 為了判斷平年閏年
if Year % 400 == 0:
    print(Year,"年為閏年")
elif Year % 100 == 0:
    print(Year,"年為平年")
elif Year % 4 == 0:
    print(Year,"年為閏年")
else :
    print(Year,"年為平年")

if (My_Month >= "01" and My_Month <= "12") and (My_Day >= "01" and My_Day <= "31"):
    # 水瓶座
    if (My_Month == "01" and My_Day >= "20") or (My_Month == "02" and My_Day <= "18"):
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("水瓶座")
        print("星座特質:", "水瓶座是特立獨行的思考家，他們的腦袋光一個念頭就可以好幾千轉，每分每秒都在為自己的想像世界重組、毀棄、翻新。他們擁有取之不竭用之不盡的靈感，又能堅持保有自己的風格。適合的工作：廣告設計、創新研發、編劇、企劃。")
    # 雙魚座
    elif (My_Month == "02" and My_Day >= "19") or (My_Month == "03" and My_Day <= "20") :
        # 如果是 2 月，需根據是否為閏年來檢查日期是否超過 28 或 29 天
        if My_Month == "02":
            # 閏年判斷邏輯
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
                print("星座特質:", "特別愛幻想的魚兒，有顆柔軟善感的心。他們擅長敘述一些貼近人心的道理，語辭溫和卻有力，足以撼動人心，他們又擁有豐富的想像力，在現實中很容易找到特殊靈感。非常適合當藝術家、演員、詩人、畫家、美術設計等。")
            else:
                print("輸入錯誤")

        # 如果是 3 月，1~20 號都是合法的雙魚座範圍
        else:
            print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
            print("星座: 雙魚座")
            print("星座特質:", "特別愛幻想的魚兒，有顆柔軟善感的心。他們擅長敘述一些貼近人心的道理，語辭溫和卻有力，足以撼動人心，他們又擁有豐富的想像力，在現實中很容易找到特殊靈感。非常適合當藝術家、演員、詩人、畫家、美術設計等。")
    # 牡羊座
    elif (My_Month == "03" and My_Day >= "21") or (My_Month == "04" and My_Day <= "19") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 牡羊座")
        print("星座特質:", "勇氣與活力滿檔，是老天給予牡羊的天賦。為了達成夢想，牡羊永遠燃燒著熱情，是敢衝敢做的冒險家。不管前方有多少險阻，羊兒都能越挫越勇，因此相當適合開疆闢土、在新領域成為先驅、或擔任第一線工作，像是：銷售人員、保險業務、市場開發、業務拓展、軍警人員等。")
    # 金牛座
    elif (My_Month == "04" and My_Day >= "20") or (My_Month == "05" and My_Day <= "20") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 金牛座")
        print("星座特質:", "個性溫和、遇事沉著、對於金錢與美好的事物高度敏感，是金牛與生俱來的天賦。因此，理財方面的工作，或是與美感、美食相關的工作，都能讓金牛大展身手。適合工作：廚師、美食評論家、服裝設計師、理財專家、保險從業人員。")
    # 雙魚座
    elif (My_Month == "05" and My_Day >= "21") or (My_Month == "06" and My_Day <= "20") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 雙子座")
        print("星座特質:", "上天給予雙子座非常優渥的天賦。他們不但創意十足、幽默風趣，凡事抱持好奇心，更有絕佳的表演天分，因此社交魅力十足，是交際場上的風雲人物。又在收集與傳遞訊息方面相當有一手，很適合從事與新聞傳播、講師、演說家、行銷相關方面的工作。")
    # 巨蟹座
    elif (My_Month == "06" and My_Day >= "21") or (My_Month == "07" and My_Day <= "22") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 巨蟹座")
        print("星座特質:", "擁有細膩情感、喜歡帶給他人溫暖的巨蟹座，善感與貼近人心就是他們的天賦。由於特別容易感受他人情緒，他們對生活周遭人事物總是洞察細微，因此十分適合從事與人相關的工作，例如：人資、行政事務、心理諮商師、教師、個人工作室等。")
    # 獅子座
    elif (My_Month == "07" and My_Day >= "23") or (My_Month == "08" and My_Day <= "22") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 獅子座")
        print("星座特質:", "獅子擁有領導風範、群眾魅力，只要站在自己的舞台上，便能夠一呼百諾。上天給了他們驚人的天賦，讓他們得以靠著旺盛的企圖心，不斷朝目標前進，又能以熱情與雄心壯志掌控全局。適合的工作：老闆、政治家、主持人、公司高層、導演。")
    # 處女座
    elif (My_Month == "08" and My_Day >= "23") or (My_Month == "09" and My_Day <= "22") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 處女座")
        print("星座特質:", "要求細節、追求完美，又有與生俱來的學習力與聰明頭腦，這便是處女的天賦。他們善於分析與歸納，在處理過程中有自己的一套邏輯，因此，與研究或分析有關的工作，處女座是不二人選。適合的工作包括：分析師、研究員、藥師、品管師等。")
    # 天秤座
    elif (My_Month == "09" and My_Day >= "23") or (My_Month == "10" and My_Day <= "22") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 天秤座")
        print("星座特質:", "天秤最驚人的天賦是絕佳的協調與溝通能力。他們能在與人交往中吸取對方經驗，內化並衍生出自己的觀點，因此總是顯得博學多聞，且強烈發散出個人魅力，這特質能吸引各種不同領域的好友。適合的工作：服務業、公關、行銷、藝術工作者、美容美髮業、服裝設計師、攝影師等。")
    # 天蠍座
    elif (My_Month == "10" and My_Day >= "23") or (My_Month == "11" and My_Day <= "21") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 天蠍座")
        print("星座特質:", "絕頂聰明的天蠍，天生就內建第六感與直覺。他們對於人性觀察入微，可說是人性探測器；又對人生異常豁達，因此遇事格外沉著冷靜。這便是上天給予蠍子的特別天賦。適合的工作：醫師、護理人員、醫療儀器操作員、偵探、法官、藥劑師等。")
    # 射手座
    elif (My_Month == "11" and My_Day >= "22") or (My_Month == "12" and My_Day <= "21") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 射手座")
        print("星座特質:", "自由奔放的射手，最大天賦就是那海闊天空的胸襟。朝九晚五的工作無法滿足射手那豪放不羈的心；不愛受束縛的他們，一心想要感受美好世界、以及與人結交的歡樂氣氛。適合的工作：機師、飛行員、國際貿易、導遊、作家、自由業、代購。")
    # 摩羯座
    elif (My_Month == "12" and My_Day >= "22") or (My_Month == "01" and My_Day <= "19") :
        print("出生日期為:", My_Year ,"年", My_Month,"月", My_Day,"日" )
        print("星座: 摩羯座")
        print("星座特質:", "認真、嚴謹、實事求是，把吃苦當作吃補，就是摩羯的驚人天賦！所謂「吃得苦中苦，方為人上人」，這句話用在摩羯是再適合也不過了。天生的毅力與決心，使他們為了達到心目中的夢想，就算遇到挫折也能咬牙撐過去，永遠認真往前走。適合的工作：法官、公務人員、高階主管、房地產人員。")
else :
    print("輸入錯誤")

print("\n ------- 額外實作 --------- ")
Life_Path_Number = int(My_Year[:1]) + int(My_Year[1:2]) + int(My_Year[2:3]) + int(My_Year[3:4]) + int(My_Month[:1]) + int(My_Month[1:2]) + int(My_Day[:1]) + int(My_Day[1:2])

print("生命靈數:", Life_Path_Number)