# Advanced Encryption Standard(AES) 알고리즘 연습임!!
# 그리고 CBC 모드로 암호화 할거임 (Cipher block chain)

from Cryptodome.Cipher import AES
from Cryptodome import Random
import numpy as np

#대칭키를 만든다. 대칭키는 128-bit, 192-bit, 256-bit를 사용할 수 있다.

secretKey128 = b'0123456701234567'
secretKey192 = b'012345670123456701234567'
secretKey256 = b'01234567012345670123456701234567'

#128-bit key 를 사용한다.

secretKey = secretKey128
# plainText = "Dong ma riu ou "
plainText = 'This is Plain text. It will be encrypted using AES with CBC mode'
print("\n\n")
print("원문  :")
print(plainText)

#CBC 모드에서는 plain text 가 128-bit(16byte)의 배수가 돼야 하므로, padding이 필요없음
#padding 으로 NULL문자를 삽입함. 수신자는 별도로 padding 을 제거할 필요는 없음

n = len(plainText)
if (n % 16) != 0:
    n = n + 16 - (n % 16)
    plainText = plainText.ljust(n, '\0')
#initialisation vector. iv도 수산자에게 보내기!

iv = Random.new().read(AES.block_size)
ivcopy = np.copy(iv)

#송신자는 secretKey와 iv로 plainText를 암호문으로 변환한다.

iv = Random.new().read(AES.block_size)
ivcopy = np.copy(iv)
aes = AES.new(secretKey, AES.MODE_CBC, iv)
cipherText = aes.encrypt(plainText.encode()) #encode utf8 넣어줘야 됨!! 책에는 없엉
print("\n\n\n")
print("암호문  : ")
print(cipherText.hex())

aes = AES.new(secretKey, AES.MODE_CBC, iv) #여기 ivcopy 변수 사용하지말고, 그냥 iv 값으로만 제출하자. ! 오류남. 아마 numpy 모듈 관련 오류인듯. 쥬피터에서는 실행 잘 됨 .
plainText2 = aes.decrypt(cipherText)
plainText2 = plainText2.decode()
print("\n\n\n")
print("해독문  :")
print(plainText2)

