# LOTTERY([바로가기](http://www.lottery-unist.ml) sample id: kangnam, pw: kangnam123)
## UNIST-멋사 2020 해커톤
### 발표자료(바로가기)
-----
## About us
### 팀원
| 팀원 | 담당 | 이메일 |
| ------ | ------ | ------ |
| 조영상 | 프론트(팀장) | luckyys610@unist.ac.kr |
| 차준형 | 백엔드/기획 | quffl9612@unist.ac.kr |
| 정현준 | 백엔드 | with1015@unist.ac.kr |
| 복영규 | 백엔드 | duckbankbok@unist.ac.kr |

### LOTTERY
#### LOTTERY란?
LOTTERY란 식품 코너의 라스트 오더에서 기인하여 남는 재고를 점주들끼리 실시간으로 거래하여 재고를 줄이는 웹 서비스입니다. LOTTERY는 점주들에겐 재고처리의 도움을 주고 손님들에겐 자신이 사고 싶은 제품이 가장 가까운 매장에서 품절이 되는 일이 없도록 도와줍니다. 뿐만 아니라 LOTTERY는 간단한 기계 학습을 통해 미래의 발주량을 예측해 점주들이 발주를 하는데 도움을 줍니다.

#### LOTTERY를 만들게 된 계기
실제로 크리스피 크림 도넛에서 알바를 하면서 발주량과 실제 판매량이 많은 요인들(e.g. 날씨, 주변 행사 등)로 인해 제각각으로 변하며 남는 재고 처리에 애를 쓴 경험을 토대로 LOTTERY란 서비스를 만들게 되었습니다.

#### LOTTERY 기능
  * 메인 페이지: 메인 페이지에서는 가장 급한 2개의 Share와 가장 급한 2개의 Request를 보여줍니다. 가장 급한 요청을 선별하는 기준은 시간이 가장 적게 남은 요청과 개수가 가장 많은 요청입니다.
 
  * Share/Request: Share는 남는 재고를 다른 지점에 공유하는 기능입니다. 재고가 남는 품목과 수량을 선택하고 요청 만료 시간을 설정하여 글 작성을 완료하시면 Share 페이지에 요청이 올라옵니다. Share와 반대되는 개념으로 Request는 부족한 재고를 다른 지점에 요청하는 기능입니다. 재고가 부족한 품목과 수량을 선택하고 요청 만료 시간을 설정하여 글 작성을 완료하시면 Request 페이지에 요청이 올라옵니다. 모든 요청은 위도, 경도 기준 가장 가까운 지점의 요청부터 표시됩니다. Share/Request 페이지에 올라온 요청을 보고 다른 지점 점주님들이 공유 요청을 하시면 자동으로 이메일을 통해 공유 요청을 전달해드립니다.

  * My Page: 마이페이지에서는 Share/Request 이력을 볼 수 있으며 이전 발주량(dummy)과 Share/Request 이력을 선형 회귀를 이용해 학습시켜 오늘 발주량을 과잉, 적정, 부족의 3가지 결과로 분류합니다. 발주량 예측은 10일 이상의 발주 기록이 있어야 하며, Share/Request 이력이 많아질수록 더 정확한 예측을 볼 수 있습니다. Sample id를 통해 구현을 확인하실 수 있습니다.

#### Future work(향후 개선방안)
  * 머신러닝 모델 개선: 실제 현장에서는 선형 회귀를 통한 머신러닝 모델이 적합하지 않은 경우가 대부분입니다. 그렇기 때문에 실제 판매량에 어떤 요인들이 적용되는지 알아보고 또한 그 요인들을 어떤 모델에 접목시킬지 분석하여 발주량을 예측하는 모델을 개선시킬 것입니다.

  * 사용자 인터페이스 개선(업데이트/삭제 등): 웹서비스를 배포하고 최종 테스트를 통해 알게 된 여러가지 인터페이스 문제점을 해소할 수 있도록 업데이트하겠습니다.

  * 여러 프랜차이즈 브랜드에 적용 가능하도록 제품 모델 확장: 현재 배포된 LOTTERY는 LOTTE GRS 사업 중 크리스피 크림 도넛을 예시로 만들어진 웹 서비스입니다. 향후 다른 LOTTE GRS 사업도 LOTTERY에 적용 가능하도록 제품 모델을 확장하겠습니다.
