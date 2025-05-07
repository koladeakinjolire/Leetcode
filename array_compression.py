class Solution(object):
    def compress(self, chars):
        if not chars:
            return 0

        write_idx = 0
        read_idx = 0
        n = len(chars)

        while read_idx < n:
            current_char = chars[read_idx]
            count = 0

            while read_idx < n and chars[read_idx] == current_char:
                read_idx += 1
                count += 1

            chars[write_idx] = current_char
            write_idx += 1

            if count > 1:
                for digit in str(count):
                    chars[write_idx] = digit
                    write_idx += 1

        return write_idx
