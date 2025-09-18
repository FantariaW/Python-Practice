import json           # 📦 匯入 json 模組，用來格式化輸出（選擇性使用）
import requests       # 🌐 匯入 requests 模組，發送網路請求
import sys            # 🖥️ 匯入 sys 模組，接收終端輸入參數

# 🛑 檢查使用者是否有輸入搜尋關鍵字（例如 python music.py Taylor）
if len(sys.argv) != 2:
    sys.exit("請提供搜尋的歌曲關鍵字！")

# 🌍 發送 GET 請求到 iTunes API，查詢歌曲資料（最多 50 首）
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# # 🧊（可選）將回應內容轉為漂亮的 JSON 格式印出來～方便觀察結構
# print(json.dumps(response.json(), indent=2))

# 🧠 將回傳結果轉為 dict 並命名為 o_dict（常見縮寫 o - object）
o_dict = response.json()
# 📑 遍歷 o 中的 "results" 清單（每一項都是一首歌的 dict）, each_dict就是一整個dict
for each_result in o_dict["results"]:
    print(each_result["trackName"])  # 打印出 dict - each_dict 裏對應 key - "trackName" 的值 🎵 印出每首歌的名稱（key: "trackName"）
