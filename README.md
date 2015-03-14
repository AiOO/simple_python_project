# simple_python_project

`(optional)` 은 전부다 구현하고 시간남으면 구현하기.

## login required

 - 로그인이 필요함
 - 로그인 되어있지않다면 `/login` 으로 redirection.

## GET /login
 - 로그인을 위한 아이디 받는 input 필드있음
 - `(optional)` 패스워드 받는 input 필드있음
 - 로그인 버튼

## POST /login
 - 유저 아이디 받아서 로그인
   - 만약 유저 존재하지 않는다면 생성후 로그인
 - 토큰을 만들던지 or 세션에 저장하던지
 - `(optional)` 패스워드 encryption

## GET /logout
 - 로그아웃해야함.
 - `/login` 으로 rdirection.

## GET / `(login required)`
 - 최근에 로깅한 태그들이 보임
 - `/tags` 로 갈 수 있는 링크 있어야함. (태그 만들기라던가 )
 - `/logout` 할수있는 링크 있어야함.
 - `/users/<name>/statistics`로 갈수있는 링크 있어야함 (태그 통계)

## GET /tags `(login required)`
 - 태그의 이름(eg. 잠자기, 출발하기 등등) 을 기록할수있는 input 필드
 - 태그를 전송할수있는 버튼있어야함.
 _ `(optional)` 태그 자동 완성 해준다면? (ajax 사용해야겠지만.)

## POST /tags `(login required)`
 - 태그의 이름을 받아서 이름과 시간 저장해야함
 - 다끝나면 `/tags`로 redirection


## GET /users/<name>/statistics

 - 태그 이름 별로 몇번 태깅됬는지
 - 태그간의 평균 시간 간격 보여주는 페이지
