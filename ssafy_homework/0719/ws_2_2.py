# @#~I NeVErDrEamEdAbouTSuCCeSs, i woRkEdfoR iT.!>!

s = input()

s = s.replace("~", "").replace("@", "").replace("#", "").replace("$", "").replace("!", "").replace(">", "")
s = s[0].upper() + s[1:].lower()
print(s)