from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")


@mcp.tool()
def get_weather(location: str) -> dict:
    """查询指定位置的天气, 如果是不存在的位置，告知位置不存在"""
    return {
        "location": str,
        "weather": "晴朗"
    }


@mcp.tool()
def create_vm(name: int, cpu: int, memory: int, disk: int) -> dict:
    """创建虚拟机"""
    return {
        "name": name,
        "status": "success"
    }


def main():
    print("Hello from mcp-demo!")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
