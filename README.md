# 바닐라 자바스크립트로 PWA 구축하기

Python/Django로 생성한 웹 사이트를 PWA로 업데이트 하기 위한 실습  

### PWA란? (PWA, Progressive Web App)

---

"**점진적 웹 앱(PWA)**"은 네이티브 앱과 같은 경험을 제공하기 위한 모던 웹 기술을 사용한 웹 애플리케이션이다. 이 앱들은 특정 요구 사항을 충족한다. 서버에 배포되고, URL을 통해서 접근 가능하고, 검색 엔진으로 색인된다.

PWA는 일반적인 앱처럼 동작하지만 많은 기능이 추가되었고 훨씬 덜 번거롭다. PWA는 빠르며 신뢰할 수 있고 오프라인 환경에서 완벽하게 동작한다.

### PWA를 사용하는 이유

---

PWA는 다음과 같은 것들로 사용자에게 풍부한 경험을 제공한다.

-   **반응형**

PWA는 데스크탑 브라우저, 모바일 기기, TV 화면 등 인터넷에 접속할 수 있고 브라우저를 지원하는 모든 제품에 맞게 만들 수 있다.

-   **신뢰성**

**서비스 워커(Service Worker)**  라는 기술을 사용해서 사용자의 환경에서 PWA를 즉시 로드할 수 있게 해준다. PWA는 애플리케이션을 위해 오프라인 지원을 제공할 수 있으며 사용자가 네트워크와 관련된 문제를 겪지 않는다.

-   **앱 스토어, 플레이 스토어가 필요 없음**

사용자들은 PWA를 다운로드하기 위해 앱 스토어를 방문할 필요가 없다. PWA는 브라우저를 통해서 바로 설치할 수 있다. 대기 시간이 없기 때문에 굉장히 빠르고 네이티브 애플리케이션과 같은 시뮬레이션 환경을 제공한다.

-   **개발자와 사용자 참여**

개발자들은 매니페스트 파일(manifest file)로 수많은 기능들을 추가하고 가지고 놀 수 있다. 가장 잘 알려진 기능 중 하나는 PWA에서 활성화 된 푸시 알림을 사용하여 사용자들을 다시 참여시키는 것이다.

-   **쉬운 공유**

PWA는 당신의 친구 또는 동료에게 굉장히 쉽게 공유할 수 있다. 사용자가 웹 사이트 또는 앱 URL만 공유하면 된다. 사용자는 설치 가능한 apk를 공유하거나 수많은 파일을 다운로드한 후에 검증 과정을 거칠 필요가 없다. 간단하게 클릭만 하면 된다.

PWA에 대해서 자세히 알고 싶다면  [Google Developers 사이트](https://developers.google.com/web/progressive-web-apps/)를 방문하면 된다.

### Reference

---

[# 바닐라 자바스크립트로 PWA 구축하기](https://ui.toast.com/weekly-pick/ko_20191007)