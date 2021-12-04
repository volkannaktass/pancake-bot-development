   
import json
   
# Opening JSON file
with open("file.txt") as tweetfile:
    pyresponse = json.loads(tweetfile.read())

print(pyresponse)


print(type(pyresponse["senderAddress"]))
print(type(pyresponse["privateKeyBar"]))
a = float(pyresponse["bnbAmount"])

print(type(a))
