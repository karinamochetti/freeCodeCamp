def find_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_len = len(word)

    def search(line, word):
        i = line.find(word)
        if i != -1:
            start = i
            end = i + word_len - 1
            return start, end

        i = line[::-1].find(word)
        if i != -1:
            start = len(line) - 1 - i
            end = start - (word_len - 1)
            return start, end


    for r in range(rows):
        result = search("".join(matrix[r]), word)
        if result:
            return [[r, result[0]], [r, result[1]]]

    # Check Columns (Vertical)
    for c in range(cols):
        column = "".join(matrix[r][c] for r in range(rows))
        result = search(column, word)
        if result:
            return [[result[0], c], [result[1], c]]

print(find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat"))
print(find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog"))
print(find_word([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish"))
print(find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox"))
