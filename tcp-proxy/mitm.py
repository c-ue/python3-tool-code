def modify_ascii(data,mode=None):
    """
    use to modify the data  pass my proxy
    """
    if mode is None:
        return data
    elif mode == 1:
        """
        modify the data on way 1
        """
        return b''
    elif mode == 2:
        """
        modify the data on way 2
        """
        return b''
    else:
        return None

def hexdump( src, length=16, sep='.' ):
    """
        @brief Return {src} in hex dump.
        @param[in] length	{Int} Nb Bytes by row.
        @param[in] sep		{Char} For the text part, {sep} will be used for non ASCII char.
        @return {Str} The hexdump
        @note Full support for python2 and python3 !
        """
    result = []
    for i in range(0, len(src), length):
        subSrc = src[i:i+length]
        hexa = ''
        for h in range(0,len(subSrc)):
            if h == length/2:
                hexa += ' '
            h = subSrc[h]
            if not isinstance(h, int):
                h = ord(h)
            h = hex(h).replace('0x','')
            if len(h) == 1:
                h = '0'+h
            hexa += h+' '
        hexa = hexa.strip(' ')
        text = ''
        for c in subSrc:
            if not isinstance(c, int):
                c = ord(c)
            if 0x20 <= c < 0x7F:
                text += chr(c)
            else:
                text += sep
        result.append(('%08X:  %-'+str(length*(2+1)+1)+'s  |%s|') % (i, hexa, text))
    return '\n'.join(result)