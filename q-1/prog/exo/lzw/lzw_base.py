def lzw_compress(uncompressed):
    pass# Code compress alogrithm here

def lwz_decompress(compressed):
    pass # Code decompress alogrithm here

sentence = "Its cold outside"
compressed_sentence = lzw_compress(sentence)
print(compressed_sentence)
uncompressed_sentence = lwz_decompress(compressed_sentence)
print(uncompressed_sentence)
if (uncompressed_sentence == sentence):
    print("Ok !")
else:
    print("The compression isn't correct !")