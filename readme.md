# 앱아이콘 생성 

파일명 
appIconGenerate.sh

준비물 
1024.png 

# 파일 복사 

파일명 
filecopy.sh 

파일안에 SOURCE_DIR 과 TARGET_DIR 를 수정해서 사용해야 합니다. 

사용예 
./filecopy.sh [파일명]


# 파일 비교 

파일명 
openDiff.sh

파일안에 SOURCE_DIR 과 TARGET_DIR 를 수정해서 사용해야 합니다. 

사용예 
./openDiff.sh [파일명]

# 피그마 export 한 이미지 후 플러터 프로젝트에 이미지 집어넣기 

피그마에서 1x , 2x, 3x png 로 export 한 후 

해당 파일안에 source

해당 폴더와 py 파일 을 같은 위치에 놓고 

move_image.py 파일 안에 
source_dir 
target_dir_path 
확인 점검후 

python move_image.py  

실행 시킵니다. 




