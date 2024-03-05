# from OpenSSL import crypto

# #cert is the encrypted certificate int this format -----BEGIN -----END
# cert = 'certificate.pem'
# crtObj = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
# pubKeyObject = crtObj.get_pubkey()
# pubKeyString = crypto.dump_publickey(crypto.FILETYPE_PEM,pubKeyObject)
# print (pubKeyString)

# import rsa

# def generate
# (pubkey, privkey) = rsa.newkeys(512)
# # print(pubkey)
# # print("*******************")
# # print(privkey)
# # print(rsa.encrypt(pubkey))
# message = "Hello World!!"
# ciphertext = (rsa.encrypt(message.encode('ascii'), pubkey))
# print(ciphertext)
# pt = rsa.decrypt(ciphertext, privkey).decode('ascii')
# print(pt)

from Crypto.PublicKey import RSA

def get_keys():
    new_key = RSA.generate(2048)

    private_key = new_key.exportKey("PEM")
    public_key = new_key.publickey().exportKey("PEM")

    # print(private_key.decode("utf-8"))
    fd = open("private_key.pem", "wb")
    fd.write(private_key)
    fd.close()

    # print(public_key.decode("utf-8"))
    fd = open("public_key.pem", "wb")
    fd.write(public_key)
    fd.close()
    return (public_key,private_key)

    