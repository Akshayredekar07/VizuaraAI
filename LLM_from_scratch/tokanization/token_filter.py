
result = ['Hello', ',', '', ' ', 'world', '.', '', ' ', 'This', ',', '', ' ', 'is', ' ', 'a', ' ', 'test', '.', '']
result = [item for item in result if item.strip()]
print(result)

# Dry Run:
# Input List: ['Hello', ',', '', ' ', 'world', '.', '', ' ', 'This', ',', '', ' ', 'is', ' ', 'a', ' ', 'test', '.', '']
# Step 1: Filter items with item.strip()
# - 'Hello' -> 'Hello' (kept)
# - ',' -> ',' (kept)
# - '' -> '' (filtered out)
# - ' ' -> '' (filtered out)
# - 'world' -> 'world' (kept)
# - '.' -> '.' (kept)
# - '' -> '' (filtered out)
# - ' ' -> '' (filtered out)
# - 'This' -> 'This' (kept)
# - ',' -> ',' (kept)
# - '' -> '' (filtered out)
# - ' ' -> '' (filtered out)
# - 'is' -> 'is' (kept)
# - ' ' -> '' (filtered out)
# - 'a' -> 'a' (kept)
# - ' ' -> '' (filtered out)
# - 'test' -> 'test' (kept)
# - '.' -> '.' (kept)
# - '' -> '' (filtered out)
# Output: ['Hello', ',', 'world', '.', 'This', ',', 'is', 'a', 'test', '.']

# The list comprehension [item for item in result if item.strip()] creates a new list by iterating over each item in result.
# item.strip() removes leading and trailing whitespace from each item.
# The if item.strip() condition keeps only items where item.strip() is non-empty (i.e., it filters out empty strings and strings containing only whitespace).