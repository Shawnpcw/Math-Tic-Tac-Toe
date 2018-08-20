from django.db import models
import bcrypt, re, datetime
class UserManager(models.Manager):
    def basic_validator(self, postData):
        result = {}
        errors = []
        
        Current_username = User.objects.filter(username=postData['username'])
        
        if len(postData['username']) <3:
            errors.append('Username should be at least 4 charaters!')
        if any(i.isdigit() for i in postData['username']):
            errors.append('Username should be only letters!')
        if len(Current_username)>0:
            errors.append('Username already exists!')
        if len(postData['password']) <7:
            errors.append('Password should be at least 8 charaters!')
        if postData['password'] != postData['pwcheck']:
            errors.append('Passwords dont match!')

        if len(errors) ==0:
            hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            new_user =User.objects.create(username=postData['username'], pw_hash = hashed_pw.decode(), gamesWon=0, gamesPlayed=0)
            result['user_id'] = new_user.id
        else:
            result['errors'] = errors
        return result
    def login_validator(self, postData):
        result = {}
        errors = []
        user = User.objects.filter(username=postData['username'])
        if len(user) ==1:
            pw_hash = user[0].pw_hash
            if bcrypt.checkpw(postData['password'].encode(),pw_hash.encode()):
                result['user_id'] = user[0].id
            else:
                errors.append('Username or Password Incorrect')
                result['errors'] = errors
        else:
            errors.append('Username or Password Incorrect')
            result['errors'] = errors
        return result
class User(models.Model):
    username = models.CharField(max_length =255)
    pw_hash = models.CharField(max_length =255)
    gamesWon = models.IntegerField()
    gamesPlayed = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()