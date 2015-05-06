def find_sha256():
    start = SegStart(ScreenEA())
    end = SegEnd(ScreenEA())
    suspects = []
    for i in range(start, end):
        data = Dword(i)
        if data == 0x6A09E667 or data == 0x0BB67AE85 or data == 0x3C6EF372:
            suspects.append(i)

    print "[+] SHA 256 suspects found at:"
    for item in suspects:
        print "\t" + hex(item)

def find_sha1():
    start = SegStart(ScreenEA())
    end = SegEnd(ScreenEA())
    suspects = []
    for i in range(start, end):
        data = Dword(i)
        if data == 0x67452301 or data == 0x98BADCFE or data == 0x0EFCDAB89:
            suspects.append(i)

    print "[+] SHA 1 suspects found at:"
    for item in suspects:
        print "\t" + hex(item)

find_sha256()
find_sha1()
