def lzw_compress(uncompressed):
    dict_size = 256
    dictionnary = dict((chr(i), i) for i in range(dict_size))
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionnary:
            w = wc
        else:
            result.append(dictionnary[w])
            dictionnary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionnary[w])
    return result


def lwz_decompress(compressed):
    from io import StringIO
    dict_size = 256
    dictionnary = dict((i, chr(i)) for i in range(dict_size))
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionnary:
            entry = dictionnary[k]
        elif k == dict_size:
            entry = w + w[0]
        result.write(entry)
        dictionnary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    return result.getvalue()

sentence = "Its cold outside"
compressed_sentence = lzw_compress(sentence)
print(compressed_sentence)
uncompressed_sentence = lwz_decompress(compressed_sentence)
print(uncompressed_sentence)
if (uncompressed_sentence == sentence):
    print("Ok !")
else:
    print("The compression or decompression isn't correct !")