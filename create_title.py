def url_to_dashed_title(url):
    tokens = url.split('/')
    dashed_title = tokens[-2]
    return dashed_title

def dashed_to_title(url):
    tokens = url.split("-")
    tokens = [token.capitalize() for token in tokens]
    return ' '.join(tokens)

def TEST_dashed_to_title():
    input = "hi-ok-no-what"
    print(dashed_to_title(input))

# TEST_dashed_to_title()
# print (url_to_dashed_title('https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/'))