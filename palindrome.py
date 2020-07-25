
def is_palendrome(s):
    s1 = []
    for i in s.lower():
        if i in 'abcdefghijklmnopqrstuvwxyz':
            s1.append(i)
    return s1 == list(reversed(s1))
            
if __name__ == '__main__':
    def test(s):
        print(s.__repr__(), 'is palendrome?', is_palendrome(s))

    test('"A man, a plan, a canal: Panama"')
    test('"foo"')
    test('')
    test('rabbit')
    test("Madam, I'm Adam")

# vim: ai sw=4 ts=4 et showmatch
