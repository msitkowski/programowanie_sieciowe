# -*- coding: utf-8 -*-
from base64 import b64decode, b64encode
from datetime import datetime

class myBase64():
    def __init__(self):
        self.chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    def my_base64encode(self, _str):
        _str_len = len(_str)
        _encoded_data = ''
        f = open('bit_string.txt', 'w')
        
        for _c in _str:
            f.write(format(ord(_c), '08b'))
            
        f.close()
        
        f = open('bit_string.txt', 'r')
        
        while True:
            bit_str = f.read(6)
            
            if bit_str == '':
                break
            
            while len(bit_str) < 6:
                bit_str += '0'
                
            _encoded_data += self.chars[int(bit_str, 2)]
        
        f.close()
            
        while _str_len%3 != 0:
            _encoded_data += '='
            _str_len += 1

        return _encoded_data
    
    def my_base64decode(self, _str):
        _decoded_data = ''
        f = open('decode_bit_str.txt', 'w')
         
        for _c in _str:
            if _c != '=':
                f.write(format(self.chars.index(_c), '06b'))
                
        f.close()
        f = open('decode_bit_str.txt', 'r')
        
        while True:
            bit_str = f.read(8)
            
            if bit_str == '' or len(bit_str) < 8:
                break
            
#             if len(bit_str) < 8:
#                 print bit_str, len(bit_str)
#             while len(bit_str) < 8:
#                 bit_str += '0'
 
            _decoded_data += chr(int(bit_str, 2))
                
        return _decoded_data

def main():
    mybase64 = myBase64();
    
    f = open('test.docx', 'rb')
    #f = open('test.pdf', 'rb')
    #f = open('20160924_110144.jpg', 'rb')
    to_encode = f.read()
    s_time = datetime.now()
    encoded = mybase64.my_base64encode(to_encode)
    #encoded = mybase64.my_base64encode('Mama i tata')
    print 'Encding time:', datetime.now()-s_time
    f.close()
    _build_in_b64_encoded = b64encode(to_encode)
    
    if _build_in_b64_encoded == encoded:
        print 'Build in b64encoding and myb64encoding returner same value'
        
    s_time = datetime.now()
    decoded = mybase64.my_base64decode(encoded)
    print 'Decoding time:', datetime.now()-s_time
    
    if b64decode(encoded) == decoded:
        print 'myb64 encoded msg decoded by build in b64decode and myb64decode returned same value'
        
    fp = open('decoded_test.docx', 'wb')
    #fp = open('decoded_test.pdf', 'wb')
    #fp = open('decoded_20160924_110144.jpg', 'wb')
    #fp = open('decoded_text.txt', 'w')
    fp.writelines(decoded)
    fp.close()
 

if __name__ == '__main__':
    main()