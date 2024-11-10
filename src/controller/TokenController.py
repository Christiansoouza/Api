from service.TokenService import TokenService

class TokenControlerr:
    def create_token(user:str,password:str):
        return TokenService.create_token(user=user, password=password)
