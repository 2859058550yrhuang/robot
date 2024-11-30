import requests
import time
import json
from datetime import datetime, timedelta
from pprint import pprint


def get_timestamp():
    return time.strftime("%Y-%m-%d", time.localtime())


# city
def get_weather(city_id="101280601"):
    url = "http://t.weather.sojson.com/api/weather/city/"
    response = requests.get(url + city_id)
    data = response.json()

    if data["status"] == 200:
        city = "".join([data["cityInfo"]["parent"], data["cityInfo"]["city"]])
        high_temperature = data["data"]["forecast"][0]["high"]
        low_temperature = data["data"]["forecast"][0]["low"]
        weather = data["data"]["forecast"][0]["type"]
        suggestion = data["data"]["forecast"][0]["notice"] + "~"
        return city, high_temperature, low_temperature, weather, suggestion
    else:
        return "Error"


def after_day_info(after_day):
    from datetime import datetime, timedelta


def after_day_info(after_day):
    current_datetime = datetime.now()
    wanted_day = current_datetime + timedelta(days=after_day)
    return wanted_day.strftime("%Y-%m-%d")


def get_otherday_temperature(day_after, city_id="101280601"):
    url = "http://t.weather.sojson.com/api/weather/city/"
    response = requests.get(url + city_id)
    data = response.json()
    if data["status"] == 200:
        high_temperature = data["data"]["forecast"][day_after]["high"]
        high_temperature = high_temperature.split(" ")[1]
        low_temperature = data["data"]["forecast"][day_after]["low"]
        low_temperature = low_temperature.split(" ")[1]
        high_temperature = high_temperature.split("℃")[0]
        low_temperature = low_temperature.split("℃")[0]
    return int(high_temperature), int(low_temperature)


def get_inspirational_quotes():
    url = "http://open.iciba.com/dsapi/"
    response = requests.get(url=url)
    json_s = json.loads(response.text)
    quota = json_s.get("content")
    return quota


def hot_point_event():
    # url = 'https://api.vvhan.com/api/hotlist/toutiao'
    url = "https://api.vvhan.com/api/hotlist/wbHot"
    response = requests.get(url)
    json_s = json.loads(response.text)
    if json_s["success"] is True:
        data = json_s["data"]
        events = {
            "event1": {
                "title": data[0]["title"],
                "url": data[0]["url"],
            },
            "event2": {
                "title": data[1]["title"],
                "url": data[1]["url"],
            },
            "event3": {
                "title": data[2]["title"],
                "url": data[2]["url"],
            },
            "event4": {
                "title": data[3]["title"],
                "url": data[3]["url"],
            },
            "event5": {
                "title": data[4]["title"],
                "url": data[4]["url"],
            },
        }
        return events
    else:
        return "Error"


def product_history():
    url = "https://api.vvhan.com/api/hotlist/woShiPm"
    response = requests.get(url)
    json_s = json.loads(response.text)
    if json_s["success"] is True:
        data = json_s["data"]
        events = {
            "event1": {
                "title": data[0]["title"],
                "url": data[0]["url"],
            },
            "event2": {
                "title": data[1]["title"],
                "url": data[1]["url"],
            },
            "event3": {
                "title": data[2]["title"],
                "url": data[2]["url"],
            },
            "event4": {
                "title": data[3]["title"],
                "url": data[3]["url"],
            },
            "event5": {
                "title": data[4]["title"],
                "url": data[4]["url"],
            },
        }
        return events
    else:
        return "Error"


def get_bilibili_video():
    url = "https://api.vvhan.com/api/hotlist/bili"
    response = requests.get(url)
    json_s = json.loads(response.text)
    if json_s["success"] is True:
        data = json_s["data"]
        events = {
            "event1": {
                "title": data[0]["title"],
                "url": data[0]["url"],
            },
            "event2": {
                "title": data[1]["title"],
                "url": data[1]["url"],
            },
            "event3": {
                "title": data[2]["title"],
                "url": data[2]["url"],
            },
            "event4": {
                "title": data[3]["title"],
                "url": data[3]["url"],
            },
            "event5": {
                "title": data[4]["title"],
                "url": data[4]["url"],
            },
        }
        return events
    else:
        return "Error"


def love_quota():
    url = "https://api.vvhan.com/api/text/love"
    response = requests.get(url)
    return response.text


city_id = "101281701"  # 中山
city_id = "101280601"  # 深圳
user_id = "7395756060067282947"
email = "2859058550@qq.com"
Timestamp = time.strftime("%Y-%m-%d", time.localtime())
city, high_temperature, low_temperature, weather, suggestion = get_weather(
    city_id=city_id
)
content = "- [{}]({})\n".format(
    hot_point_event()["event1"]["title"], hot_point_event()["event1"]["url"]
)
content += "- [{}]({})\n".format(
    hot_point_event()["event2"]["title"], hot_point_event()["event2"]["url"]
)
content += "- [{}]({})\n".format(
    hot_point_event()["event3"]["title"], hot_point_event()["event3"]["url"]
)
content += "- [{}]({})\n".format(
    hot_point_event()["event4"]["title"], hot_point_event()["event4"]["url"]
)
content += "- [{}]({})\n".format(
    hot_point_event()["event5"]["title"], hot_point_event()["event5"]["url"]
)

product_content = "- [{}]({})\n".format(
    product_history()["event1"]["title"], product_history()["event1"]["url"]
)
product_content += "- [{}]({})\n".format(
    product_history()["event2"]["title"], product_history()["event2"]["url"]
)
product_content += "- [{}]({})\n".format(
    product_history()["event3"]["title"], product_history()["event3"]["url"]
)
product_content += "- [{}]({})\n".format(
    product_history()["event4"]["title"], product_history()["event4"]["url"]
)
product_content += "- [{}]({})\n".format(
    product_history()["event5"]["title"], product_history()["event5"]["url"]
)

bilibili_content = "- [{}]({})\n".format(
    get_bilibili_video()["event1"]["title"], get_bilibili_video()["event1"]["url"]
)
bilibili_content += "- [{}]({})\n".format(
    get_bilibili_video()["event2"]["title"], get_bilibili_video()["event2"]["url"]
)
bilibili_content += "- [{}]({})\n".format(
    get_bilibili_video()["event3"]["title"], get_bilibili_video()["event3"]["url"]
)
bilibili_content += "- [{}]({})\n".format(
    get_bilibili_video()["event4"]["title"], get_bilibili_video()["event4"]["url"]
)
bilibili_content += "- [{}]({})\n".format(
    get_bilibili_video()["event5"]["title"], get_bilibili_video()["event5"]["url"]
)


def send_lark_message(user_id="7395756060067282947"):
    # bytedance
    # url = "https://open.larkoffice.com/open-apis/bot/v2/hook/b5e6da3b-547a-4ba7-ac81-9c41ed610013"
    # myown
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/47f539d3-99bc-4bf1-aa49-ad6a26b6205f"

    # final
    # url = 'https://open.feishu.cn/open-apis/bot/v2/hook/8f52c3b6-1d0e-4d7c-9a36-0c6ef952a3c8'
    headers = {"Content-Type": "application/json"}
    data = {
        "msg_type": "interactive",
        "card": {
            "config": {"update_multi": True},
            "i18n_elements": {
                "zh_cn": [
                    {
                        "tag": "column_set",
                        "flex_mode": "none",
                        "horizontal_spacing": "8px",
                        "horizontal_align": "left",
                        "columns": [
                            {
                                "tag": "column",
                                "width": "weighted",
                                "vertical_align": "top",
                                "elements": [
                                    {
                                        "tag": "column_set",
                                        "flex_mode": "none",
                                        "horizontal_spacing": "default",
                                        "background_style": "default",
                                        "columns": [
                                            {
                                                "tag": "column",
                                                "elements": [
                                                    {
                                                        "tag": "div",
                                                        "text": {
                                                            "tag": "plain_text",
                                                            "content": f"{Timestamp}：{city}天气如下\n最高气温：{high_temperature}\n最低气温：{low_temperature}\n天气状况：{weather}\n{suggestion}",
                                                            "text_size": "normal",
                                                            "text_align": "left",
                                                            "text_color": "grey",
                                                        },
                                                        "icon": {
                                                            "tag": "standard_icon",
                                                            "token": "collect_filled",
                                                            "color": "black",
                                                        },
                                                    }
                                                ],
                                                "width": "weighted",
                                                "weight": 1,
                                            }
                                        ],
                                    }
                                ],
                                "weight": 1,
                            }
                        ],
                        "margin": "16px 0px 0px 0px",
                    },
                    {
                        "tag": "column_set",
                        "flex_mode": "none",
                        "horizontal_spacing": "default",
                        "background_style": "default",
                        "columns": [
                            {
                                "tag": "column",
                                "elements": [
                                    {
                                        "tag": "div",
                                        "text": {
                                            "tag": "plain_text",
                                            "content": "近五天的天气变化如下，要注意天气变化噢～",
                                            "text_size": "normal",
                                            "text_align": "left",
                                            "text_color": "grey",
                                        },
                                        "icon": {
                                            "tag": "standard_icon",
                                            "token": "collect_filled",
                                            "color": "grey",
                                        },
                                    }
                                ],
                                "width": "weighted",
                                "weight": 1,
                            }
                        ],
                    },
                    {
                        "tag": "chart",
                        "chart_spec": {
                            "type": "line",
                            "title": {"text": "天气变化趋势图"},
                            "data": {
                                "values": [
                                    {
                                        "type": "最高温度",
                                        "day": Timestamp,
                                        "value": get_otherday_temperature(0)[0],
                                    },
                                    {
                                        "type": "最高温度",
                                        "day": after_day_info(1),
                                        "value": get_otherday_temperature(1)[0],
                                    },
                                    {
                                        "type": "最高温度",
                                        "day": after_day_info(2),
                                        "value": get_otherday_temperature(2)[0],
                                    },
                                    {
                                        "type": "最高温度",
                                        "day": after_day_info(3),
                                        "value": get_otherday_temperature(3)[0],
                                    },
                                    {
                                        "type": "最高温度",
                                        "day": after_day_info(4),
                                        "value": get_otherday_temperature(4)[0],
                                    },
                                    {
                                        "type": "最低温度",
                                        "day": Timestamp,
                                        "value": get_otherday_temperature(0)[1],
                                    },
                                    {
                                        "type": "最低温度",
                                        "day": after_day_info(1),
                                        "value": get_otherday_temperature(1)[1],
                                    },
                                    {
                                        "type": "最低温度",
                                        "day": after_day_info(2),
                                        "value": get_otherday_temperature(2)[1],
                                    },
                                    {
                                        "type": "最低温度",
                                        "day": after_day_info(3),
                                        "value": get_otherday_temperature(3)[1],
                                    },
                                    {
                                        "type": "最低温度",
                                        "day": after_day_info(4),
                                        "value": get_otherday_temperature(4)[1],
                                    },
                                ]
                            },
                            "xField": ["day", "type"],
                            "yField": "value",
                            "seriesField": "type",
                            "legends": {"visible": True, "orient": "bottom"},
                        },
                        "preview": True,
                        "color_theme": "brand",
                        "height": "auto",
                    },
                    {
                        "tag": "column_set",
                        "flex_mode": "none",
                        "horizontal_spacing": "default",
                        "background_style": "default",
                        "columns": [
                            {
                                "tag": "column",
                                "elements": [
                                    {
                                        "tag": "div",
                                        "text": {
                                            "tag": "plain_text",
                                            "content": "",
                                            "text_size": "normal",
                                            "text_align": "left",
                                            "text_color": "default",
                                        },
                                    }
                                ],
                                "width": "weighted",
                                "weight": 1,
                            }
                        ],
                    },
                    {
                        "tag": "column_set",
                        "flex_mode": "none",
                        "horizontal_spacing": "default",
                        "background_style": "default",
                        "columns": [
                            {
                                "tag": "column",
                                "elements": [
                                    {
                                        "tag": "div",
                                        "text": {
                                            "tag": "plain_text",
                                            "content": "今日社会热点",
                                            "text_size": "normal",
                                            "text_align": "left",
                                            "text_color": "grey",
                                        },
                                        "icon": {
                                            "tag": "standard_icon",
                                            "token": "collect_filled",
                                            "color": "grey",
                                        },
                                    }
                                ],
                                "width": "weighted",
                                "weight": 1,
                            }
                        ],
                    },
                    {
                        "tag": "markdown",
                        "content": content,
                        "text_align": "left",
                        "text_size": "normal",
                    },
                    {
                        "tag": "column_set",
                        "flex_mode": "none",
                        "horizontal_spacing": "default",
                        "background_style": "default",
                        "columns": [
                            {
                                "tag": "column",
                                "elements": [
                                    {
                                        "tag": "div",
                                        "text": {
                                            "tag": "plain_text",
                                            "content": "产品经理热文日榜",
                                            "text_size": "normal",
                                            "text_align": "left",
                                            "text_color": "grey",
                                        },
                                        "icon": {
                                            "tag": "standard_icon",
                                            "token": "collect_filled",
                                            "color": "grey",
                                        },
                                    }
                                ],
                                "width": "weighted",
                                "weight": 1,
                            }
                        ],
                    },
                    {
                        "tag": "markdown",
                        "content": product_content,
                        "text_align": "left",
                        "text_size": "normal",
                    },
                    {
                        "tag": "column_set",
                        "flex_mode": "none",
                        "horizontal_spacing": "default",
                        "background_style": "default",
                        "columns": [
                            {
                                "tag": "column",
                                "elements": [
                                    {
                                        "tag": "div",
                                        "text": {
                                            "tag": "plain_text",
                                            "content": "Bilibili热榜",
                                            "text_size": "normal",
                                            "text_align": "left",
                                            "text_color": "grey",
                                        },
                                        "icon": {
                                            "tag": "standard_icon",
                                            "token": "collect_filled",
                                            "color": "grey",
                                        },
                                    }
                                ],
                                "width": "weighted",
                                "weight": 1,
                            }
                        ],
                    },
                    {
                        "tag": "markdown",
                        "content": bilibili_content,
                        "text_align": "left",
                        "text_size": "normal",
                    },
                    #####
                ]
            },
            "i18n_header": {
                "zh_cn": {
                    "title": {
                        "tag": "lark_md",
                        "content": f"<at id=all></at>  姐姐下午好～{love_quota()}",
                    },
                    "subtitle": {
                        "tag": "plain_text",
                        "content": f"{get_inspirational_quotes()}",
                    },
                    "template": "indigo",
                    "ud_icon": {"tag": "standard_icon", "token": "like_filled"},
                }
            },
        },
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())


if __name__ == "__main__":
    send_lark_message()
