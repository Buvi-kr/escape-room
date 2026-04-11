# 🛡️ 도기탐정 '포우리' 프로젝트 마스터 블루프린트 (Master Blueprint)

본 문서는 포천 아트밸리 천문과학관 방탈출 '포우리' 프로젝트의 모든 기획, 로직, 시각적 가이드를 집대성한 **최종 청사진**입니다. 개발 전 이 문서를 통해 모든 흐름과 에셋 사양을 확정합니다.

---

## 1. 📂 프로젝트 개요 & 아키텍처 (System Design)

### 🏗️ 기술 스택 및 구조
- **Architecture:** 단일 페이지 애플리케이션 (Single Page Application, SPA)
- **Core:** HTML5, CSS3 (Glassmorphism), Vanilla JavaScript (ES6+).
- **Storage:** 브라우저 `localStorage`를 이용한 실시간 세이브/로드 시스템.
- **Responsive:** 모바일 웹 환경(480px) 최적화 및 뷰포트 고정 디자인.

### 💾 기획 에이전트 설계 (Core Logic)
1. **상태 관리 컨셉 (State Agent):**
   - 유저의 모든 액션(닉네임 입력, 미션 성공, 힌트 클릭)은 즉시 `pouri_save` 객체에 직렬화되어 저장됨.
   - 새로고침 시 이 데이터를 역산하여 마지막 위치와 시간을 복구함.
2. **타이머 로직 (Time Agent):**
   - `performance.now()` 대신 `Date.now()` 기반의 절대 시간차를 계산하여, 브라우저가 백그라운드로 가도 실제 시간이 흐르도록 설계.
3. **입력 노멀라이제이션 (Validation Agent):**
   - 텍스트 정답 비교 시 `trimmedValue.replace(/\s/g, "").toLowerCase()` 공식을 적용해 띄어쓰기나 대소문자 오류 방지.

---

## 2. 🌌 전체 게임 흐름 (Total Game Flow)

| 단계 | 화면 (Screen) | 주요 내용 및 액션 |
| :--- | :--- | :--- |
| **01** | **타이틀 (Title)** | 닉네임 입력 → '미션 시작' 버튼 클릭 |
| **02** | **프롤로그 (Prologue)** | 인트로 스토리 (태양풍 위기 상황 전달) |
| **03** | **스테이지 인트로 (Intro)** | 각 전시실 진입 전 목표와 배경 스토리 브리핑 |
| **04** | **미션 수행 (Mission)** | 배경 이미지 삽입 → 도기 탐정 대사 → 문제 풀이 (객관식/주관식) |
| **05** | **전시실 클리어 (Clear)** | 전시실 내 모든 미션 완료 시 보상 연출 및 시스템 복구율 게이지 상승 |
| **06** | **엔딩 (Ending)** | 최종 방어막 가동 성공 연출 및 결과 확인 |
| **07** | **결과 (Result)** | 최종 기록(시간, 힌트 수) 리포트 카드 출력 |

---

## 3. 🧩 데이터베이스 (Full Mission Database)

| No | 스테이지 | 미션 제목 | 문제 (Question) | 정답 (Answer) | 힌트 (Hint) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | 로비 | 시스템 로그인 | ISS는 하루에 지구를 몇 바퀴 돌까요? | `15.78` | 로비 보안 패널 숫자를 확인해! |
| **2** | 1전시실 | 산소 복구 | 생물이 살 수 있는 환경을 만들어준 핵심 요소는? | `바다` | 지구 탄생 초기 전시물을 봐. |
| **3** | 1전시실 | 코어 해제 | 지구 내부 층 중 액체 상태인 부분은? | `외핵` | 지구 내부 구조 표를 참고해. |
| **4** | 1전시실 | 에너지 확인 | 지구와 충돌한 화성 크기 행성의 이름은? | `테이아` | 거대 충돌설 설명판을 읽어봐. |
| **5** | 2전시실 | 에너지 키트 | 12월의 탄생 별자리는 무엇인가? | `궁수자리` | 입구 별자리판에서 12월을 찾아. |
| **6** | 2전시실 | 정화 작업 | 시야를 넓게 만든 굴절 망원경의 종류는? | `케플러식` | 망원경 발달사 전시물을 확인해. |
| **7** | 2전시실 | 동력 충전 | 목성의 하루 길이는 몇 시간인가? | `9.93` | 행성 정보 표의 자전 주기를 봐. |
| **8** | 휴게실 | 좌표 확보 | 우주인의 활동 반경을 넓혀준 이동 수단은? | `월면차` | 달 탐사 장비 모형 앞을 봐. |
| **9** | 3전시실 | 시스템 안정 | 별의 등급을 처음으로 분류한 천문학자는? | `히파르코스` | 별의 밝기 설명 패널을 읽어봐. |
| **10** | 3전시실 | 최종 베리어 | 수소 핵융합으로 가장 오래 빛나는 단계는? | `주계열` | 별의 일생 전시물을 확인해. |

---

## 4. 🎨 시각 에셋 마스터 가이드 (Visual & Prompt Assets)

### 💠 공통 스타일: "Neon Futurism"
- **Style:** Cyberpunk science, deep contrast, glowing HUD, premium glass textures.
- **Engine:** Nano Banana (DALL-E 3 / Midjourney v6 based).

| 폴더/파일 경로 | 대상 | 상세 생성 프롬프트 (Nano Banana용) |
| :--- | :--- | :--- |
| `assets/img/title_bg.png` | **타이틀 배경** | Futuristic space museum at night, starry sky with a giant energy shield globe, cinematic lighting, 8k, --ar 9:16 |
| `assets/img/p0_bg.png` | **ISS 장면** | International Space Station orbiting Earth, realistic space view, bright solar panels, high detail, --ar 4:3 |
| `assets/img/p1_bg.png` | **원시 지구** | Primitive Earth with stormy oceans, volcanic fire, and ancient sky, scientific illustration, --ar 4:3 |
| `assets/img/earth_core.png` | **지구 내부** | Cross-section of Earth, glowing liquid outer core (golden-orange energy), labeled style, --ar 4:3 |
| `assets/img/theia.png` | **거대 충돌** | High-speed impact of planet Theia hitting Earth, epic scale, space debris, cinematic, --ar 4:3 |
| `assets/img/sagittarius.png` | **궁수자리** | Sagittarius constellation glowing stars, celestial blue background, magical star map style, --ar 4:3 |
| `assets/img/telescope.png` | **망원경** | Keplerian refracting telescope diagram, clean modern lens layout, scientific tool, studio light, --ar 4:3 |
| `assets/img/jupiter.png` | **목성** | Close-up of Jupiter with Great Red Spot, vibrant atmosphere bands, realistic texture, --ar 4:3 |
| `assets/img/rover.png` | **월면차** | Lunar Roving Vehicle on the Moon surface, grey craters, Earth in background black sky, --ar 4:3 |
| `assets/img/hipparchus.png` | **천문학자** | Ancient star map, star magnitude classification UI overlay, futuristic parchment, --ar 4:3 |
| `assets/img/main_sequence.png` | **주계열성** | Bright stable sun-like star, intense solar flares, core fusion glow, cinematic space, --ar 4:3 |
| `assets/img/ending_bg.png` | **엔딩** | Restored futuristic city under a rainbow energy shield, peaceful green parks, celebration, --ar 9:16 |

---

## 5. 🎨 UI/UX 디자인 시스템 (Design Tokens)

- **Colors:** 
  - `Primary`: #00F2FE (Cyan Glow)
  - `Secondary`: #FFD700 (Star Gold)
  - `Danger`: #FF4757 (Red Alert)
  - `Background`: #050510 (Deep Void)
- **Typography:**
  - `Header`: Orbitron (700+) - 기계적이고 과학적인 느낌
  - `Body`: Noto Sans KR (400) - 가독성 중심
- **Interactions:**
  - **Glassmorphism**: 카드 배경에 `backdrop-filter: blur(10px)` 적용.
  - **Glow Effect**: 주요 버튼 및 글자에 `text-shadow` 및 `box-shadow`로 발광 효과 부여.

---

## 6. 🛠️ 구현 주의 사항 (Checklist)

1. **에셋 로딩**: 모든 이미지는 생성 후 `./assets/img/` 경로에 정확히 배치해야 함.
2. **반응형**: iPhone SE 등 작은 화면에서도 텍스트가 잘리지 않도록 버튼 패딩 조절 필수.
3. **정답 처리**: 주관식 정답 입력 시 한글의 경우 공백 제거 필수.
4. **힌트 패널**: 유저가 힌트를 볼 때마다 `hintsUsed` 카운트를 올려 결과창에 반영.
