f = open("testcss/test.css", "rt")
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
comment = ""
index = 0
for l in oneLine:
    # class type
    if l == "{":
        word = word.rstrip().replace(" ", "|")
        wholeCss.append([word])
        wholeCss[count].append([])
        before = word
        word = ""
        flag = 1

    word += l

    if l == "/" and oneLine[index + 1] == "*":
        comment_flag = 1
    elif l == "/" and oneLine[index - 1] == "*":
        comment = word.replace(" ","").replace("{","")
        if flag == 1:
            wholeCss[count][1].append(comment)
        if flag == 0:
            wholeCss.append([word])
            count += 1
        comment = ""
        word = ""
        flag = 1

    if flag == 1:
        if l == ";":
            word= word.replace(" ", "").replace("{","")
            wholeCss[count][1].append(word)
            word=""
        if l == "}":
            word = ""
            flag = 0
            count += 1
    index += 1

for i in range(0, len(wholeCss)):
    print(wholeCss[i])

f.close()
