import struct
# import matplotlib.pyplot as plt


class PCM():
    def __init__(name):
        with open(name, "rb") as file:
            data = file.read()
        ChunkID = data[0:4].decode()
    ChunkID = 0

class WavField():
    name = ''
    offset = 0
    size = 0
def main():
    wav = PCM('circuit.wav')
    

if __name__ == '__main__':
    main()   



# print(data)

#fileType = data[0:4].decode()

#print(fileType)

#fileSize = struct.unpack_from('i', data, offset=4)
#print(fileSize)



#pureAdcData =[a for a in struct.iter_unpack("H",data[44:])]

# print(pureAdcData)

# plt.plot(pureAdcData)
# plt.show()

