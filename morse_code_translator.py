class morse:
    a = ".-"
    b = "-..."
    c = "-.-."
    d = "-.."
    e = "."
    f = "..-."
    g = "--."
    h = "...."
    i = ".."
    j = ".---"
    k = "-.-"
    l = ".-.."
    m = "--"
    n = "-."
    o = "---"
    p = ".--."
    q = "--.-"
    r = ".-."
    s = "..."
    t = "-"
    u = "..-"
    v = "...-"
    w = ".--"
    x = "-..-"
    y = "-.--"
    z = "--.."

    def translate(self, input):
        c = ""
        input = str.lower(input)
        for item in input:
            if item == " ":
                c = c + "/ "
            else:
                c = c + getattr(self, item) + " "
        print(c)

    def convert(self, arr):
        c = ""
        input = arr.split()
        for item in input:
            for attr_name in dir(self):
                attr_value = getattr(self, attr_name)
                if attr_value == item:
                    c = c + attr_name
                    break
                elif item == "/":
                    c = c + " "
                    break
                elif item == " ":
                    break
        print(c)


a = morse()
r = int(
    input(
        "Enter '1' to translate morse code into text and '2' to translate text into morse code: "
    )
)
if r == 1:
    inp = input("Enter the morse code to be translated: ")
    a.convert(inp)
elif r == 2:
    inp = input("Enter the string to be translated: ")
    a.translate(inp)
else:
    print("Invalid input. Please Try Again!")
