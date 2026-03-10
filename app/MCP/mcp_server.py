
from mcp.server.fastmcp import FastMCP
mcp=FastMCP()

@mcp.tool()
def make_reservation():
    
    """
    use this tool when you need to make a reservation for a specific restaurant
    """
    return """ I booked a reservationa dn sent you a confirmation email"""


if __name__ == "__main__":
    print("MCP SERVER started")
    mcp.run(transport="streamable-http")
