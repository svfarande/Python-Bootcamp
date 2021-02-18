import re

text = "I have mobile. And my mobile no. is 1234567890"
pattern = "mobile"

print(pattern in text)  # True
# re.search(pattern, text) will always give span of 1st match
print(re.search(pattern, text))  # <re.Match object; span=(7, 13), match='mobile'>
print(re.search(pattern + "garbage", text))  # None # as that is not in text

search_result = re.search(pattern, text)
print(f"Pattern - \"{pattern}\" in Text - \"{text}\" is at {search_result.span()} -> from index"
      f" {search_result.start()} to {search_result.end()}")
# Pattern - "mobile" in Text - "I have mobile. And my mobile no. is 1234567890" is at
# (7, 13) -> from index 7 to 13

print(re.findall(pattern, text))   # ['mobile', 'mobile']

# finditer returns re.Match objects with span() for all matches
for i in re.finditer(pattern, text):
    print(f"{i} '{i.group()}'-> {i.span()} -> {i.start()} to {i.end()}")
