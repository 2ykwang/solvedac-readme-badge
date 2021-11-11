<div align="center">
    <h2 align="center">solvedac-readme-badge</h2>  
   solved.ac 유저 정보를 이용해 README.md에 사용 가능한 뱃지 또는 카드를 만들어주는 프로젝트 입니다.
   <br><br>
</div>

## TOC

- [TOC](#toc)
- [설치](#설치)
- [사용법](#사용법)
- [뱃지](#뱃지)
  - [설정 가능한 변수](#설정-가능한-변수)
    - [모양](#모양)
    - [테마](#테마)
    - [사이즈](#사이즈)
- [카드](#카드)
  - [설정 가능한 변수](#설정-가능한-변수-1)
    - [모양](#모양-1)
    - [테마](#테마-1)
    - [사이즈](#사이즈-1)

## 설치

```sh
# .env_example 을 복사하여
# .env 파일 생성
# API_HOST = "solved.ac"

# 저장소 클론
$ git clone https://github.com/2ykwang/solvedac-readme-badge .

# Virtual Environment 사용 할 경우
$ python3 -m venv .venv

# Linux
$ source .venv/bin/activate

# Windows
$ .\.venv\Scripts\activate.bat # Command Prompt
$ .\.venv\Scripts\activate.ps1 # Power Shell

# 실행
$ pip install -r requirements.txt
$ flask run

```

## 사용법

```markdown
- badge
  ![solvedac-badge](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=baekjoon_id_here)

- compact badge
  ![solvedac-badge-compact](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=baekjoon_id_here&compact=1)

- card (not implemented)

- compact card ( not implemented )
```

<br>

## 뱃지

### 설정 가능한 변수

매개변수를 이용해 뱃지 또는 카드를 사용자 정의할 수 있습니다.

e.g) `badge?user?(parameter)=(value)`

|     매개변수     |   타입    |                          설명                          | 기본 값   |                        값                         |
| :--------------: | :-------: | :----------------------------------------------------: | --------- | :-----------------------------------------------: |
|      `user`      |  string   |        solved.ac 에 등록된 아이디를 입력합니다.        | `None`    |               `username`,`2ykwang`                |
|     `theme`      |  string   |                 색 테마를 설정합니다.                  | `default` |      `테마` 항목 참고 `default`, `dark`, ...      |
|    `compact`     |  boolean  |                뱃지의 모양을 설정합니다                | `False`   |                 `true` or `false`                 |
|      `size`      |  string   |             뱃지 또는 카드의 크기 입니다.              | `medium`  | `사이즈` 항목 참고 `small` or `medium` or `large` |
|   `back_color`   | hex color |   배경 색을 설정합니다. 기본값은 테마 색을 따릅니다.   | `theme`   |           Hex Color code `333`,`939584`           |
| `use_back_color` |  boolean  |             배경색을 사용할지 설정합니다.              | `true`    |                 `true` or `false`                 |
|  `common_color`  | hex color | 메인 글씨색을 설정합니다. 기본값은 테마 색을 따릅니다. | `theme`   |           Hex Color code `333`,`efefef`           |
|   `sub_color`    | hex color | 보조 글씨색을 설정합니다. 기본값은 테마 색을 따릅니다. | `theme`   |           Hex Color code `333`,`efefef`           |
|  `border_color`  | hex color |  테두리 색을 설정합니다. 기본값은 테마 색을 따릅니다.  | `theme`   |           Hex Color code `333`,`efefef`           |
|   `use_border`   |  boolean  |             테두리를 사용할지 설정합니다.              | `True`    |                 `true` or `false`                 |

<br>

#### 모양

`compact` 파라미터를 사용해 모양을 설정할 수 있습니다.

e.g) `compact=true` or `compact=false`

|        값         |                                               compact                                                |
| :---------------: | :--------------------------------------------------------------------------------------------------: |
|      `True`       | ![preview](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=2ykwang&compact=1) |
| `False` (default) |     ![preview](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=2ykwang&)      |

기본값은 `false` 입니다.

<br>

#### 테마

`theme` 파라미터를 사용해 테마를 설정할 수 있습니다.

e.g:) `theme=onedark`, `theme=dark`, ...

|      값       |                                                   예시 URI /미리보기                                                   |
| :-----------: | :--------------------------------------------------------------------------------------------------------------------: |
|   `default`   |   ![default](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=2ykwang&theme=default&compact=1)   |
|    `swift`    |    ![default](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=2ykwang&theme=swift&compact=1)    |
|    `dark`     |      ![dark](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=2ykwang&theme=dark&compact=1)      |
|   `onedark`   |   ![onedark](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=2ykwang&theme=onedark&compact=1)   |
| `github-dark` | ![onedark](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=2ykwang&theme=github-dark&compact=1) |

<br>

#### 사이즈

`size` 파라미터를 사용해 사이즈를 설정 할 수 있습니다.

입력 가능한 값은 `small`, `medium`, `large` 입니다.

|        값        |                                                           미리보기                                                            |
| :--------------: | :---------------------------------------------------------------------------------------------------------------------------: |
| `small`(default) |  ![small](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=2ykwang&theme=default&compact=1&size=small)  |
|     `medium`     | ![medium](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=2ykwang&theme=default&compact=1&size=medium) |
|     `large`      |  ![large](https://solvedac-readme-badge.herokuapp.com/api/v1/generate/badge?user=2ykwang&theme=default&compact=1&size=large)  |

기본값은 `small` 입니다.

<br>

## 카드

### 설정 가능한 변수

#### 모양

#### 테마

#### 사이즈
