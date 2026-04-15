# 🛡️ 도기탐정 '포우리' 프로젝트 마스터 블루프린트 (Ultimate Master Prompt)

본 문서는 **포천 아트밸리 천문과학관**의 인터랙티브 방탈출 웹 애플리케이션 **'도기탐정의 태양풍 방어 대작전'**을 개발, 유지보수, 그리고 확장을 위한 최종 소스 오브 트루스(Source of Truth)입니다. 이 문서를 AI 코딩 어시스턴트에게 제공하면 즉시 고퀄리티의 코드를 생성할 수 있도록 정밀하게 설계되었습니다.

---

## 1. 🚀 프로젝트 비전 & 핵심 철학 (Vision & Identity)

- **핵심 목표**: 천문과학관 관람객(초등학생 및 가족 단위)이 전시물을 탐색하며 문제를 해결하는 즐거움을 제공.
- **주인공**: 포천 아트밸리 마스코트 **'도기탐정(포우리)'**.
- **무게중심**: 고퀄리티 시각 연출(Neon Futurism) + 매끄러운 사용자 경험 + 게임화(Gamification).
- **기술 제약**: 단일 HTML 파일(SPA) 지향, 외부 라이브러리 최소화(바닐라 JS/CSS), 모바일 웹(480px 이하) 최적화.

---

## 2. 🏗️ 시스템 아키텍처 및 로직 (Architectural Specs)

### 🏗️ 코어 기술 스택
- **Base**: HTML5, Semantic UI.
- **Style**: CSS3 (Glassmorphism, Flex/Grid Layout, Keyframe Animations).
- **Logic**: Vanilla JavaScript (ES6+).
- **Storage**: `localStorage` (Save-key: `pouri_save`)를 통한 실시간 상태 동기화.

### 💾 기능 에이전트 설계
1.  **State Manager**: `pouri_save` 객체에 닉네임, 현재 미션 번호, 시작 시간, 힌트 사용 횟수, 클리어한 미션 목록 저장.
2.  **Time Agent**: `Date.now()` 기반 절대 시간 측정. 브라우저 종료 후 재접속해도 경과 시간 유지.
3.  **Input Validator**: 텍스트 정답의 경우 `trim()`, `toLowerCase()`, 공백 제거 후 비교 처리.
4.  **UI/UX Agent**: 
    - **Neon Futurism Theme**: Deep Blue, Gold, Cyan 컬러 조합.
    - **Micro-interactions**: 정답 시 `glow`, 오답 시 `shake`, 게이지 바 `progressFill`.

---

## 3. 🧩 스토리 & 미션 데이터베이스 (Full Scenario Master)

| 단계 | 테마 (Action) | 상황 내러티브 (Narration) | 정답 | 정답 형식 | 힌트 (전시실 위치) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Intro** | **태양풍 경보** | "긴급 상황! 강력한 태양풍이 관측됐어. 지구 방어막 '오메가 베리어'를 켜야 해!" | - | - | - |
| **M01** | **시스템 로그인** | "방어 시스템에 로그인해야 해. ISS 데이터를 동기화하자!" | `15.78` | 숫자 (ㅁㅁ.ㅁㅁ) | 로비 보안 패널 숫자를 확인해! |
| **M02** | **산소 시스템** | "로그인 성공! 하지만 연료인 산소가 부족해. 지구의 탄생 데이터를 분석하자!" | `바다` | 객관식 | 1전시실 '지구의 탄생' 패널 참조 |
| **M03** | **코어 베리어** | "산소 복구 완료! 하지만 열기가 너무 뜨거워. 지구의 코어 에너지가 필요해!" | `외핵` | 객관식 | 1전시실 지구 단면 모형 확인 |
| **M04** | **중력 동기화** | "코어 보호 성공! 이제 지구의 단짝인 달의 중력 엔진을 켜야 해. 충돌 데이터를 찾아줘!" | `테이아` | 단답식 | 1전시실 '달의 탄생' 패널 (거대 충돌설) |
| **M05** | **좌표 매핑** | "1전시실 완료! 이제 방어막을 쏠 정확한 우주 좌표가 필요해. 수호자의 암호를 풀어봐!" | `궁수자리` | 객관식 | 2전시실 입구 황도 12궁 별자리판 |
| **M06** | **시야 보정** | "좌표 확보! 하지만 초점이 안 맞아. 망원경의 원리로 조준점을 선명하게 맞춰야 해!" | `케플러식` | 객관식 | 2전시실 망원경 종류 설명판 |
| **M07** | **회전 동력** | "조준 완료! 이제 강력한 에너지를 쏠 회전 동력이 필요해. 행성의 회전 힘을 빌려오자!" | `목성` | 단답식 | 2전시실 행성별 자전 주기 게시판 |
| **M08** | **이동 경로** | "동력 충전 완료! 마지막 코어를 켜러 가야 해. 달의 험난한 지형을 이동할 데이터를 가져와!" | `월면차` | 객관식 | 2층 휴게실 월면차 모형 옆 설명판 |
| **M09** | **시스템 안정** | "3전시실 도착! 에너지가 불안정해. 별의 밝기 데이터로 시스템을 안정화하자!" | `히파르코스` | 객관식 | 3전시실 입구 '별의 밝기' 패널 |
| **M10** | **베리어 가동** | "마지막이야! 별의 황금기 에너지를 뽑아내서 최종 방어막을 가동하자!" | `주계열` | 단답식 | 3전시실 안쪽 '별의 일생' 도표 |
| **End** | **지구 수호** | "방어막 가동 성공! 태양풍을 막아냈어. 우리가 지구를 지켰어!" | - | - | 결과 카드(닉네임, 시간, 증서) |

---

## 4. 🎨 시각 연출 및 이미지 가이드 (Visual Asset Matrix)

### 🌌 공통 스타일
- **Style Keywords**: Hyper-realistic, futuristic UI, vibrant space colors, cinematic lighting, sleek game interface.
- **Palette**: Deep Blue (`#0A0A2A`), Gold (`#FFD700`), Cyan (`#00F2FE`).

### 🖼️ AI 이미지 생성 프롬프트 목록
1.  **Title/Prologue**: `A futuristic space science museum at night with a giant holographic energy shield dome overhead, starlit sky, "POURI" logo aesthetic, cinematic lighting, 8k resolution, game title screen style.`
2.  **M01 (ISS)**: `International Space Station (ISS) orbiting a glowing blue Earth, realistic space view, cinematic sunlight hitting the station, orbital path lines visible, high detail.`
3.  **M02 (Ocean)**: `Primitive Earth with a vast, stormy ocean under a volcanic sky, first life emerging, atmospheric lighting, epic scale, scientific illustration style.`
4.  **M03 (Core)**: `Cross-section of Earth showing layers, focusing on a glowing liquid outer core (golden-orange), labeled "Outer Core" aesthetic, high-tech scientific diagram style.`
5.  **M04 (Theia)**: `Giant impact hypothesis, a Mars-sized planet "Theia" colliding with early Earth, massive debris cloud, cinematic space disaster scene, hyper-realistic.`
6.  **M05 (Constellation)**: `Sagittarius constellation glowing in a deep blue night sky, mythical centaur silhouette made of stars, celestial map aesthetic, mystical lighting.`
7.  **M06 (Telescope)**: `A sleek, high-quality Keplerian refracting telescope, cutaway diagram showing lenses and light paths, professional scientific instrument look, studio lighting.`
8.  **M07 (Jupiter)**: `Close-up of Jupiter with its colorful bands and the Great Red Spot, realistic textures, cinematic lighting from the sun, majestic space view.`
9.  **M08 (Rover)**: `Lunar Roving Vehicle (LRV) parked on the dusty grey surface of the moon, Earth rising in the background black sky, realistic Apollo mission aesthetic.`
10. **M09 (Stars)**: `Ancient Greek astronomer Hipparchus observing stars, combined with a modern UI showing star magnitude classes (1 to 6), parchment meets digital HUD style.`
11. **M10 (Main Sequence)**: `A bright, stable sun-like star (Main Sequence), intense solar flares, core fusion glow, cinematic space photography style, high energy.`
12. **Ending**: `A beautiful, restored futuristic city of Pocheon, green parks, high-tech buildings, clear blue sky, a giant rainbow energy shield successfully deployed, peaceful atmosphere.`

---

## 5. 🛠️ 구현 체크리스트 (Technical Checklist)

- [ ] **SPA Router**: 미션 번호 변화에 따라 `#app` 컨테이너의 내용을 교체하는 구조인가?
- [ ] **Glassmorphism UI**: 배경 흐림 처리(`backdrop-filter: blur()`)와 투명도 있는 다크 모드 UI가 조화로운가?
- [ ] **Digital Keypad**: 1번 미션 전 전용 입력창(ㅁㅁ.ㅁㅁ)이 디지털 폰트로 구현되었는가?
- [ ] **Interaction Feedback**: 정답 시 폭발하는 듯한 파동(Wave) 효과와 성공 효과음이 적용되었는가?
- [ ] **Result Card Capture**: 최종 화면에서 닉네임과 기록이 담긴 화면을 이미지로 캡처하거나 공유할 수 있는 인터페이스가 있는가?
- [ ] **Optimization**: 모든 이미지는 WebP 포맷으로 처리되어 초기 로딩 속도가 2초 이내인가?

---

## 6. 📢 AI 코딩 지시문 (AI Prompting Instruction)

> "위 마스터 블루프린트의 내용을 바탕으로, 포천 아트밸리 천문과학관 전용 방탈출 웹 앱 `index.html`을 개발해줘. 모든 코드는 단일 파일에 포함되어야 하며, 특히 `Glassmorphism` 디자인과 `Interstellar` 스타일의 애니메이션 연출에 집중해줘. 10개의 미션 데이터는 `const MISSIONS` 배열로 관리하고, 사용자의 진행 상황은 `localStorage`에 자동 저장되도록 해. 각 미션마다 도기탐정의 개성 넘치는 대사(도기 대사)와 힌트 보기 기능을 포함해줘."
