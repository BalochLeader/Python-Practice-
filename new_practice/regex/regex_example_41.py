# Regular Expression Example 41
# This program demonstrates basic regex matching.

import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"

match = re.search(pattern, text)
if match:
    print(f"Pattern '{pattern}' found in text at position {match.start()}")
else:
    print(f"Pattern '{pattern}' not found.")

pattern_all = r"o"
matches_all = re.findall(pattern_all, text)
print(f"All occurrences of '{pattern_all}': {matches_all}")
