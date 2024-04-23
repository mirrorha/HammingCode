def countParityBits(n):
    for i in range(n):
        if 2**i >= n + i + 1:
            return i


def addParityBits(data):

    n = len(data)
    k = countParityBits(n)
    print(f"k = {k}")

    res = ""

    j = 0
    l = 0

    for i in range(1, n + k + 1):
        if i == 2**j:
            res = res + '0'
            j += 1
        else:
            res = res + data[l]
            l += 1

    print(res)
    return res


def encode(data):
    print(data)
    m = len(data)
    code = addParityBits(data)
    n = len(code)
    k = n - m  # Number of parity bits
    print(f"k in encode = {k}")
    ans = "0" + code

    for i in range(k):
        val = 0
        for j in range(n):
            if (j + 1) & (2**i) == 2**i:  # if i-th parity bit covers j-th data bit
                val = val ^ int(ans[j])  # parity bit value = 1 if sum of the covered bits is odd, 0 - else

        ans = ans[:2**i] + str(val) + ans[2**i + 1:]

    return ans[1:]


def isPowerOfTwo(n, l):
    i = 0
    arr = []
    while 2**i <= l:
        arr.append(2**i)
        i += 1

    return n in arr


def decode(data):
    n = len(data)
    k = 1
    error = ""

    while 2**k < n:
        k += 1
    print(f"k in decoding = {k}")

    for i in range(k):
        val = 0
        for j in range(n):
            if (j + 1) & (2**i) == 2**i:
                val = val ^ int(data[j])
        error = error + str(val)

    error = int(error, 2)

    if error == 0:
        print("No errors")

    data = data
    ans = ""

    for i in range(len(data)):
        if not(isPowerOfTwo(i + 1, len(data))):
            ans += data[i]

    return ans


string = "Hello, World!"


def createByteArray(data):
    # arr = []
    # for x in data:
    #     arr.append(format(ord(x), 'b'))
    # print(arr)

    return ''.join('{0:08b}'.format(ord(x), 'b') for x in data)


data = createByteArray(string)
#data = "0100010000111101"
print(f"data = {data}")
code = encode(data)
print(f"encoded data - {code}")
decoded = decode(code)
print(f"decoded data - {decoded}")
print(data == decoded)