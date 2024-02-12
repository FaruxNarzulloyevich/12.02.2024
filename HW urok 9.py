class worker:
    def __init__(self,follow,obey,listen):
        self.follow = follow
        self.obey = obey
        self.listen = listen

class menedger(worker):
    def __init__(self,follow,obey,listen):
        super.__init__(follow,obey,listen)
    def give_advise(self):
        return 'Davayte sdelayem tak!'

    def change(self):
        return 'Peredelayte'

