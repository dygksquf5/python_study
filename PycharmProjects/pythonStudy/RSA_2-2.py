from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

# Private key 와 Public key 쌍을 생성한다.
# Private key는 소유자가 보관하고, Public key는 공개한다.

key = RSA.generate(2048)
privKey = key.export_key() #key 소유자 보관용
pubKey = key.publickey().export_key() #외부 공개용!



# #keyPair 의 p,q,e,d 를 확인 해 본다.
# keyObj = RSA.importKey(privKey)
# print("p = ", keyObj.p)
# print("q = ", keyObj.q)
# print("e = ", keyObj.e)
# print("d = ", keyObj.d)

#암호화 할 원문
plainText = 'This is Plain text. It will be encrypted using RSA'.encode("utf-8")
print()
print("원문: ")
print(plainText)

#공개키로 원문을 암호화 한다.
key = RSA.import_key(pubKey)
cipher_rsa = PKCS1_OAEP.new(key)
cipherText = cipher_rsa.encrypt(plainText)
print("\n")
print("암호문 :")
print(cipherText.hex())

#Private key 를 소유한 수신자는 자신의 Private key로 암호문을 해독한다.
#pubKey와 쌍을 이루는 privKey만이 이 암호문을 해독할 수 있다.

key = RSA.import_key(privKey)
cipher_rsa = PKCS1_OAEP.new(key)
plainText2 = cipher_rsa.decrypt(cipherText)

print('\n')
print("해독문 :")
print(plainText2)






