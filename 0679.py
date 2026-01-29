text = "   Python   this   is   very   cool   "
words = text.split("   ")
words.pop(0); words.pop(-1)
print(words)
print(" ".join(words))
print("_".join(words))
print(" ".join(words).lower())