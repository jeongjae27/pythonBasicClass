buffer_size = 1024

with open('videoplayback.mp4','rb') as source: # read binary
    with open('videoplayback2.mp4','wb'):       # write binary
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)

print('Finish')