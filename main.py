from fastmcp import FastMCP
import math

# Initialize the FastMCP server
mcp = FastMCP("Math Server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Calculate base raised to the power of exponent."""
    return math.pow(base, exponent)

@mcp.tool()
def square_root(x: float) -> float:
    """Calculate the square root of a non-negative number."""
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(x)

@mcp.tool()
def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    return math.factorial(n)

if __name__ == "__main__":
    mcp.run()