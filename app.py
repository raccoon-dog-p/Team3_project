from flask import Flask, request
# JWT 사용을 위한 SECRET_KEY 정보가 들어있는 파일 임포트
from config import Config
from flask.json import jsonify
from http import HTTPStatus
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.movie import AddFavoriteResource, DeleteFavoriteResource, MovieSearchResource
from resources.home import HomePosterResource
from resources.login import UserLoginResource
from resources.rating import MovieRecommandResource
from resources.register import UserRegisterResource
from resources.logout import UserLogoutResource, jwt_blacklist


app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)

# JWT 토큰 만들기
jwt = JWTManager(app)

# todo : 로그아웃 개발하고 나서, 코멘트 해제한다.
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

# 경로와 리소스를 연결한다.
api.add_resource(UserRegisterResource, '/api/register')
api.add_resource(UserLoginResource, '/api/login')
api.add_resource(UserLogoutResource, '/api/v1/user/logout')
api.add_resource(MovieSearchResource,'/1')
api.add_resource(AddFavoriteResource,'/2/<int:movie_id>')
api.add_resource(DeleteFavoriteResource,'/3/<int:movie_id>')
api.add_resource(MovieRecommandResource,'/4')
api.add_resource(HomePosterResource,'/home')

if __name__ == '__main__' :
    app.run()