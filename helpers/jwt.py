from jose import jwt
from config.config import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
    
def validate_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])                
    except:
        return False
    return payload
    

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)