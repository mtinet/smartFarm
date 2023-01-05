import firebase_admin
from firebase_admin import credentials, storage

# Firebase 인증 정보를 가져옵니다.
cred = credentials.Certificate("serviceAccountKey.json")

# Firebase 인증 정보를 이용해 애플리케이션을 초기화합니다.
firebase_admin.initialize_app(cred, {
    'storageBucket': 'imageandvideo-19310.appspot.com'
})

# 업로드할 이미지 파일을 열기 위해 파일 객체를 생성합니다.
with open("video.mp4", "rb") as video_file:
    # 이미지 파일 데이터를 읽어옵니다.
    video_data = video_file.read()

    # 이미지 데이터를 이용해 Blob 객체를 생성합니다.
    bucket = storage.bucket()
    blob = bucket.blob("video/video.mp4") # 올라갈 폴더와 파일명
    blob.upload_from_string(video_data, content_type='video/mp4') # 콘텐츠 타입 설정

# 업로드된 이미지의 URL을 가져옵니다.
url = blob.public_url
print(url)
