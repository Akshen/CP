class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        self.A = A
        self.B = B
        ltr_count = 0
    
        if len(self.A)==0:
            return ''
            
        for i in self.A:
                ltr_count +=1
    
        tp = []
        ltr_in_line = 0
        temp = self.B

        for i in self.A:
            if (len(i)==temp):
                temp = 0
                ltr_in_line +=1
            elif (len(i)+1)>temp:
                tp.append(ltr_in_line)
                ltr_in_line = 1
                temp = B - ((len(i)+1)) 
            else:
                ltr_in_line +=1
                temp -= (len(i)+1)
    
        tp.append(ltr_in_line)
        line_len = 0
        words_list = [[] for _ in range(len(tp))]

        for i in range(len(tp)):
            for j in range(tp[i]):
                words_list[i].append(self.A[j])
            del self.A[:tp[i]]
    
        def character_count(L):
            count = 0
            for x in L:
                count +=len(x)
            return count
    
        def update_word(sr, i):
            length_w = len(i)
            while(sr>0):
                if len(length_w)==1:
                    i[0] = i[0] + ' '*sr
                    sr -=sr
                    break   
                
                if length_w-1 != i:       
                    for k in range(:
                        if k != len(words_list[i])-1:
                            words_list[i][k] = words_list[i][k] + ' '
                            sr -=1
                else:
                    for k in range(length_w):
                        words_list[i][k] = words_list[i][k] + ' '
                        sr -=1

    
        for i in range(len(words_list)):
            char_count = character_count(words_list[i])
            space_required = self.B - char_count
            update_word(space_required, words_list[i])
    
        
        return [''.join(x) for x in words_list]

obj = Solution()
#print(obj.fullJustify(["zsrs", "daqn", "loajxsl", "hhqkt", "slxiziyf", "rdzfyhgle", "v", "fbsmjxhcn", "pxscg", "hpxndkqjh", "cihpirm", "fhixozfh", "mgeysxb", "icvezcc", "ogcsqhfmbq", "iwmoiwp", "hbksjto", "c", "xn", "w", "otie", "errlpglazq", "jj", "vrtuwlmkh", "yulxfcuypy", "oojvw", "almcvzu", "exchiodmg", "cvx", "gxojn", "ilzrq", "pgtnfg", "mdqtuadbaz", "whfbvtkip", "hggcpal", "lfpbjut", "lrpi", "mgaj", "ttbwvzuhea", "mwdcehyt", "sli", "cdsrkxyou", "jmd", "lgsndxffa", "b", "tbkibeu", "crstuepwvv", "lyday", "pfnwdqir", "mlb", "afgdywx", "ily", "snbehhg", "scndl", "b", "etbrae", "qcrcmqjapf", "ruwsb", "jzpfw", "d", "nj", "fiyugwkj", "dyg", "hnnhx", "wlrrui" ], 61))
#print(obj.fullJustify(['What','must','be','shall','be.'], 12))
print(obj.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))