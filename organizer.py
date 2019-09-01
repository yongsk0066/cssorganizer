f = open("testcss/board_post_large.css", "rt")
replace_letter = [
    "\n",
    " ",
]
css_type = {
    ".": "class",
    "#": "id",
    "@": "media_query",
}

lines = f.readlines()
oneLine = ""
for line in lines:
    oneLine += line

# t = target.split(".")
# css file to one line string
oneLine = oneLine.replace("\n", "")

# css parsing
wholeCss = []
word = ""
flag = 0
count = 0

for l in oneLine:
    if l == "{":
        wholeCss.append([word])
        before = word
        word = ""
        flag = 1
    word += l
    if l == "}":
        word = word.replace(" ", "")
        wholeCss[count].append(word)
        word = ""
        flag = 0
        count += 1

for i in range(0, len(wholeCss)):
    print(wholeCss[i])

f.close()
