class Config :
    JWT_SECRET_KEY = 'tset'
    S3_BUCKET = "csvfiles"
    S3_KEY = "don't public"
    S3_SECRET = "don't public"
    S3_LOCATION = 'https://{}.s3.amazonaws.com/'.format(S3_BUCKET)

