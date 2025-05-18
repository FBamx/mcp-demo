from typing import Any
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("demo")

WEATHER_API="https://restapi.amap.com/v3/weather/weatherInfo?key=91717c0b7f1fe503505132f141506211&city={}"

async def make_request(url: str) -> dict[str, Any] | None:
    headers = {
        "User-Agent": "weather-app/1.0",
        "Accept": "application/geo+json",
    }
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.json()
        except Exception:
            return None


@mcp.tool()
async def get_weather(location: str) -> dict:
    """
    查询指定位置的天气
    
    Args:
        location: 位置, 例如110000
    """

    url = WEATHER_API.format(location)
    data = await make_request(url=url)
    return data


@mcp.tool()
def create_vm(name: int, cpu: int, memory: int, disk: int) -> dict:
    """
    创建虚拟机

    Args:
        name: 虚拟机名称，不支持中文
        cpu: cpu核数,不能超过8核心
        memory: 内存大小, 不能超过16G
        disk: 硬盘大小,不能超过200G
    """
    return {
        "name": name,
        "status": "success"
    }


def main():
    print("Hello from mcp-demo!")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
