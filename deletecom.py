import amino

client=amino.ClientSid()
#تسجيل
print ("By Endru")

sid=input("sid: ")

client.sssid(sid=sid)

#رابط المنتدى

comlink=input("Community Link: ")

cominfo=client.get_from_code(comlink)
comId=cominfo.path[1:cominfo.path.index('/')]

subclient=amino.SubClient(comId=comId,profile=client.profile)


clientx=amino.acm.ACM(profile=client.profile, comId=comId)

email=input("Your Email: ")
password=input("Your Password: ")

clientx.delete_community(email=email,  password=password, verificationCode=None)

print ("Done")
