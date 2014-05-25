import os, sys

def crc16(buff, crc = 0, poly = 0xa001):
	l = len(buff)
	i = 0
	while i < l:
		ch = (buff[i])
		uc = 0
		crc ^= ch
		while uc < 8:
			if (crc & 1):
				crc = (crc >> 1) ^ poly
			else:
				crc >>= 1
			uc += 1
		i += 1
	return crc

buf = [0xaa, 0x00, 0xaa, 0xbb, 0xcc, 0xdd]

crc = crc16(buf)
buf.append((crc >> 0) & 0xff)
buf.append((crc >> 8) & 0xff)

s = "sudo i2cset -y 6 0x23 " + " ".join([str(x) for x in buf]) + " i"
print (s)
os.system(s)