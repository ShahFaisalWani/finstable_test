input_list  = [
  "aaaaaabbbbbbbbbbbbbcccccccc","abcdefgh", "aabbccddee","aaaaccccddddd",
  "abcdefgabcdefgh","Bbbbcccccccccccccbbbbbb`","aaaaaaaaaaaaaaa",
  "abbbbbbbbbbbaaaaaa"
]

words = []
longest_length = 0

for word in input_list:
  word_len = len(set(word))
  if word_len > longest_length:
    longest_length = word_len
  words.append((word, word_len))

answer = [(word,length) for  word, length in words if length == longest_length]

for word, length in answer:
  print("Word = %s, unique length = %d \n" % (word,length))