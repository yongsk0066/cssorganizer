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

# css file to one line string

lines = f.readlines()
oneLine = ""
for line in lines:
    oneLine += line

oneLine = oneLine.replace("\n", "")


# css parsing

def parseToList(c):
    func_word = ""
    func_list = []

    for l in c:
        func_word += l

        if l == "{":
            func_word = func_word.replace("{", "").strip()
            func_list.append(func_word)
            func_list.append([])
            func_word = ""
        if l == ";":
            func_word = func_word.replace("{", "").strip()
            func_list[1].append(func_word)
            func_word = ""

    return func_list


def getInsideString(c):
    media_word = ""
    shell = 0
    for i in c:
        if i == "}":
            shell -= 1
            if shell == 0:
                return media_word
        if shell != 0:
            media_word += i
        if i == "{":
            shell += 1


def getEach(oneLine):
    shell = 0
    word = ""
    result = []
    for l in oneLine:
        word += l
        if l == "{":
            shell += 1
        if l == "}":
            shell -= 1
            if shell == 0:
                escape = word
                result.append(escape)
                word = ""
    return result


# test_set = "@media ( max-width: 768px ) {body {color: red;color: red;}div {width: 100%;}}"
#
# b = []
# a = getInsideString(test_set)
# for i in getEach(a):
#     b.append(parseToList(i))
#
# print(b)
# print(getEach(test_set))
# # for i in cssList:
# #     print(i)
def returnList(oneLine):
    wholeCss = []
    word = ""
    flag = 0  # 0 : main,  1 : inside cover, 2 : secondary cover
    count = 0  # word count
    index = 0
    comment_flag = 0
    media_flag = 0
    media_count = 0
    inside_list = []
    base = []
    for l in oneLine:
        # style type append
        if l == "@":
            media_flag = 1
        if media_flag == 1:
            word += l
            if l == "{":
                media_count += 1
                if media_count == 1:
                    base = [word.replace("{", "").strip()]
            if l == "}":
                media_count -= 1
                if media_count == 0:
                    for i in getEach(getInsideString(word)):
                        inside_list.append(parseToList(i))
                    base.append(inside_list)
                    wholeCss.append(base)
                    count += 1
                    media_flag = 0
                    word = ""
        else:
            if l == "{":
                word = word.strip().replace(" ", "|").replace("{", "")
                wholeCss.append([word])
                wholeCss[count].append([])
                before = word
                word = ""
                flag = 1

            # word proceed
            word += l

            # comment flag
            if l == "/" and oneLine[index + 1] == "*":
                comment_flag = 1

            # comment close
            elif l == "/" and oneLine[index - 1] == "*":
                comment = word.replace(" ", "").replace("{", "")
                # inside comment append
                if flag == 1:
                    wholeCss[count][1].append(comment)
                # outside comment append
                if flag == 0:
                    wholeCss.append([word])
                    count += 1
                # reset flags
                comment = ""
                word = ""
                flag = 1
                comment_flag = 0

            # property (not comment)
            if flag == 1 and not comment_flag == 1:
                # property append
                if l == ";":
                    word = word.replace("{", "").strip()
                    wholeCss[count][1].append(word)
                    word = ""

                # reset flag and escape property
                if l == "}":
                    word = ""
                    flag = 0
                    count += 1
        index += 1
    return wholeCss


# test code


for i in returnList(oneLine):
    print(i)
# for i in range(0, len(wholeCss)):
#     print(wholeCss[i])

f.close()
