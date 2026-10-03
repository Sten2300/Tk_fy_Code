import string
import time
import random







class Compare_time:
    def __init__(self,corr_word):
        all_letters  = string.ascii_lowercase
        self.alphab = [let for let in all_letters]
        self.alphab.append(" ")
        self.corr_word = corr_word
        self.str_length = len(corr_word)
        self.cur_str = ""
        self.strtrue = False

    def gen_string(self):
        out = ''
        if len(self.cur_str) != self.str_length:
            for _ in range(self.str_length):
                out += self.alphab[random.randint(0,26)] #len == 27
            return out
        else:
            new_str = self.cur_str
            for i in range(self.str_length):
                if new_str[i] != self.corr_word[i]:
                    out += self.alphab[random.randint(0,26)] #len == 27
                else:
                    out += new_str[i]
            return out


    def score_str(self, s):
        score = 0
        try: 
            for i in range(self.str_length):
                if s[i] == self.corr_word[i]:
                    score += 1
        except IndexError:
            return -1

        return score/(self.str_length)*100
    
    def compare(self, newstr):
        old = (self.cur_str, self.score_str(self.cur_str))
        new = (newstr, self.score_str(newstr))
        if new[1] > old[1]:
            self.cur_str = new[0]

    def done(self):
        if self.corr_word == self.cur_str:
            self.strtrue = True


    def run(self):
        start_time = time.time()
        cur_count = 0
        while not self.strtrue:
            new_str = self.gen_string()
            self.compare(new_str)
            self.done()
            if cur_count % 10 == 0:
                end_time = time.time()
                print(f'current best word is: {self.cur_str} after {cur_count} iterations')
            cur_count += 1
        end_time = time.time()
        print(self.cur_str)
        print("total time to find word was:", end_time - start_time)


word = "methinks it is like a weasel"
c = Compare_time(word)
c.run()
    



