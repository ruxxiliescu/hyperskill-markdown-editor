command = ""
formatters = ['plain',  'bold', 'italic', 'header',
              'link',  'inline-code', 'new-line',
              'ordered-list', 'unordered-list']
levels = [1, 2, 3, 4, 5, 6]
final_str = ""


def ordered_list(c):
    f_string = ""
    while True:
        input_rows = int(input("Number of rows: "))
        if input_rows <= 0:
            print("he number of rows should be greater than zero")
            continue
        else:
            break
    if c == "ordered-list":
        txt = [str(i) + ". " + input(f"Row #{i}: ")
               for i in range(1, input_rows + 1)]
        f_string += "\n".join(txt) + "\n"
    elif c == "unordered-list":
        txt = ["* " + input(f"Row #{i}: ")
               for i in range(1, input_rows + 1)]
        f_string += "\n".join(txt) + "\n"
    return f_string


def headings():
    while True:
        input_level = int(input("Level: "))
        if input_level in levels:
            break
        else:
            print("The level should be within the range of 1 to 6")
            continue
    input_text = input("Text: ")
    f_string = f"{'#' * input_level} {input_text}\n"
    return f_string


def plain_text(input_text):
    f_string = input_text
    return f_string


def bold_text(input_text):
    f_string = f'**{input_text}**'
    return f_string


def italic_text(input_text):
    f_string = f'*{input_text}*'
    return f_string


def inline_code_text(input_text):
    f_string = f'`{input_text}`'
    return f_string


def newline():
    f_string = f'\n'
    return f_string


def link_text():
    input_label = input("Label: ")
    input_url = input("URL: ")
    f_string = f'[{input_label}]({input_url})'
    return f_string


while command != "!done":
    command = input("Choose a formatter: ")
    if command in formatters:
        if command == "header":
            level = ""
            final_str += headings()
            print(final_str)
        elif command == "link":
            label = ""
            url = ""
            final_str += link_text()
            print(final_str)
        elif command == "new-line":
            final_str += newline()
            print(final_str)
        elif command == "ordered-list" or command == "unordered-list":
            final_str += ordered_list(command)
            print(final_str)
        else:
            text = input("Text: ")
            if command == "plain":
                final_str += plain_text(text)
                print(final_str)
            elif command == "bold":
                final_str += bold_text(text)
                print(final_str)
            elif command == "italic":
                final_str += italic_text(text)
                print(final_str)
            elif command == "inline-code":
                final_str += inline_code_text(text)
                print(final_str)
    elif command == '!help':
        print('Available formatters:', *formatters, '\n', 'Special commands: !help !done')
    elif command == "!done":
        with open("output.md", 'w') as file:
            file.writelines(final_str.splitlines(keepends=True))
        break




