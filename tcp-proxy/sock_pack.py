try:
    import pickle
    pickle_exist = True
except ImportError:
    pickle_exist = False
try:
    import base64
    base64_exist = True
except ImportError:
    base64_exist = False


def recv_all(sock):
    data = b''
    while True:
        content = sock.recv(4096)
        data += content
        if content < 4096:
            break
    return data


def serialize_send(sock,data,type=None):
    if (type is None or type == 1) and pickle_exist:
        ser_data = pickle.dumps(data)
        sock.sendall(b'1'+ser_data)
    elif (type is None or type == 2) and base64_exist:
        ser_data = base64.b64encode(data)
        sock.sendall(b'2'+ser_data)
    else:
        raise ImportError('No useful package or not match.')
    return


def serialize_recv(sock):
    data = recv_all(sock)
    if data[0] == b'1' and pickle_exist:
        ret_data = pickle.loads(data[1:])
        return ret_data
    elif data[0] == b'2' and base64_exist:
        ret_data = base64.b64decode(data[1:])
        return ret_data
    else:
        raise ImportError('No useful package or not match')
    return