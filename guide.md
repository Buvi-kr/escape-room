# 🎨 '포우리' 이미지 생성 프롬프트 가이드 (Nano Banana용)

이 가이드는 포천 아트밸리 천문과학관 방탈출 앱 '포우리'에 필요한 모든 시각 에셋의 생성 프롬프트를 정리한 것입니다. 모든 이미지는 **모바일 최적화(9:16 또는 3:4)** 및 **고급스러운 게임 그래픽 스타일**을 지향합니다.

---

## 🌌 공통 스타일 가이드
- **스타일 키워드:** Hyper-realistic, futuristic UI, vibrant space colors, cinematic lighting, sleek game interface style.
- **주요 톤:** Deep Blue (#0A0A2A), Gold (#FFD700), Cyan (#00F2FE).

---

## 0. 프롤로그 (로비 및 인트로)

| 위치 | 이미지 설명 | 권장 크기 | 나노 바나나 프롬프트 (English) |
| :--- | :--- | :--- | :--- |
| **타이틀 배경** | 과학관의 밤하늘과 방어막 UI | 1080x1920 | A futuristic space science museum at night with a giant holographic energy shield dome overhead, starlit sky, "POURI" logo aesthetic, cinematic lighting, 8k resolution, game title screen style. |
| **로비 문제 (ISS)** | 지구를 도는 ISS 위성 | 1080x800 | International Space Station (ISS) orbiting a glowing blue Earth, realistic space view, cinematic sunlight hitting the station, orbital path lines visible, high detail, scientific but artistic. |
| **이동 연출** | 과학관으로 뛰어가는 캐릭터 | 1080x1080 | A cute, brave space-detective puppy character (Pouri) running towards a glowing high-tech science museum building, futuristic background, dynamic pose, vibrant colors. |

---

## 1. 제1전시실 (지구 이야기)

| 위치 | 이미지 설명 | 권장 크기 | 나노 바나나 프롬프트 (English) |
| :--- | :--- | :--- | :--- |
| **P1-1 (바다)** | 원시 지구의 거대한 바다 | 1080x800 | Primitive Earth with a vast, stormy ocean under a volcanic sky, first life emerging, atmospheric lighting, epic scale, scientific illustration style. |
| **P1-2 (외핵)** | 지구의 내부 구조 (단면) | 1080x800 | Cross-section of Earth showing layers, focusing on a glowing liquid outer core (golden-orange), labeled "Outer Core" aesthetic, high-tech scientific diagram style. |
| **P1-3 (테이아)** | 지구와 테이아의 충돌 | 1080x800 | Giant impact hypothesis, a Mars-sized planet "Theia" colliding with early Earth, massive debris cloud, cinematic space disaster scene, hyper-realistic. |

---

## 2. 제2전시실 (별과 우주)

| 위치 | 이미지 설명 | 권장 크기 | 나노 바나나 프롬프트 (English) |
| :--- | :--- | :--- | :--- |
| **P2-1 (궁수자리)** | 황도 12궁 밤하늘 | 1080x800 | Sagittarius constellation glowing in a deep blue night sky, mythical centaur silhouette made of stars, celestial map aesthetic, mystical lighting. |
| **P2-2 (망원경)** | 케플러식 망원경 구조 | 1080x800 | A sleek, high-quality Keplerian refracting telescope, cutaway diagram showing lenses and light paths, professional scientific instrument look, studio lighting. |
| **P2-3 (목성)** | 거대한 목성과 대적점 | 1080x800 | Close-up of Jupiter with its colorful bands and the Great Red Spot, realistic textures, cinematic lighting from the sun, majestic space view. |

---

## 3. 휴게실 & 제3전시실 (최종 미션)

| 위치 | 이미지 설명 | 권장 크기 | 나노 바나나 프롬프트 (English) |
| :--- | :--- | :--- | :--- |
| **P3-1 (월면차)** | 달 표면의 월면차 | 1080x800 | Lunar Roving Vehicle (LRV) parked on the dusty grey surface of the moon, Earth rising in the background black sky, realistic Apollo mission aesthetic. |
| **P4-1 (히파르코스)** | 별의 등급 분류 차트 | 1080x800 | Ancient Greek astronomer Hipparchus observing stars, combined with a modern UI showing star magnitude classes (1 to 6), parchment meets digital HUD style. |
| **P4-2 (주계열성)** | 빛나는 주계열성 별 | 1080x800 | A bright, stable sun-like star (Main Sequence), intense solar flares, core fusion glow, cinematic space photography style, high energy. |

---

## 4. 에필로그 (엔딩)

| 위치 | 이미지 설명 | 권장 크기 | 나노 바나나 프롬프트 (English) |
| :--- | :--- | :--- | :--- |
| **엔딩 배경** | 복구된 포천 도시 | 1080x1920 | A beautiful, restored futuristic city of Pocheon, green parks, high-tech buildings, clear blue sky, a giant rainbow energy shield successfully deployed, peaceful and celebratory atmosphere. |
| **에너지 그래프** | 최종 에너지 충전 완료 | 1080x800 | A high-tech holographic UI panel showing 100% energy charge, futuristic graphs and data streaming, "SYSTEM STABILIZED" text, premium glassmorphism finish. |

---

## 💡 제작 팁
1. **일관성:** 모든 프롬프트 끝에 `--v 6.0` (또는 나노 바나나의 최신 엔진 설정)과 `high-quality, masterpiece`를 추가하세요.
2. **캐릭터:** '포우리' 캐릭터 이미지는 시트에 맞춰 통일된 외형이 나오도록 첫 이미지의 `seed` 값을 활용하면 좋습니다.
3. **비율:** 배경용은 `--ar 9:16`, 문제 삽입용은 `--ar 4:3` 또는 `--ar 1:1`로 설정하여 생성하세요.
