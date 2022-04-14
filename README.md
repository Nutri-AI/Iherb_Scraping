# Iherb_Scrapping


<img width="700" alt="iherb_homepage" src="https://user-images.githubusercontent.com/64734692/163292271-9390f315-f50c-490d-828c-8078e4f80006.png"
     title="iherb homepage">
<br>

[Iherb Korea](https://kr.iherb.com/)에서 영양제 데이터를 수집함

## 수집한 데이터의 목록
<img width="800" alt="iherb_product_info" src="https://user-images.githubusercontent.com/64734692/163292633-300cbb4a-3196-4a92-9f04-d157979b124f.png">  
<br>
<img width="300" alt="iherb_supplement_fact" src="https://user-images.githubusercontent.com/64734692/163292706-377fb4d7-6805-47c9-b9ed-2bf4743bbed1.png">
<br>

- 영양제 이름 및 회사명
- 제품 코드
- 가격
- 영양 성분표

## How to use
<img width="1200" alt="iherb_categories" src="https://user-images.githubusercontent.com/64734692/163292967-b86b36df-e57a-43ee-aa9c-f1396b771f87.png">
<br>

- Write nutrient supplements categories among categories above in **categories.txt**
- Run **main.py**
- Files will be downloaded to **output** directory

## Arguments
usage:
```python
python3 run.py [--directory './output'] [—-sleep 1]
```
