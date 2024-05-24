def winmessage(s):
    if s[0] == s[1] and s[1] == s[2] and s[0] != "0":
        return "Победил " + s[0]
    if s[3] == s[4] and s[4] == s[5] and s[3] != "0":
        return "Победил " + s[3]
    if s[6] == s[7] and s[7] == s[8] and s[6] != "0":
        return "Победил " + s[6]
    if s[0] == s[3] and s[3] == s[6] and s[0] != "0":
        return "Победил " + s[0]
    if s[1] == s[4] and s[4] == s[7] and s[1] != "0":
        return "Победил " + s[1]
    if s[2] == s[5] and s[5] == s[7] and s[2] != "0":
        return "Победил " + s[2]
    if s[0] == s[4] and s[4] == s[8] and s[0] != "0":
        return "Победил " + s[0]
    if s[2] == s[4] and s[4] == s[6] and s[2] != "0":
        return "Победил " + s[2]
	return "Победитель определен"