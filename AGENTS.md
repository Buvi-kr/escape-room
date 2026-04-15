# 🛡️ 도기탐정 '포우리' 프로젝트 마스터 블루프린트 (Master Blueprint)

본 문서는 포천 아트밸리 천문과학관 방탈출 '포우리' 프로젝트의 모든 기획, 로직, 시각적 가이드를 집대성한 **최종 청사진**입니다.

---

## 1. 📂 프로젝트 개요 & 아키텍처 (System Design)

### 🏗️ 기술 스택 및 구조
- **Architecture:** 단일 페이지 애플리케이션 (Single Page Application, SPA)
- **Core:** HTML5, CSS3 (Glassmorphism), Vanilla JavaScript (ES6+).
- **Storage:** 브라우저 `localStorage`를 이용한 실시간 세이브/로드 시스템.
- **Responsive:** 모바일 웹 환경(480px) 최적화 및 뷰포트 고정 디자인.

### 💾 기획 에이전트 설계 (Core Logic)
1. **상태 관리 컨셉 (State Agent):** 모든 액션은 `pouri_save` 객체에 저장됨.
2. **타이머 로직 (Time Agent):** 절대 시간차(`Date.now()`) 기반으로 백그라운드에서도 시간 흐름 유지.
3. **입력 노멀라이제이션 (Validation Agent):** 텍스트 정답 시 공백 제거 및 소문자 변환 로직 적용.

---

## 2. 🧩 시나리오 흐름 & 내러티브 데이터베이스 (Full Scenario Master)

| 단계 | 테마 (Action) | 상황 내러티브 (Narration) | 시각적 연출 및 연관 에셋 (Visual Prompt) |
| :--- | :--- | :--- | :--- |
| **Intro** | **태양풍 경보** | "긴급 상황! 강력한 태양풍이 관측됐어. 지구 방어막 '오메가 베리어'를 켜야 해!" | A cute detective puppy (Pouri) looking at a glowing holographic alert screen, red emergency lights, 8k. |
| **M01** | **시스템 로그인** | "방어 시스템에 로그인해야 해. ISS 데이터를 동기화하자!" | Pouri typing on a floating neon keyboard, ISS orbiting Earth in the background, futuristic UI. |
| **M02** | **산소 시스템** | "로그인 성공! 하지만 방어막 연료인 산소 에너지가 부족해. 지구의 탄생 데이터를 분석하자!" | Blue oxygen particles filling a glass sphere, primitive ocean Earth background. |
| **M03** | **코어 베리어** | "산소 복구 완료! 하지만 태양풍의 열기가 너무 뜨거워. 지구의 코어 에너지가 필요해!" | Glowing orange core inside a cutaway of Earth, radiant heat waves, high-tech lab. |
| **M04** | **중력 동기화** | "코어 보호 성공! 이제 지구의 단짝인 달의 중력 엔진을 켜야 해. 충돌 데이터를 찾아줘!" | Earth and Moon connected by a transparent gravity beam, cinematic space view. |
| **M05** | **좌표 매핑** | "1전시실 완료! 이제 방어막을 쏠 정확한 우주 좌표가 필요해. 수호자의 암호를 풀어봐!" | A holographic star chart with crosshairs focusing on a specific constellation (Sagittarius). |
| **M06** | **시야 보정** | "좌표 확보! 하지만 초점이 안 맞아. 망원경의 원리로 조준점을 선명하게 맞춰야 해!" | A massive futuristic telescope lens focusing light beams into a sharp point, cinematic optic effects. |
| **M07** | **회전 동력** | "조준 완료! 이제 강력한 에너지를 쏠 회전 동력이 필요해. 행성의 회전 힘을 빌려오자!" | A giant spinning turbine powered by the rotation of a gas giant (Jupiter). |
| **M08** | **이동 경로** | "동력 충전 완료! 마지막 코어를 켜러 가야 해. 달의 험난한 지형을 이동할 데이터를 가져와!" | A lunar rover driving across a cratered surface towards a glowing beacon, Earth rising. |
| **M09** | **에너지원 식별** | "3전시실 도착! 에너지가 불안정해. 밤하늘에서 스스로 빛나는 별의 정체를 밝혀 시스템을 안정화하자!" | Pouri examining a glowing star hologram, scientific data streams on a high-tech monitor. |
| **M10** | **베리어 가동** | "마지막이야! 태양을 관측하는 위성의 데이터를 가져와서 최종 방어막을 가동하자!" | Pouri activating a giant solar observation satellite (SOHO) hologram, a dazzling energy beam shooting into the sky. |
| **End** | **지구 수호** | "방어막 가동 성공! 태양풍을 막아냈어. 우리가 지구를 지켰어!" | Earth protected by a beautiful rainbow-colored energy dome, Pouri smiling proudly. |

---

## 3. 🧩 퀴즈 데이터베이스 (Quiz Database)

| No | 문제 (Question) - *이미지 텍스트 100% 반영* | 정답 (Answer) | 정답 형식 | 안내 (Guide) |
| :--- | :--- | :--- | :--- | :--- |
| **1** | ISS는 하루에 우리 지구를 몇 번 돌까요? (소수점 포함 · 예: 00.00) | `15.78` | 단답식 | 로비 보안 패널에 적혀있는 숫자를 찾아봐! |
| **2** | 뜨거운 열기를 식혀주고 생명이 태어날 수 있게 해준 이것은? | `바다` | 객관식(4) | 하늘에서 내린 비가 모여 만들어졌어요. 1전시실 지구 탄생 전시물에서 확인해봐! |
| **3** | 지구 가장 깊은 곳, 철과 니켈이 녹아 출렁거리는 이곳은? | `외핵` | 객관식(4) | 너무 뜨거워서 금속이 '액체' 상태인 곳이야. 지구 내부 구조 전시물을 살펴봐! |
| **4** | 지구가 마그마로 끓고 있을 때, 충돌한 행성의 이름은? | `테이아` | 단답식 | 1전시실 계단 아래에 있는 달 탄생과 관련된 게시물을 찾아봐! |
| **5** | 12월에 태어난 친구들을 지켜주는 별자리는? (11/23~12/24) | `궁수자리` | 객관식(4) | 황도 12궁 별자리 전시물을 찾아봐! 해당 별자리는 11월 23일~12월 24일생의 수호 별자리야. |
| **6** | 갈릴레이 망원경의 좁은 시야를 넓혀준 망원경은? | `케플러식` | 객관식(4) | 망원경 발달사 전시물에서 각 망원경의 특징을 비교해봐! |
| **7** | 태양계에서 가장 빠르게 돌아서 하루가 짧은 행성은? | `목성` | 단답식 | 행성 정보 게시판에서 각 행성의 자전 주기를 확인해봐! |
| **8** | 달에서 활동 반경을 넓혀준 '달의 자동차'는? | `월면차` | 객관식(4) | 달 탐사 장비 모형 앞에서 이름을 찾아봐! |
| **9** | 밤하늘에서 스스로 빛나는 별들의 정체는? 태양과 마찬가지로 고온 가스가 공 모양으로 모인 'OO'이다. | `항성` | 객관식(4) | 별에 관한 궁금증 전시물을 읽어봐! |
| **10** | 태양 관측을 위해 1995년 발사된 태양 관측 위성의 이름은? | `SOHO` | 단답식 | 태양 관측 위성에 대한 설명 전시물을 읽어봐! |

---

## 4. 🎨 UI 및 시각 에셋 연출 가이드 (Visual Production)

- **배경:** "Neon Futurism" (Cyberpunk + Space Science)
- **트랜지션 애니메이션**: 
  - 정답 시 화면 전체에 `Primary Color` 파동 효과.
  - 내러티브 화면에서는 `Interstellar` 같은 몽환적인 성운 배경 배치.

---

## 5. 🛠️ 구현 핵심 체크리스트 (Technical Check)

1. **상황 중계 카드**: 퀴즈 전후에 나타나는 '스토리 카드' 구현. (이미지 + 포우리 대사 + 계속하기 버튼)
2. **사운드 피드백**: 로그인 성공음, 시스템 가동 윙잉 소리 등 테마에 맞춘 효과음 배치 권장.
3. **키패드 UI**: 1번 미션 전용 `ㅁㅁ.ㅁㅁ` 디지털 패드 CSS 정밀 구현.
