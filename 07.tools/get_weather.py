from langchain.tools import tool
from pydantic import SecretStr
import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)


@tool
def get_weather_by_city(city_name="Hefei") -> str:
    """
    获取指定城市的天气信息
    city_name: 城市名称，默认为 Hefei，需要求提供英文名称
    返回天气描述和温度信息
    """
    api_key = SecretStr(os.environ["OPEN_WEATHER_API_KEY"]).get_secret_value()
    print(f"Fetching weather data for {city_name}...\n")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}\
        &appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"{city_name}的天气是{weather_desc}，温度是{temp}°C。"
    else:
        print(f"Error fetching weather data: {response.status_code} \
              - {response.text}")
        return f"无法获取{city_name}的天气信息，请检查城市名称或API密钥是否正确。"


if __name__ == "__main__":
    weather_info = get_weather_by_city.invoke({})
    print(weather_info)
