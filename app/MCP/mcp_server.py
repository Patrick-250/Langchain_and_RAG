import wikipedia

from mcp.server.fastmcp import FastMCP

mcp=FastMCP()

@mcp.tool()
def wikipedia_search(query:str)->str:
    try:
        return wikipedia.summary(query,sentences=2)
    except Exception as e:
        return "Error happend on my end"
@mcp.tool()
def get_me(name:str)->str:
    if name=="Patrick Rumanzi":
        return """
         Software Engineer with experience delivering scalable, secure, and high performing systems. Interested
in AI/ML and data engineering, passionate about figuring out how things work and enjoy using tech to
solve real business problems. With experience from Tech companies including Scale AI, HCLTech and
others, thrive on solving complex problems and making real differences. Also, passionate about
continuous learning- especially in the exciting world of AI- and enjoy mentoring and helping others to
foster growth and innovation. Enjoy contributing to different open-source Repositories that mostly
resonate with me. My current role as Senior Technical lead at HCLTECH provided the opportunity to
manage cross-functional teams to deliver large scale solutions. Open to volunteering for Gender equality,
Animal welfare and environment sustainabilitySoftware Engineer with experience delivering scalable, secure, and high performing systems. Interested
in AI/ML and data engineering, passionate about figuring out how things work and enjoy using tech to
solve real business problems. With experience from Tech companies including Scale AI, HCLTech and
others, thrive on solving complex problems and making real differences. Also, passionate about
continuous learning- especially in the exciting world of AI- and enjoy mentoring and helping others to
foster growth and innovation. Enjoy contributing to different open-source Repositories that mostly
resonate with me. My current role as Senior Technical lead at HCLTECH provided the opportunity to
manage cross-functional teams to deliver large scale solutions. Open to volunteering for Gender equality,
Animal welfare and environment sustainability
        """
    else:
        return None
if __name__ == "__main__":
    print("MCP SERVER started")
    mcp.run(transport="streamable-http")
