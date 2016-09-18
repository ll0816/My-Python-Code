# coding=utf-8
import HTMLParser, re

text = u"I luv my &lt;3 iphone &amp; you're awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com"

# 1. Escaping HTML characters

html_parser = HTMLParser.HTMLParser()
tweet = html_parser.unescape(text)
print tweet

# 2. Decoding data

tweet = text.encode('ascii', 'ignore')
print tweet

# 3. Apostrophe lookup

APPOSTOPHES = {u"he's" : "he is", u"'you're" : "you are"} ## Need a huge dictionary
words = str(tweet).split(" ")
print words
reformed = [APPOSTOPHES[word] if word in APPOSTOPHES else word for word in words]
reformed = " ".join(reformed)
print reformed

# 4. Removal of Stop-words

# 5. Removal of Punctuations

# 6. Removal of Expressions

# 7. Split Attached Words

cleaned = " ".join(re.findall('[A-Z][^A-Z]*', text))
print cleaned

# 8. Slangs lookup

# 9. Standardizing words

# 10. Removal of URLs