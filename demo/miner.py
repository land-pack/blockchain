


class HashMiner(object):

    def __init__(self, max_length=256):
        self.max_length = max_length


    def miner(self, counter=100000):
        """

        """
        lst = ['0' for i in range(self.max_length)]
        sst = ''.join(lst)
        
        print(sst)
        for i in range(counter):
            subfix = "{0:b}".format(i)
            s_len = self.max_length -  len(subfix)
            prefix = sst[:s_len] 
            sst = prefix + subfix
            print(sst)


if __name__ == '__main__':
    hm = HashMiner(max_length=32)
    hm.miner()
