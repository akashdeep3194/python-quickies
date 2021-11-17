print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        BODY = input()
    except EOFError:
        break
    contents.append(BODY)

print(contents)
