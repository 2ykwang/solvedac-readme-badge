<div align="center">
    <h2 align="center">solvedac-readme-badge</h2> 
   solved.ac 유저 정보를 이용해 README.md에 사용 가능한 뱃지 또는 카드를 만들어주는 프로젝트 입니다.
</div>

## 사용법

```markdown
![solvedac](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/api?user=baekjoon_id_here)

![solvedac](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/api?user=baekjoon_id_here&compact=1)
```

<br>

## 사용자 정의 하기

### 설정 가능한 변수

매개변수를 이용해 뱃지 또는 카드를 사용자 정의할 수 있습니다.

e.g) `api?user?(parameter)=(value)`

|     매개변수      |   타입    |                          설명                          | 기본 값 |                   예시                   | 구현 |
| :---------------: | :-------: | :----------------------------------------------------: | ------- | :--------------------------------------: | ---- |
|      `theme`      |  string   |                 색 테마를 설정합니다.                  | default | `themes`항목 참고 `default`, `dark`, ... |      |
|      `type`       |  string   |                   타입을 설정합니다.                   | badge   |    `types` 항목 참고 `badge`, `card`     |      |
|     `compact`     |  boolean  |                뱃지의 모양을 설정합니다                | False   |            `true` or `false`             |      |
|      `size`       |  string   |             뱃지 또는 카드의 크기 입니다.              | medium  |      `small` or `medium` or `large`      |      |
|   `back_color`    | hex color |   배경 색을 설정합니다. 기본값은 테마 색을 따릅니다.   | theme   |     Hex Color code `#333`,`#939584`      |      |
| `use_back_color`  |  boolean  |             배경색을 사용할지 설정합니다.              | true    |            `true` or `false`             |      |
| `main_font_color` | hex color | 메인 글씨색을 설정합니다. 기본값은 테마 색을 따릅니다. | theme   |     Hex Color code `#333`,`#efefef`      |      |
| `sub_font_color`  | hex color | 보조 글씨색을 설정합니다. 기본값은 테마 색을 따릅니다. | theme   |     Hex Color code `#333`,`#efefef`      |      |
|  `border_color`   | hex color |  테두리 색을 설정합니다. 기본값은 테마 색을 따릅니다.  | theme   |     Hex Color code `#333`,`#efefef`      |      |
|   `use_border`    |  boolean  |             테두리를 사용할지 설정합니다.              | true    |            `true` or `false`             |      |

<br>

### 테마

`theme` 파라미터를 사용해 테마를 설정할 수 있습니다.

e.g:) `theme=onedark`, `theme=dark`, ...

|   테마    |                                              예시 URI /미리보기                                               |
| :-------: | :-----------------------------------------------------------------------------------------------------------: |
| `default` |    `https://solvedac-readme-badge.herokuapp.com/api/v1/generate/api?user=2ykwang&theme=default&compact=1`     |
|           | ![dark](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/api?user=2ykwang&theme=default&compact=1) |
|  `dark`   |      `https://solvedac-readme-badge.herokuapp.com/api/v1/generate/api?user=2ykwang&theme=dark&compact=1`      |
|           |  ![dark](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/api?user=2ykwang&theme=dark&compact=1)   |
| `onedark` |    `https://solvedac-readme-badge.herokuapp.com/api/v1/generate/api?user=2ykwang&theme=onedark&compact=1`     |
|           | ![dark](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/api?user=2ykwang&theme=onedark&compact=1) |

<br>

### 타입

`type` 매개변수를 사용해 모양 타입을 설정 할 수 있습니다.

e.g) `type=badge` or `type=card`

#### 뱃지

|       타입        |                                              미리보기                                              |
| :---------------: | :------------------------------------------------------------------------------------------------: |
|      `badge`      |     ![preview](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/api?user=2ykwang&)      |
| `badge` (compact) | ![preview](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/api?user=2ykwang&compact=1) |

#### 카드

|       타입       | 미리보기 |
| :--------------: | :------: |
|      `card`      |          |
| `card` (compact) |          |
