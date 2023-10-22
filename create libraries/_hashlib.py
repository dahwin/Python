#encoding: utf-8
#module _hashlib
# from c:\python3.10\DLLs\_hashlib.pyd

def compare_digest(*args,**kwargs):
    pass
def get_fips_mode(*args,**kwargs):
    pass
def hmac_digest(*args,**kwargs):
    pass
def hmac_new(*args,**kwargs):
    pass
def new(*args,**kwargs):
    pass
def openssl_md5(*args,**kwargs):
    pass
def openssl_sha1(*args,**kwargs):
    pass
def openssl_sha224(*args,**kwargs):
    pass
def openssl_sha256(*args,**kwargs):
    pass
def openssl_sha384(*args,**kwargs):
    pass
def openssl_sha3_224(*args,**kwargs):
    pass
def oenssl_sha3_256(*args,**kwargs):
    pass
def openssl_sha3_384(*args,**kwargs):
    pass
def openssl_sha3_512(*args,**kwargs):
    pass
def openssl_sha_512(*args,**kwargs):
    pass
def openssl_shake_128(*args,**kwargs):
    pass
def openssl_shake_256(*args,**kwargs):
    pass
def pdkdf2_hmac(*args,**kwargs):
    pass
def scrypt(*args,**kwargs):
    pass

# classes


class HASH(object):
    def copy(self,*args,**kwargs):
        '''
        return a copy of the hash object
        '''
        pass
    def digest(self,*args,**kwargs):
        """ return the digest value as a bytes object."""
        pass
    def hexdigest(self,*args,**kwargs):
        """ return the digest value as a string of hexadeciaml digits"""
        pass
    def update(self,*args,**kwargs):
        """ update thsi hash object's state with the provieded string."""

    def __int__(self,*args,**kwargs):
        pass
    def __repr__(self,*args,**kwargs):
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)
    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)
    name = property(lambda self: object(), lambda self, v: None, lambda self: None)


class HASHXOF(HASH):
    def digest(self,*args,**kwargs):
        """ return the digest value as a string of hexadecimal digits."""
        pass
    def hexdigest(self,*args,**kwargs):
        """return the digest vatue as a string of hexadecimal digits. """
        pass
    digest_size = property(lambda self: object(),lambda self, v:None,lambda self:None)

class HMAC(object):
    def copy(self,clone):
        """return a  copy('clone')of the hmch object """
        pass
    def digest(self,*args,**kwargs):
        '''return the digest of the  bytes passed to the update() method so far.'''
        pass
    def hexdigest(self,*args,**kwargs):
        """ Return hexadecimal digest of the bytes passed to the update() method so far.

        This may be used to exchange the value safely in email or other non-binary
        environments."""
        pass
    def update(self,*args,**kwargs):
        pass
    def __int__(self,*args,**kwargs):
        pass
    def __repr__(self,*args,**kwargs):
        """ return repr (self)"""

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

class UnsupportedDigestmodError(ValueError):
    # no doc
    def __init__(self,*args,**kwargs):
        pass
    __weakref__ = property(lambda self: object(),lambda self, v: None, lambda self:None)
    """ list of weak references to the object (if defined)"""
# variables with complex values

openssl_md_meth_names = None
_constructors = None
__loader__ =None
__spec__ = None




