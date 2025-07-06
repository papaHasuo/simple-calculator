from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("simple-calculator")

@mcp.tool()
async def add(a: int, b: int) -> int:
    """二つの引数を足して返す関数

    Args:
        a: 足す数
        b: 足される数
    """
    return a+b

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
