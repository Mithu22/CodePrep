class Solution:

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lengths = [len(words[i]) for i in range(len(words))]
        currLength = 0
        start = stop = 0
        i = 0
        lines = []
        while i < len(lengths):
            currLength = 0
            while i < len(lengths) and currLength + lengths[i] <= maxWidth:
                currLength += 1 + lengths[i]
                i = i + 1
            stop = i - 1
            s = ""
            line = []
            for j in range(start, stop + 1):
                line.append(words[j])
            start = i
            lines.append(line)

        results = []
        for line in lines[:-1]:
            s = ""
            lineLength = 0
            for w in line:
                lineLength += len(w)
            spaces = len(line) - 1
            lineLength += spaces
            toPad = maxWidth - lineLength
            if len(line) == 1:
                s += line[0] + (" " * toPad)
            else:
                eachSpace, remSpace = divmod(toPad, spaces)
                for w in line[:-1]:
                    s += w + " " + (" " * eachSpace)
                    if remSpace:
                        s += " "
                        remSpace = remSpace - 1
                s += line[-1]
            results.append(s)

        ll = ""
        lastLineLength = 0
        for w in lines[-1]:
            lastLineLength += len(w)
            ll += w + " "
        lastLineLength += len(lines[-1]) - 1
        lpd = maxWidth - lastLineLength
        ll = ll.strip()
        ll += " " * lpd
        results.append(ll)
        return results