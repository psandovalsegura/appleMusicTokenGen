# -*- coding: UTF-8 -*-
# 
# Pedro Sandoval Segura
# @psandovalsegura
# 8/10/18
#

import glob, os
import datetime
import jwt

# Apple Music supports only developer tokens that are signed with the ES256 algorithm
defaultAlg = 'ES256'

# Token expiration time must not be greater than 15777000 (6 months in seconds)
maxExpTime = 15777000

def getIssuedAtAndExpTime():
    """
    Log the time of issuance and the expiration time as seconds strings
    """
    issuedAt = datetime.datetime.now()
    expirationTime = datetime.datetime.now() + datetime.timedelta(seconds=maxExpTime)
    return issuedAt.strftime("%s"), expirationTime.strftime("%s")

def getPrivateKey():
    """
    Read the user's Music Kit Private Key
    The *.p8 file should be placed in the same directory as this script
    """
    for f in glob.glob("*.p8"):
        privateKeyFile = open(f, "r")
        privateKeyString = privateKeyFile.read()
        return privateKeyString

    raise ValueError('Please place your AuthKey_*.p8 file in the current working directory')

def getTeamID():
    """
    Prompt user for their 10-character Team ID
    """
    print("👤 Hint: This can be found at https://developer.apple.com/account/#/membership/")
    print("👤 Enter your Apple Developer Team ID: ")
    teamID = raw_input()
    if len(teamID) != 10:
        raise ValueError('Team ID is invalid')
    return teamID

def getKeyIdentifier():
    """
    Prompt user for their key identifier
    """
    print("🔑 Hint: This can be found at https://developer.apple.com/account/ios/authkey/")
    print("🔑 Enter your key identifier: ")
    keyIdentifier = raw_input()
    return keyIdentifier

def createAuthToken():
    """
    Create an Apple Music JSON Web Token
    """
    keyIdentifier = getKeyIdentifier()
    teamID = getTeamID()
    issuedAt, expirationTime = getIssuedAtAndExpTime()
    secret = getPrivateKey()
    headers = {
        "alg": defaultAlg,
        "kid": keyIdentifier
    }
    payload = {
        "iss": teamID,
        "exp": int(issuedAt),
        "iat": int(expirationTime)
    }
    return jwt.encode(payload, secret, algorithm=defaultAlg, headers=headers)

if __name__ == "__main__":
    token = createAuthToken()
    print("✅ Your token was successfully created: ")
    print(token)

    print("\n🔔 To test the validity of your token, try this curl command:")
    print("curl -v -H 'Authorization: Bearer %s' \"https://api.music.apple.com/v1/catalog/us/artists/1798556\" " % (token))