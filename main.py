from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("simple-calculator")

@mcp.tool()
async def add(a: int, b: int) -> int:
    """二つの引数を足して返す関数

    Args:
        a: 足される数
        b: 足す数
    """
    return a + b

@mcp.tool()
async def minus(a: int, b: int) -> int:
    """二つの引数を引いて返す関数

    Args:
        a: 引かれる数
        b: 引く数
    """
    return a - b

@mcp.tool()
async def multiply(a: int, b: int) -> int:
    """二つの引数を掛けて返す関数

    Args:
        a: 掛けられる数
        b: 掛ける数
    """
    return a * b

@mcp.tool()
async def divide(a: int, b: int) -> float:
    """二つの引数を割って返す関数

    Args:
        a: 割られる数
        b: 割る数
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
