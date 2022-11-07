

digits = ["one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]
s9 = sum(map(len, digits))
assert sum(map(len, digits[:5])) == 19
s19 = s9 + len("ten" + "eleven" + "twelve" + "thirteen" + "fourteen" +
               "fifteen" + "sixteen" + "seventeen" + "eighteen" + "nineteen")


def tens(n):
    return n * 10 + s9


l = ["twenty", "thirty", "forty", "fifty",
     "sixty", "seventy", "eighty", "ninety"]
s99 = s19 + sum([tens(len(x)) for x in l])


def hundreds(n):
    return n + len("hundred") + (n + len("hundredand")) * 99 + s99


s999 = s99 + sum([hundreds(len(digit)) for digit in digits])
print(s999 + len("onethousand"))
