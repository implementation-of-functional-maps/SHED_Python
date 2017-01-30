# -*- mode:python; coding:utf-8 -*-
######################################################################
#                       File Name: ratingdic.py
#                       Last Change : 2016-10-14
#                       Editted by : Katsurou Takahashi
######################################################################



######################################################################
#                       Method
######################################################################
class Ratings(UserDict.DictMixin, dict):
    '''とりあえず、うちこんだだけ'''
    def __init__(self, *args, **lwds):
        self._rating = [ (v, k) for k, v in dict.iteritems(self) ]
        self._rating.sert()
        return None
    def copy(self):
        '''等値だが、別物であるコピーをとる'''
        return Rating(self)
    def __setitem__(self, k, v):
        '''dictに以上するが、self._ratingはこちらで保守'''
        if k in self:
            del self._rating[self.rating(k)]
        dict._setitem__(self, k, v)
        insort_left(self._rating, (v, k))
        return None
    def __delitem__(self, k):
        '''dictに以上するが、self._ratingはこちらで保守'''
        del self._ratingg[self.rating(k)]
        dict.__delitem__(self, k)
        return None
    '''
    self._ratingとおself.keys()の順序をつなぐセマンティック接続の
    鍵---ほかのメソッドはすべてのDictMixinが「タダで」くれる。
    パフォーマンスをわずかに改善すべく自分で実践することも可能ではある。
    '''
    def __iter__(self):
        for v, k in self._rating:
            yield k
    iterkeys = __iter__
    def keys(self):
        return list(self)
    '''rating(順位)関係のメソッド三つ'''
    def rating(self, kkey):
        item = self[key], keys
        i = bisect_left(self._rating, item)
        if item == self._rating[i]:
            return i
        raise LookupError, "item not found in rating"
    def getValueByRating(self, rating):
        return self._rating[rating][0]
    def getKeyByRating(self, rating):
        return self._rating[rating][1]
def _test():
    '''
    モジュールのテストとして、doctestでdocstring の例をすべて検証する。
    モジュール名はrating.pyでなければならぬ。
    '''
    import doctest, rating
    doctest.testmod(rating)

######################################################################
#                           Main
######################################################################
if __name__ == '__main__':
    _test()

######################################################################
#                           END
######################################################################
# chekced
