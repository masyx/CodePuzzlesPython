from nose.tools import assert_equal
# Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. 
# Only compress the string if it saves space.



class CompressString():
    # O(n) time | O(n) space
    def runLengthEncoding(self, string):
        if not string:
            return string
        result = ''
        prev_char = string[0]
        count = 0
        for char in string:
            if char == prev_char:
                count += 1
            else:
                result += f"{prev_char + (str(count) if count > 1 else '')}"
                prev_char = char
                count = 1
        result += f"{prev_char + (str(count) if count > 1 else '')}"
        return result if len(result) < len(string) else string

    def runLengthEncoding_2(self, string):
        if not string:
            return string
        result = []
        prev_char = string[0]
        count = 0
        for char in string:
            if char == prev_char:
                count += 1
            else:
                result.append(prev_char)
                result.append(f"{(str(count) if count > 1 else '')}")
                prev_char = char
                count = 1
        result.append(prev_char)
        result.append(f"{(str(count) if count > 1 else '')}")
        return ''.join(result) if len(result) < len(string) else string


class TestCompressString():
    def test_compress_string(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDDE'), 'A3BC2D4E')
        assert_equal(func('BAAACCDDDD'), 'BA3C2D4')
        assert_equal(func('AAABAACCDDDD'), 'A3BA2C2D4')
        assert_equal(func('.............______=========AAAA   AAABBBB   BBB'), '.13_6=9A4 3A3B4 3B3')
        print(f'Success: test_compress_string({func.__func__})')

def main():
    #string = '.............______=========AAAA   AAABBBB   BBB'
    stringCompressor = CompressString()
    tester = TestCompressString()
    tester.test_compress_string(stringCompressor.runLengthEncoding)
    tester.test_compress_string(stringCompressor.runLengthEncoding_2)
    
if __name__ == "__main__":
    main()