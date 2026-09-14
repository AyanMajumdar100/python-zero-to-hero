# TEXT SPLITTING BASED ON SIZE
def split_text(text, size=100):
    return [text[i:i + size] for i in range(0, len(text), size)]    # LIST

print(split_text("12312321321sadadasdasdasdas das dasd asdadas", 10))
print(type(split_text("12312321321sadadasdasdasdas das dasd asdadas", 10)))
# OUTPUT: ['1231232132', '1sadadasda', 'sdasdas da', 's dasd asd', 'adas']


for i in range(0, len("12312321321sadadasdasdasdas das dasd asdadas"), 10):
    print("12312321321sadadasdasdasdas das dasd asdadas"[i:i+10])
