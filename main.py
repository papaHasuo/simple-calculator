from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("simple-calculator")

@mcp.tool()
async def add(a: int, b: int) -> str:
    """二つの引数を足して返す関数

    Args:
        a: 足す数
        b: 足される数
    """
    return "\n---\n".join([str(a), str(b), str(a + b)])

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
