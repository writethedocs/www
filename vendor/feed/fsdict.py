# −*− coding: UTF−8 −*−
from path import path
import os
import pickle
"""
A class providing dictionary access to a folder.
cribbed from http://bitbucket.org/howthebodyworks/fsdict
"""

def get_tmp_dir():
    import tempfile
    return tempfile.mkdtemp()
    
class FSDict(dict):
    """
    provide dictionary access to a temp dir. I don't know why i didn't just use
    shelve. I think I forgot it existed.
    
    N.B. the keys ordering here is FS-dependent and thus unlike to be the same as
    with a real dict. beware.
    """
    
    unclean_dirs = []
    
    def __init__(self, initval=[], work_dir=None, *args, **kwargs):
        if work_dir is None:
            work_dir = get_tmp_dir()
        self.work_dir = path(work_dir)
        if not self.work_dir.exists():
            self.work_dir.mkdir()
        for key, val in getattr(initval, 'iteritems', initval.__iter__)():
            self[key] = val
        self.unclean_dirs.append(self.work_dir)
        super(FSDict, self).__init__(*args, **kwargs)
    
    def __setitem__(self, key, val, *args, **kwargs):
        pickle.dump(val, open(self.work_dir/key, 'w'))
    
    def __getitem__(self, key, *args, **kwargs):
        return pickle.load(open(self.work_dir/key, 'r'))
    
    def __repr__(self):
        """
        a hardline list of everything in the dict. may be long.
        """
        return repr(dict([(k, v) for k, v in self.iteritems()]))
        
    def __str__(self):
        """
        str is truncated somewhat.
        """
        if len(self.keys()):
            return '{' + repr(self.keys()[0]) + ':' + repr(self[self.keys()[0]]) + ', ...'
        else:
            return super(FSDict, self).__str__()
    
    def keys(self, *args, **kwargs):
        return [key for key in self.iterkeys()]
    
    def iterkeys(self, *args, **kwargs):
        for f in self.work_dir.files():
            yield str(self.work_dir.relpathto(f))
        
    def iteritems(self):
        for key in self.iterkeys():
            yield key, self[key]
            
    def itervalues(self):
        for key in self.iterkeys():
            yield self[key]
            
    def __delitem__(self, key, *args, **kwargs):
        (self.work_dir/key).unlink()
    
    def values(self, *args, **kwargs):
        return [self[key] for key in self.keys()]
        
    def cleanup(self):
        self.work_dir.rmtree()
    
    @classmethod
    def cleanup_all(cls):
        for fsd in cls.unclean_dirs:
            try:
                fsd.rmtree()
            except OSError:
                pass
    
    def move(self, new_dir):
        
        try:
            self.work_dir.move(new_dir)
        except Exception, e:
            raise
        else:
            self.work_dir = new_dir
    
    def __eq__(self, other):
        """
        when compared to a dict, equate equal if all keys and vals are equal
        note, this is potentially expensive.
        """
        #duck type our way to sanity:
        if not hasattr(other, 'keys'): return False
        #OK, it's a dict-ish thing
        try:
            return all([self[key]==other[key] for key in other]) and \
              len(self.keys())==len(other.keys())
        except KeyError:
            return False