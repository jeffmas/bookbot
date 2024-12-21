def count_words(txt):
    words = txt.split()
    return len(words)

def count_characters(txt):
    chr = {}
    for c in txt.lower():
        if c in chr:
            chr[c] += 1
        else:
            chr[c] = 1
    return chr

def generate_report(num_words, num_chars, path):
    def sort_on(dict):
        return dict["count"]
    
    report = "--- Begin report of " + path + " ---\n"
    report += f"{num_words} words found in the document\n\n"
    lst = []
    for char in num_chars:
        if char.isalpha():
            lst.append({"char":char, "count":num_chars[char]})
    lst.sort(reverse=True, key=sort_on)
    for i in lst:
        report += f"The '{i['char']}' character was found {i['count']} times\n"
    report += "--- End report ---"
    return report

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        num_chr = count_characters(file_contents)
        print(generate_report(num_words, num_chr, path))
        


main()